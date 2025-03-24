API de Previsão do Tempo com FastAPI, Docker e PostgreSQL
Visão Geral
Este projeto consiste em uma API REST criada com o FastAPI, que permite consultar previsões do tempo para diferentes cidades utilizando a OpenWeatherMap API. As previsões são armazenadas em um banco de dados PostgreSQL e podem ser consultadas, filtradas por cidade e data, ou deletadas. Além disso, a aplicação é configurada para ser executada em um ambiente Docker.

Este README fornece uma explicação detalhada sobre como o projeto está estruturado, como configurá-lo e como ele funciona.

Objetivo do Projeto
O objetivo principal é criar uma API simples para interação com a OpenWeatherMap API, fornecendo previsões do tempo para uma cidade e armazenando essas informações em um banco de dados. A API permite aos usuários:

Consultar previsões do tempo para cidades.

Armazenar previsões no banco de dados.

Filtrar previsões por cidade e data.

Excluir previsões específicas.

A aplicação foi desenvolvida para ser fácil de configurar e rodar, utilizando Docker para garantir que todos os serviços necessários (aplicação, banco de dados e cache) sejam executados de forma isolada e sem conflitos.

Tecnologias Utilizadas
Este projeto utiliza as seguintes tecnologias:

FastAPI: Framework moderno e rápido para construir APIs com Python.

Uvicorn: Servidor ASGI que roda a aplicação FastAPI.

SQLAlchemy: ORM para facilitar a interação com o banco de dados PostgreSQL.

PostgreSQL: Banco de dados relacional utilizado para armazenar as previsões do tempo.

Redis: Sistema de cache e fila, embora atualmente não esteja sendo usado diretamente na aplicação, foi incluído para escalabilidade futura.

Docker: Para isolar o ambiente de desenvolvimento e garantir que o projeto seja executado de forma consistente em qualquer máquina.

Arquitetura do Projeto
Estrutura de Diretórios
bash
Copiar
Editar
/api_previsao_temperatura
│
├── /app
│   ├── /database.py          # Configuração da conexão com o banco de dados PostgreSQL.
│   ├── /main.py              # Implementação dos endpoints da API, onde as lógicas de negócios são executadas.
│   ├── /models.py            # Definição das models do banco de dados utilizando SQLAlchemy.
│   ├── /schemas.py           # Definição dos schemas Pydantic para validação de dados de entrada e saída.
│   ├── /service.py           # Lógica de interação com o banco de dados, incluindo CRUD (criar, ler, deletar).
│   ├── /weather_api.py       # Função que interage com a OpenWeatherMap API para obter previsões do tempo.
│   ├── /routes.py            # Definição das rotas da API.
├── /Dockerfile               # Definição do Dockerfile para construção do contêiner da aplicação.
├── /docker-compose.yml       # Arquivo para configuração de contêineres (App, Banco de Dados, Redis).
├── /requirements.txt         # Dependências do Python necessárias para rodar o projeto.
└── .env                      # Arquivo de variáveis de ambiente (exemplo de chave da API).
Descrição dos Arquivos
/app/database.py: Este arquivo configura a conexão com o banco de dados PostgreSQL, utilizando SQLAlchemy para facilitar a criação e gerenciamento de tabelas e consultas.

/app/main.py: Contém os endpoints da API. Aqui, a aplicação FastAPI recebe as requisições HTTP e executa as funções de negócios, como buscar previsões, armazenar no banco de dados e responder com os dados.

/app/models.py: Aqui, definimos as models do banco de dados, que são as representações das tabelas. Utilizamos o SQLAlchemy para mapear essas tabelas para o banco de dados PostgreSQL.

/app/schemas.py: Utilizamos o Pydantic para definir os schemas da API. Esses schemas servem para validar os dados que entram e saem da API (dados de requisição e resposta).

/app/service.py: Contém a lógica de negócios relacionada ao banco de dados. Este arquivo gerencia as operações CRUD (criação, leitura, atualização e exclusão) das previsões.

/app/weather_api.py: Aqui, está a lógica para interagir com a OpenWeatherMap API. Este arquivo contém funções que fazem as requisições à API externa e retornam as previsões do tempo para uma cidade.

/app/routes.py: Define as rotas da API (URLs). As rotas são mapeadas para funções específicas que realizam a interação com o banco de dados ou com a API externa.

Como Rodar o Projeto com Docker
Pré-requisitos
Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina. Caso não tenha, siga as instruções nos links abaixo para instalação:

Instalar Docker

Instalar Docker Compose

Passos para Executar
Clone o Repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/api-previsao-tempo.git
cd api-previsao-tempo
Crie o arquivo .env

Na raiz do projeto, crie um arquivo .env contendo as variáveis de ambiente necessárias. Exemplo:

env
Copiar
Editar
OPENWEATHER_API_KEY=SUA_CHAVE_AQUI
DATABASE_URL=postgresql://postgres:secret@db:5432/postgres
Aqui, OPENWEATHER_API_KEY deve ser a chave que você obteve da OpenWeatherMap, e DATABASE_URL contém a URL de conexão do banco de dados PostgreSQL.

Execute o Docker Compose

Com o Docker e o Docker Compose configurados, execute o seguinte comando para construir e iniciar os contêineres:

bash
Copiar
Editar
docker-compose up --build
Esse comando irá:

Construir a imagem da aplicação a partir do Dockerfile.

Iniciar o contêiner do PostgreSQL.

Iniciar o contêiner da aplicação FastAPI.

Iniciar o contêiner do Redis (embora não esteja sendo usado diretamente neste momento, pode ser útil para cache no futuro).

Após a execução, a API estará disponível em http://localhost:8000.

Acessando a Documentação da API

O FastAPI fornece uma documentação interativa da API automaticamente. Você pode acessá-la em:

Swagger: http://localhost:8000/docs

Redoc: http://localhost:8000/redoc

Por que Docker?
O Docker foi utilizado para garantir que a aplicação e todos os seus serviços necessários (como o banco de dados e Redis) sejam executados de forma isolada e com dependências consistentes, independentemente do sistema operacional da máquina. Isso facilita o processo de configuração e desenvolvimento, garantindo que o projeto funcione da mesma maneira em qualquer ambiente.

Com o Docker Compose, podemos configurar múltiplos contêineres (como o banco de dados, a aplicação e o Redis) e gerenciá-los de forma eficiente com apenas um comando.

Testando a API
Após rodar a aplicação, você pode usar ferramentas como o Postman ou o curl para testar os endpoints da API.

Exemplo de uso da API
Criar previsão (POST):

bash
Copiar
Editar
curl -X 'POST' \
  'http://localhost:8000/previsao/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "cidade": "São Paulo"
}'
Listar previsões (GET):

bash
Copiar
Editar
curl -X 'GET' \
  'http://localhost:8000/previsao/' \
  -H 'accept: application/json'
Excluir previsão (DELETE):

bash
Copiar
Editar
curl -X 'DELETE' \
  'http://localhost:8000/previsao/1' \
  -H 'accept: application/json'
Conclusão
Este projeto é um exemplo completo de uma API simples de previsão do tempo, utilizando as melhores práticas de desenvolvimento com FastAPI, PostgreSQL, Redis e Docker. O uso do Docker garante que o ambiente de desenvolvimento seja consistente e isolado, tornando o projeto mais fácil de configurar e executar, independentemente da máquina ou sistema operacional.