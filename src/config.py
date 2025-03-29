import os
from dotenv import load_dotenv

load_dotenv()

TWELVEDATA_API_KEY = os.getenv('TWELVEDATA_API_KEY')

if not TWELVEDATA_API_KEY:
    raise ValueError("TWELVEDATA_API_KEY не найден в .env файле")