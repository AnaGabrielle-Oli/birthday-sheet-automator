# Birthday-sheet-automator 🎂

Birthday é um script em Python que automatiza a verificação de aniversariantes do dia. Ele se conecta a uma planilha do Google Sheets, lê uma lista de nomes e datas de aniversário, e identifica quais pessoas estão fazendo aniversário na data atual.

##Funcionalidades
Conexão Segura: Utiliza a API do Google Sheets com autenticação via service_account para acessar os dados de forma segura.

 - Verificação Automática: Compara o dia e o mês atuais com a lista de aniversários na planilha.

 - Flexibilidade: Lê os dados da planilha utilizando a biblioteca pandas, permitindo fácil manipulação e extensão.

 - Saída Clara: Exibe no console os nomes dos aniversariantes.

##Tecnologias Utilizadas
 - Python

 - Pandas: Para manipulação e análise de dados.

 - Gspread: Para interagir com a API do Google Sheets.

 - Google Cloud Platform (GCP): Para gerenciamento de APIs e credenciais.
