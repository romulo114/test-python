import os

APP_TITLE='Invoice app'
APP_DESC='Test project for Estridge'
API_VERSION='v1'

DEBUG = os.environ.get('DEBUG', True)

POSTGRES_USER = os.environ.get('POSTGRES_USER', '')
POSTGRES_PASS = os.environ.get('POSTGRES_PASSWORD', '')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'postgres')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432)
POSTGRES_DB = os.environ.get('POSTGRES_DB', '')
POSTGRES_DB_URL = f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
