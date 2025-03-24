# 🌤 **Desafio - Desenvolvedor Jr.**

## 📌 Descrição
Este projeto consiste na criação de uma API REST para buscar previsões do tempo de cidades utilizando uma API pública (OpenWeatherMap ou WeatherAPI) e armazená-las em um banco de dados. A API permite consultar dados históricos, filtrar previsões por cidade e data, além de excluir registros.

---

## 🚀 Tecnologias Que Podem Ser Utilizadas
- **Linguagem:** Python 3.x  
- **Framework:** FastAPI ou Flask  
- **Banco de Dados:** SQLite ou PostgreSQL  
- **ORM:** SQLAlchemy  
- **API Externa:** OpenWeatherMap ou WeatherAPI  
- **Versionamento de Código:** Git  

---

## 📖 Funcionalidades

### 🔹 Endpoints Disponíveis

1. **Buscar previsão do tempo e armazenar no banco**  
   - `POST /previsao/`  
   - **Payload:** `{ "cidade": "São Paulo" }`  
   - **A API busca os dados na OpenWeatherMap e armazena no banco, associando-os à cidade e à data da consulta.**  

2. **Listar todas as previsões armazenadas**  
   - `GET /previsao/`  

3. **Buscar previsões filtrando por cidade e data**  
   - `GET /previsao?cidade=São Paulo&data=2024-03-20`  

4. **Excluir uma previsão armazenada**  
   - `DELETE /previsao/{id}`  

---

## ✅ Requisitos Mínimos
Para realizar este desafio, é necessário ter conhecimento básico em:
- Python  
- FastAPI ou Flask  
- SQL e ORMs (SQLAlchemy)  
- Consumo de APIs externas  
- Banco de dados (SQLite ou PostgreSQL)  

---

## 🧪 Testes Automatizados  
Os testes são um diferencial! Se puder, implemente testes automatizados usando `pytest` para validar os endpoints.  

Para rodar os testes:  
```bash
pytest tests/
```

---

🎯 Bônus
Quer se destacar ainda mais? Implemente uma interface visual utilizando Streamlit para demonstrar o consumo da sua API!

💡 Sugestões de Recursos para o Streamlit:
Criar um campo de input para que o usuário digite o nome da cidade e visualize a previsão do tempo retornada pela API.

---

## 📝 Critérios de Avaliação  
O projeto será avaliado com base nos seguintes critérios:
- Clareza e organização do código  
- Uso adequado do framework escolhido  
- Boas práticas de API REST  
- Estrutura e organização do projeto  
- Implementação de testes (se aplicável)  

---

## Obs:

OpenWeatherMap:
- O plano gratuito permite até 1.000 chamadas de API por dia.
Inclui dados atuais, previsões e acesso a dados históricos limitados.
Para acessar funcionalidades adicionais ou aumentar o limite de chamadas, é necessário assinar um dos planos pagos. 

WeatherAPI:
- O plano gratuito oferece acesso a dados em tempo real, previsões de 14 dias, dados históricos e outros recursos.
No entanto, pode haver limitações no número de chamadas ou recursos disponíveis. 

🚀 **Boa sorte e bom desenvolvimento!** 🚀
