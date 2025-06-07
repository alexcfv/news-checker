import os
import logging
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')

#INFO CRITICAL WARNING
logging_level = logging.INFO