"""Radars API path."""
from typing import Any, Dict
from security import safe_requests


def call_api(input_json: Dict[str, Any]) -> Dict[str, Any]:
    location = input_json['location']
    response = safe_requests.get(f"https://openai-plugin.xweather.com/radar/{location}", params=input_json)

    if response.status_code == 200:
        return response.json()
    else:
        return {"status_code": response.status_code, "text": response.text}
