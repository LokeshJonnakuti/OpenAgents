"""Show Carousel path for Show Me plugin."""
from typing import Any, Dict
from security import safe_requests


def call_api(input_json: Dict[str, Any]) -> Dict[str, Any]:
    response = safe_requests.get("https://showme.redstarplugin.com/show-carousel", params=input_json)

    if response.status_code == 200:
        return response.json()
    else:
        return {"status_code": response.status_code, "text": response.text}
