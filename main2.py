import pandas as pd

def agrupar_por_setor(df, mapeamento):
    """
    Agrupa mensagens por setor, renomeando categorias, somando mensagens e calculando percentual.
    """
    df = df.copy()
    df['Setor'] = df['category'].replace(mapeamento)

    # Agrupar
    agrupado = df.groupby('Setor')[['userMessages', 'agentMessages']].sum().reset_index()

    # Total de mensagens e percentual
    agrupado['Total'] = agrupado['userMessages'] + agrupado['agentMessages']
    total_geral = agrupado['Total'].sum()
    agrupado['percentual'] = agrupado['Total'].apply(
        lambda x: f"{round((x / total_geral) * 100, 2)} %"
    )

    # Renomear colunas
    agrupado = agrupado.rename(columns={
        'userMessages': 'Recebido',
        'agentMessages': 'Enviado'
    })

    return agrupado.sort_values(by='Total', ascending=False)

# Caminho do arquivo
arquivo_excel = 'relatorio-abril-25.xlsx'
df = pd.read_excel(arquivo_excel)

# Mapeamento de categorias (resumo)
mapeamento = {
    "Assistência": "Assistencia 24h (Tato)",  
    "Evento - Análise de evento": "Eventos",
    "evento - Cuiabá": "Eventos",
    "Cobrança - Núcleo PE": "Cobrança",
    "Eventos - NE​": "Eventos",
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
    "Contato - Agendamento": "Rastreador",  
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
    "Atendimento Consultor Eventos": "Eventos"
}

# Gerar relatórios
df_oficial = df[df['oficial'] == True]
relatorio_oficial = agrupar_por_setor(df_oficial, mapeamento)
total_enviado = relatorio_oficial['Enviado'].sum()
relatorio_oficial['percentual'] = relatorio_oficial['Enviado'].apply(
    lambda x: f"{round((x / total_enviado) * 100, 2)} %"
)

relatorio_nao_oficial = agrupar_por_setor(df[df['oficial'] == False], mapeamento)

relatorio_geral = agrupar_por_setor(df, mapeamento)

# Exibir
print("=== SOMENTE GUPSHUP ===")
print(relatorio_oficial)
print("\n=== SOMENTE EZCHAT ===")
print(relatorio_nao_oficial)
print("\n=== GUPSHUP/EZCHAT ===")
print(relatorio_geral)