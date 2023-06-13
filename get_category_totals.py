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

def get_children(term):
    facets = []
    for child_term in term["term"]:
        facets += get_term(child_term)
    return facets

def get_term(term):
    facets = []
    facets.append({"format": term["search"], "total": int(term["count"])})
    if "term" in term:
        facets += get_children(term)
    return facets

def get_formats(category):
    facets = []
    try:
        for term in category["facets"]["facet"][0]["term"]:
            facets += get_term(term)
    except (KeyError, TypeError):
        return []
    formats = [dict(f, **{"category_name": category["name"], "category_code": category["code"]}) for f in facets]
    return formats

def get_category_totals():
    params = {
        "q": " ",
        "category": "all",
        "encoding": "json",
        "n": 0,
        "key": API_KEY,
        "facet": "format"
    }
    totals = []
    formats = []
    response = s.get("https://api.trove.nla.gov.au/v3/result", params=params)
    data = response.json()
    for category in data["category"]:
        totals.append({"category_name": category["name"], "category_code": category["code"], "total": int(category["records"]["total"])})
        formats += get_formats(category)
    return totals, formats

def main():
    Path("data").mkdir(exist_ok=True)
    totals, formats = get_category_totals()
    df_totals = pd.DataFrame(totals)
    df_totals.to_csv(Path("data", "trove-category-totals.csv"), index=False)
    df_formats = pd.DataFrame(formats)
    df_formats[["category_name", "category_code", "format", "total"]].to_csv(Path("data", "trove-category-formats.csv"), index=False)

if __name__ == "__main__":
    main()