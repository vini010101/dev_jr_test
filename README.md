# Previsão do Tempo - Teste Técnico (Dev Junior Backend)

Este projeto foi desenvolvido como parte de um **teste técnico** para a posição de **Dev Junior Backend**. A aplicação consiste em uma **API FastAPI** que fornece previsões do tempo para diferentes cidades e uma interface **Streamlit** para visualização e interação com a API.

## Tecnologias Usadas

- **FastAPI**: Framework para a construção de APIs em Python.
- **Streamlit**: Biblioteca para criar interfaces web de forma rápida e interativa.
- **SQLite**: Banco de dados utilizado para armazenar as previsões.

## Como Rodar o Projeto

### 1. Instalar Dependências

Clone o repositório e instale as dependências com o comando:

```bash
pip install -r requirements.txt

2. Rodar a API (FastAPI)
Navegue até a pasta da API e execute o seguinte comando para rodar a API:

uvicorn app.main:app --reload
A API estará disponível em http://127.0.0.1:8000/.


3. Rodar a Interface (Streamlit)
Abra um Novo Terminal e execute
streamlit run app_streamlit.py
A interface estará disponível em http://localhost:8501/.


Funcionalidades
Buscar previsão do tempo: O usuário pode buscar a previsão do tempo para uma cidade cadastrada.

Excluir previsão: O usuário pode excluir a previsão de uma cidade específica do banco de dados.

Como Funciona
API FastAPI
GET /previsao: Retorna a previsão de uma cidade.

DELETE /previsao/{cidade}: Exclui a previsão de uma cidade.

Interface Streamlit
O usuário pode buscar previsões digitando o nome de uma cidade.

Também pode excluir previsões já salvas ao inserir o nome da cidade e clicar no botão "Excluir Previsão".

Decisões Técnicas
FastAPI foi escolhido por ser rápido, moderno e simples para desenvolver APIs RESTful com alto desempenho.

Streamlit foi escolhido pela sua capacidade de criar interfaces interativas de maneira rápida e simples, ideal para protótipos e testes técnicos.

SQLite foi utilizado por ser um banco de dados leve, fácil de configurar e suficientemente robusto para este projeto.

Como Testar
Inicie a API e a interface conforme descrito acima.

Na interface do Streamlit, busque a previsão para uma cidade como "São Luís".

Teste a exclusão de uma cidade digitando o nome da cidade e clicando no botão "Excluir Previsão".

