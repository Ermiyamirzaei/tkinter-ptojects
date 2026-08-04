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

def translate_text(text:str, source:str="auto", target:str="fa", engin:str="google"):
    if not text or not text.strip():
        raise TranslationError("NO txt was provided to translate.")
    if engin not in ("google", "microsoft", "yandex"):
        raise TranslationError(f"invalid transations engin {engin}":)

    url = f"{BASE_URL}/{engin}/"

    payload = {
        "source": "" if source == "auto"else source,
        "target":target,
        "text": text,
    }


    try:
        response = requests.post(url, json=payload, headers=_headers(), timeout=15)
    except requests.exceptions.ConnectionError:
        raise TranslationError("Colud not connect the server.")
    except requests.exceptions.Timeout:
        raise TranslationError("The requset time out.")
    except requests.exceptions.RequestException as e:
        raise TranslationError(f"Unexpected requst error: {e}")


    if response.status_code == 200:
        data = response.json()
        result = data.get("result")
        if result is None:
            raise TranslationError("server does not response")
        return result

    try:
        message = response.json().get("message", "")
    except ValueError:
        message = ""

    status_message = {
        400:"Reqired parameters are mising",
        401: "Invalid Api token.",
        402: "the request failed on the server side",
        403: "Insufficient account credit for the request",
        404: "Dta not found",
        409: " The request violates the services rules",
        429: "Too many request. please wait a momment",

    }

    base_messeage = status_message.get(
        response.status_code,
        f"server error (status codr {response.status_code})"
    )

    full_message = f"{base_messeage} {message}".strip()
    raise TranslationError(full_message)