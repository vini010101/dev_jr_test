from dotenv import load_dotenv
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Carregar variáveis de ambiente
load_dotenv()

# Obter a URL do banco de dados a partir das variáveis de ambiente
database_url = os.getenv('DATABASE_URL')

# Alembic Config object
config = context.config

# Substituir a URL de banco de dados no config se ela existir
if database_url:
    config.set_main_option('sqlalchemy.url', database_url)

# Interpretar o arquivo de configuração para logs (não altere)
fileConfig(config.config_file_name)

# Importar o Base (onde os modelos são definidos) e as tabelas do seu projeto
from whater_api.app.models import Base 

# Informar ao Alembic quais são os modelos/tabelas que ele deve acompanhar
target_metadata = Base.metadata

