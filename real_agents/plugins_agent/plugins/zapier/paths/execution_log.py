"""Execution log path for Zapier plugin."""
from typing import Any, Dict
from security import safe_requests


def call_api(input_json: Dict[str, Any], api_key) -> Dict[str, Any]:
    headers = {
        "X-API-Key": api_key,
    }
    url = "https://nla.zapier.com/api/v1/" + input_json['execution-log']
    response = safe_requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"status_code": response.status_code, "text": response.text}
