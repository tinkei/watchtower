import json
import os
from pathlib import Path
from pprint import pprint
from typing import Optional

import requests
from dotenv import load_dotenv

load_dotenv()

# DISCOS API base URL and API key.
BASE_URL = "https://discosweb.esoc.esa.int"
API_TOKEN = os.getenv("DISCOS_API_KEY", None)

# Define headers for authentication.
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
    "DiscosWeb-Api-Version": "2",
}


# Example query: Fetch data for a specific satellite (by COSPAR ID or NORAD ID)
def fetch_one(id: int) -> Optional[dict]:
    query_url = f"{BASE_URL}/api/objects/{id}"

    # Send GET request
    response = requests.get(query_url, headers=HEADERS)

    # Check response.
    if response.ok and response.status_code == 200:
        satellite_data = response.json()  # Parsed JSON data
        print("Satellite Data:")
        print(json.dumps(satellite_data, indent=4))
        return satellite_data
    elif response.status_code == 429:
        print("Error rate limit reached:", response.status_code, response.text)
        return None
    else:
        print("Error:", response.status_code, response.text)
        return None


def fetch_many() -> Optional[list[dict]]:
    query_url = f"{BASE_URL}/api/objects"
    params = {
        "filter": "eq(objectClass,Payload)&gt(reentry.epoch,epoch:'2020-01-01')",
        "sort": "-reentry.epoch",
    }
    response = requests.get(query_url, headers=HEADERS, params=params)

    satellite_data = response.json()
    if response.ok:
        print("Satellite Data:")
        print(json.dumps(satellite_data, indent=4))
        return satellite_data
    else:
        pprint(satellite_data["errors"])
        return None


if __name__ == "__main__":
    norad_id = 25544  # Example: ISS
    satellite_data = fetch_one(id=norad_id)

    data_path = Path("./data")
    data_path.mkdir(parents=True, exist_ok=True)
    with open(data_path / f"result_{norad_id}.json", "w") as fp:
        json.dump(satellite_data, fp, indent=4)
