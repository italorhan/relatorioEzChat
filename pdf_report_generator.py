from fpdf import FPDF

class PDFReportGenerator:
    def __init__(self, oficiais, nao_oficiais, title="Consumo EZCHAT"):
        self.oficiais = oficiais
        self.nao_oficiais = nao_oficiais
        self.title = title

    def generate_pdf(self, output_path):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=8)

        # Configuração das larguras das colunas
        col_widths = {
            "categoria": 40,
            "chats": 20,
            "mensagens_usuario": 30,
            "mensagens_agente": 30,
            "total_mensagens": 30,
        }
        table_width = sum(col_widths.values())  # Largura total da tabela

        pdf.add_page()
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(200, 10, txt=self.title, ln=True, align='C')
        pdf.ln(5)

        x_start = (210 - table_width) / 2  # 210 é a largura da página A4

        def add_table(pdf, x_start, col_widths, data_list, table_title):
            # Adicionar cabeçalho da tabela
            pdf.set_x(x_start)  # Centralizar
            pdf.set_font("Arial", style='BU', size=10)
            pdf.cell(table_width, 10, table_title, ln=True, align='C')
            pdf.ln(2)

            pdf.set_font("Arial", style='B', size=8)
            # Cabeçalhos da tabela
            pdf.set_x(x_start)
            pdf.cell(col_widths["categoria"], 8, "Categoria", border=1, align='C')
            pdf.cell(col_widths["chats"], 8, "Chats", border=1, align='C')
            pdf.cell(col_widths["mensagens_usuario"], 8, "Mensagens Usuário", border=1, align='C')
            pdf.cell(col_widths["mensagens_agente"], 8, "Mensagens Agente", border=1, align='C')
            pdf.cell(col_widths["total_mensagens"], 8, "Total Mensagens", border=1, align='C', ln=True)

            pdf.set_font("Arial", size=8)
            for categoria in data_list:
                pdf.set_x(x_start)  # Centralizar cada linha
                pdf.cell(col_widths["categoria"], 8, categoria.categoria, border=1, align='C')
                pdf.cell(col_widths["chats"], 8, str(categoria.total_chats), border=1, align='C')
                pdf.cell(col_widths["mensagens_usuario"], 8, str(categoria.user_messages), border=1, align='C')
                pdf.cell(col_widths["mensagens_agente"], 8, str(categoria.agent_messages), border=1, align='C')
                pdf.cell(col_widths["total_mensagens"], 8, str(categoria.total_mensagens), border=1, align='C', ln=True)

            pdf.ln(10)

        add_table(pdf, x_start, col_widths, self.oficiais, "API Oficial")

        add_table(pdf, x_start, col_widths, self.nao_oficiais, "API Não Oficial")

        pdf.output(output_path)
        print(f"PDF gerado com sucesso: {output_path}")