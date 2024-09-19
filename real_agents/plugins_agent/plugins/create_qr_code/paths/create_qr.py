"""Create QR Code API."""
from typing import Any, Dict
from security import safe_requests


def call_api(input_json: Dict[str, Any]) -> Dict[str, Any]:
    url = "https://create-qr-code.modelxy.com/create-qr-code"
    response = safe_requests.get(url, params=input_json)
    if response.status_code == 200:
        return response.json()
    else:
        return {"status_code": response.status_code, "text": response.text}
