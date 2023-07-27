import os

import dotenv

dotenv.load_dotenv('.env')

RETRY_TIME = 60
DT_FORMAT = '%I:%M%p on %B %d, %Y'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_FILE = 'main.log'
API_KEY = os.getenv('API_KEY')
MAIN_URL = os.getenv('MAIN_URL')
PARSE_URL = os.getenv('PARSE_URL')
SECTIONS = os.getenv('SECTIONS').split(', ')
TG_TOKEN = os.getenv('TG_TOKEN')
CHAT_ID = [os.getenv('CHAT_ID')]
