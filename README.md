# Projeto de Geração de Relatórios em PDF

Este projeto processa dados de um arquivo Excel, agrupa informações por categorias e gera um relatório em PDF com tabelas formatadas. O objetivo é organizar os dados em categorias oficiais e não oficiais, facilitando a visualização e análise dos dados.

## Sumário

- [Visão Geral](#visão-geral)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como Executar](#como-executar)
- [Detalhes do Código](#detalhes-do-código)
- [Contato](#contato)

## Visão Geral

O programa lê dados de um arquivo Excel (`.xlsx`), processa as informações, ajusta as categorias conforme regras definidas e gera um relatório em PDF contendo tabelas separadas para categorias oficiais e não oficiais.



## Pré-requisitos

- Python 3.6 ou superior.
- Bibliotecas Python:
  - `pandas`
  - `fpdf`
  - `openpyxl` (necessário para o `pandas` ler arquivos Excel)

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git

	2.	Navegue até o diretório do projeto:

cd seu_repositorio


	3.	Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv

Ative o ambiente virtual:
	•	No Windows:

venv\Scripts\activate


	•	No Unix ou MacOS:

source venv/bin/activate


	4.	Instale as dependências:

pip install pandas fpdf openpyxl

Ou, se você tiver um arquivo requirements.txt, use:

pip install -r requirements.txt



Como Executar

	1.	Verifique o arquivo de dados:
Certifique-se de que o arquivo .xlsx que vai ser lido está no diretório raiz do projeto ou ajuste o caminho no arquivo main.py.
	2.	Execute o programa:

python main.py


	3.	Resultado:
	•	Um arquivo PDF chamado .pdf será gerado no diretório atual.
	•	O console exibirá uma mensagem confirmando a geração do PDF.

Detalhes do Código

categoria_info.py

Define a classe CategoriaInfo, que encapsula as informações de cada categoria:
	•	Atributos:
	•	categoria: Nome da categoria.
	•	total_chats: Número total de chats.
	•	user_messages: Número de mensagens dos usuários.
	•	agent_messages: Número de mensagens dos agentes.
	•	total_mensagens: Soma das mensagens de usuários e agentes.
	•	oficial: Indica se a categoria é oficial (True) ou não oficial (False).

data_processor.py

Contém a classe DataProcessor, responsável por:
	•	Ler o arquivo Excel usando pandas.
	•	Ajustar as categorias com base em regras de substituição.
	•	Agrupar os dados por categoria ajustada e indicador oficial/não oficial.
	•	Retornar uma lista de objetos CategoriaInfo.

categorias_grupo.py

Define a classe CategoriasGrupo, que:
	•	Recebe uma lista de CategoriaInfo.
	•	Separa as categorias em listas de oficiais e não oficiais para facilitar o processamento posterior.

pdf_report_generator.py

Contém a classe PDFReportGenerator, que:
	•	Recebe as listas de categorias oficiais e não oficiais.
	•	Gera um relatório em PDF contendo tabelas formatadas para cada grupo.
	•	Utiliza a biblioteca fpdf para criação do PDF.

main.py

Arquivo principal que:
	•	Inicializa o DataProcessor com o caminho do arquivo Excel.
	•	Processa os dados e obtém a lista de categorias.
	•	Cria um objeto CategoriasGrupo para organizar as categorias.
	•	Inicializa o PDFReportGenerator e gera o relatório em PDF.

Contato

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato:
	•	Email: wanderson.martins@primeresults.com.br
	•	GitHub: WandersonM

---