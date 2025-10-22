import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv('BASE_URL')
FAKE_TOKEN = os.getenv('FAKE_TOKEN')
BASE_HEADERS = os.getenv('BASE_HEADERS')