from dotenv import load_dotenv
import os

load_dotenv()

try:
    HOST = os.environ.get('HOST')
    PORT = os.environ.get('PORT')
    USER = os.environ.get('USER')
    PASSWORD = os.environ.get('PASSWORD')
    DB_NAME = os.environ.get('DB_NAME')
except Exception as err:
    raise Exception(
        f'ERRO AO CARREGAR VARIÁVEIS DE AMBIENTE {err}'
    )
