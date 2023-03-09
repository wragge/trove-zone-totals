import os
from pathlib import Path

import pandas as pd  # makes manipulating the data easier
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from dotenv import load_dotenv

load_dotenv()

# Create a session that will automatically retry on server errors
s = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
s.mount("http://", HTTPAdapter(max_retries=retries))
s.mount("https://", HTTPAdapter(max_retries=retries))

API_KEY = os.getenv("TROVE_API_KEY")

def get_zone_totals():
    params = {
        "q": " ",
        "zone": "all",
        "encoding": "json",
        "n": 0,
        "key": API_KEY
    }
    totals = []
    response = s.get("https://api.trove.nla.gov.au/v2/result", params=params)
    data = response.json()
    for zone in data["response"]["zone"]:
        if zone["name"] != "url":
            totals.append({"zone": zone["name"], "total": int(zone["records"]["total"])})
    return totals

def main():
    Path("data").mkdir(exist_ok=True)
    totals = get_zone_totals()
    df = pd.DataFrame(totals)
    df.to_csv(Path("data", "trove-zone-totals.csv"), index=False)

if __name__ == "__main__":
    main()