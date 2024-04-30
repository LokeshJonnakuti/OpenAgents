"""Perform query to AskYourPDF API."""
from typing import Any, Dict
import requests


def call_api(input_json: Dict[str, Any]) -> Dict[str, Any]:
    response = requests.post("https://plugin.askyourpdf.com/query", json=input_json, timeout=60)

    if response.status_code == 200:
        return response.json()
    else:
        return {"status_code": response.status_code, "text": response.text}
