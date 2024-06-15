"""Maps plugin for generating maps from latlng coordinates."""
from typing import Any, Dict
from security import safe_requests


def call_api(input_json: Dict[str, Any]) -> Dict[str, Any]:
    query_param = input_json["latlng"]
    response = safe_requests.get(f"https://maps.smoothplugins.com/?latlng={query_param}")

    if response.status_code == 200:
        return {"result": response.content.decode()}
    else:
        return {"status_code": response.status_code, "text": response.text}
