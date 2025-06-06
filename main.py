import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os

# 🔧 Função para limpar strings invisíveis
def limpar_strings_invisiveis(df):
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str).str.replace('\u200b', '', regex=False).str.strip()
    df.columns = [col.replace('\u200b', '').strip() for col in df.columns]
    return df

def agrupar_por_setor(df, mapeamento):
    df = df.copy()
    df['Setor'] = df['category'].replace(mapeamento)
    agrupado = df.groupby('Setor')[['userMessages', 'agentMessages']].sum().reset_index()
    agrupado['Total'] = agrupado['userMessages'] + agrupado['agentMessages']
    agrupado = agrupado.rename(columns={
        'userMessages': 'Recebido',
        'agentMessages': 'Enviado'
    })
    return agrupado.sort_values(by='Total', ascending=False)

def gerar_grafico_barras(df, titulo, nome_arquivo):
    plt.figure(figsize=(12, 6))
    plt.bar(df['Setor'], df['Mensagens'], color='#5DADE2')
    plt.title(titulo, fontsize=14)
    plt.xlabel('Setor')
    plt.ylabel('Mensagens')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(nome_arquivo)
    plt.close()

def salvar_relatorio_em_pdf_com_graficos(relatorios, nomes_relatorios, nome_pdf='relatorio_ezchat.pdf'):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    for nome, df in zip(nomes_relatorios, relatorios):
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.set_text_color(30, 30, 30)
        pdf.cell(0, 10, f"{nome}", ln=True)

        if nome == "Rateio GupShup":
            pdf.set_font("Arial", '', 10)
            pdf.ln(5)
            pdf.multi_cell(0, 10, "(Cálculo realizado apenas através das mensagens enviadas)")
            pdf.ln(5)

        if nome != "Conversas Humanas":
            # Detectar qual coluna usar no gráfico
            if 'Mensagens' in df.columns:
                df_grafico = df[['Setor', 'Mensagens']]
            elif 'Enviado' in df.columns:
                df_grafico = df[['Setor', 'Enviado']].rename(columns={'Enviado': 'Mensagens'})
            elif 'Total' in df.columns:
                df_grafico = df[['Setor', 'Total']].rename(columns={'Total': 'Mensagens'})
            else:
                continue

            nome_imagem = f"grafico_{nome.lower().replace(' ', '_')}.png"
            gerar_grafico_barras(df_grafico, f"Mensagens - {nome}", nome_imagem)
            pdf.image(nome_imagem, x=10, y=40, w=190)
            pdf.ln(130)
            os.remove(nome_imagem)
        else:
            pdf.ln(20)

        # Tabela
        pdf.set_font("Arial", 'B', 10)
        col_width = 190 / len(df.columns)
        row_height = 8

        for col in df.columns:
            pdf.set_fill_color(200, 220, 255)
            pdf.cell(col_width, row_height, str(col), border=1, align='C', fill=True)
        pdf.ln()

        pdf.set_font("Arial", '', 9)
        for _, row in df.iterrows():
            for item in row:
                texto = str(item)
                if len(texto) > 20:
                    texto = texto[:17] + "..."
                pdf.cell(col_width, row_height, texto, border=1)
            pdf.ln()

    pdf.output(nome_pdf)
    print(f"✅ PDF gerado com sucesso: {nome_pdf}")

# 🚀 Fluxo principal
arquivo_excel = 'relatorio-abril-25.xlsx'
df = pd.read_excel(arquivo_excel)
df = limpar_strings_invisiveis(df)

# Mapeamento de categorias
mapeamento = {
    "Assistência": "Assistencia 24h",
    "Sac Consultor Assistência 24h": "Assistencia 24h",
    "TATO - SUPORTE A REDE PRESTADOR": "Assistencia 24h",
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
    "Atendimento Consultor Eventos": "Eventos",
}

# 🔍 Relatório GupShup (apenas mensagens enviadas)
df_oficial = df[df['oficial'] == True]
relatorio_gupshup = agrupar_por_setor(df_oficial, mapeamento)[['Setor', 'Enviado']]
relatorio_gupshup = relatorio_gupshup.rename(columns={'Enviado': 'Mensagens'})
total_gupshup = relatorio_gupshup['Mensagens'].sum()
relatorio_gupshup['percentual'] = relatorio_gupshup['Mensagens'].apply(
    lambda x: f"{round((x / total_gupshup) * 100, 2)} %"
)

# 🌐 Relatório EzChat completo
relatorio_geral = agrupar_por_setor(df, mapeamento)
relatorio_geral['percentual'] = relatorio_geral['Total'].apply(
    lambda x: f"{round((x / relatorio_geral['Total'].sum()) * 100, 2)} %"
)

# ➕ Relatório de Totais (sem gráfico)
total_recebido = df['userMessages'].sum()
total_enviado = df['agentMessages'].sum()
total_geral = total_recebido + total_enviado
relatorio_total = pd.DataFrame([{
    'Setor': 'Todos os Setores',
    'Recebido': total_recebido,
    'Enviado': total_enviado,
    'Total': total_geral,
    'percentual': '100 %'
}])

# 📄 Gerar PDF
salvar_relatorio_em_pdf_com_graficos(
    relatorios=[relatorio_gupshup, relatorio_geral, relatorio_total],
    nomes_relatorios=["Rateio GupShup", "Rateio EzChat", "Conversas Humanas"]
)
