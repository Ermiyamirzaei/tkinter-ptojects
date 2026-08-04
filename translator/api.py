import os
import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = "https://api.one-api.ir/translate/v1"
API_TOKEN = os.getenv("ONE_API_TOKEN") 

class TranslationError(Exception):
    pass

def _headers():
    if not API_TOKEN or API_TOKEN == "your_token_here":
        raise TranslationError(
            "API token is not set! Please set ONE_API_TOKEN in the .env file"
        )
    return{
        "one-api-token": API_TOKEN,
        "Contetnt-Type": "application/json",
    }

def translate_text():
    ...