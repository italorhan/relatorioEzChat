from data_processor import DataProcessor
from categorias_grupo import CategoriasGrupo
from pdf_report_generator import PDFReportGenerator

def main():
    file_path = "agv-abril-25.xlsx" ## Caminho para o relatorio fornecedido pelo time do EZchat.

    data_processor = DataProcessor(file_path)
    categorias = data_processor.process_data()

    categorias_grupo = CategoriasGrupo(categorias)

    pdf_generator = PDFReportGenerator(
        oficiais=categorias_grupo.oficiais,
        nao_oficiais=categorias_grupo.nao_oficiais,
        title="Ezchat consumo Abril 2025" # Inserir aqui o titulo do relatorio.
    )
    output_pdf_path = "ReportEzchatConsumo.pdf" # Caminho de saida do relatorio em pdf.
    pdf_generator.generate_pdf(output_pdf_path)

if __name__ == "__main__":
    main()