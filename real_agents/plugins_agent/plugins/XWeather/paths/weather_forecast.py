"""Weather Forecast API Path."""
from typing import Dict, Any
from security import safe_requests


def call_api(input_json: Dict[str, Any]) -> Dict[str, Any]:
    location = input_json["location"]
    url = f"https://openai-plugin.xweather.com/weather/forecast/{location}"
    response = safe_requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return {"status_code": response.status_code, "text": response.text}
