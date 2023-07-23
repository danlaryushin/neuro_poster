import os

import dotenv

dotenv.load_dotenv('.env')

API_KEY = os.getenv('API_KEY')
MAIN_URL = os.getenv('MAIN_URL')
PARSE_URL = os.getenv('PARSE_URL')
SECTIONS = os.getenv('SECTIONS')
TG_TOKEN = os.getenv('TG_TOKEN')
CHAT_ID = [os.getenv('CHAT_ID')]
