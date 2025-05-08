import string
import pandas as pd
import re
from categoria_info import CategoriaInfo


def adjust_category(category):
    substituicoes = {
        "Assistência": "Assistencia 24h (Tato)",  
        "Sac Consultor Assistência 24h": "Assistencia 24h (Tato)",  
        "TATO - SUPORTE A REDE PRESTADOR": "Assistencia 24h (Tato)",  
        "Cadastro - Atualização Cadastral": "Cadastro",  
        "Cadastro - Reativação": "Cadastro",  
        "Cadastro - Titularidade": "Cadastro",  
        "Cadastro - Troca de Veiculo": "Cadastro",  
        "Cadastro - VistoCode": "Cadastro",  
        "Cadastro - VistoCode - Migrações": "Cadastro",  
        "C.A.T. - Atendimento": "Cat",  
        "Cobrança - Cobrança": "Cobrança",  
        "Cobrança - Núcleo MT": "Cobrança",  
        "Cobrança - Reativação": "Cobrança",  
        "Cartruck Geral": "Eventos",  
        "Eve - Abertura / Colisão": "Eventos",  
        "Eve - Acompanhamento (Ativo)": "Eventos",  
        "Eve - Atendimento": "Eventos",  
        "Eve - Atendimento | Furto e Roubo": "Eventos",  
        "Eve - Carro Reserva": "Eventos",  
        "Eve - Regulagem": "Eventos",  
        "Eve - Ressarcimento": "Eventos",  
        "Eve - Vidros": "Eventos",  
        "Evento": "Eventos",  
        "Evento - Abertura": "Eventos",  
        "Evento - Acompanhamento": "Eventos",  
        "Evento - Autorização de oficina": "Eventos",  
        "Evento - Carro Reserva": "Eventos",  
        "Evento - Direcionamento de Oficina": "Eventos",  
        "Evento - Relacionamento Regulagem": "Eventos",  
        "Evento - Ressarcimento": "Eventos",  
        "Eventos - Acordos": "Eventos",  
        "Eventos - NE": "Eventos",  
        "Eventos - Vidros": "Eventos",  
        "Atendimento - Núcleo São Paulo": "Núcleo São Paulo",  
        "teste": "Operações e Serviços de TI",  
        "Contato - Agendamento": "Rastreamento",  
        "Atendimento Consultor Rastreador": "Rastreador",  
        "Rastreador - Acesso ao monitoramento": "Rastreador",  
        "Rastreador - Agendamento": "Rastreador",  
        "Rastreador - Atendimento ativo": "Rastreador",  
        "Rastreador - Informações técnicas": "Rastreador",  
        "Rastreador - Outras informações": "Rastreador",  
        "2 Via Boleto - Atendimento": "Suporte",  
        "Sup - Boas vindas": "Suporte",  
        "Sup - Suporte": "Suporte",  
        "Suporte - 2° Via de boleto": "Suporte",  
        "Suporte - Atendimento": "Suporte",  
        "Suporte - Atualização cadastral": "Suporte",  
        "Suporte - Boas Vindas": "Suporte",  
        "Suporte - Cancelamento": "Suporte",  
        "Suporte - Retenção": "Suporte",  
        "Suporte Boas Vindas - NE": "Suporte",
    }

    # Substituir com base no mapeamento
    for chave, valor in substituicoes.items():
        if chave.lower() in category.lower():
            return valor.capitalize()

    return''.join([x for x in category.capitalize() if x in string.printable])


class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def process_data(self):
        self.data = pd.read_excel(self.file_path)

        self.data['category_ajustada'] = self.data['category'].apply(adjust_category)

        grouped_data = self.data.groupby(['category_ajustada', 'oficial']).agg(
            total_chats=('total', 'sum'),
            user_messages=('userMessages', 'sum'),
            agent_messages=('agentMessages', 'sum')
        ).reset_index()

        categorias = []
        for _, row in grouped_data.iterrows():
            categoria_info = CategoriaInfo(
                categoria=row['category_ajustada'],
                total_chats=row['total_chats'],
                user_messages=row['user_messages'],
                agent_messages=row['agent_messages'],
                oficial=row['oficial']
            )
            categorias.append(categoria_info)

        return categorias