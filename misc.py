import requests
from bs4 import BeautifulSoup as bs

API = "KEY_HERE"

incomeshares_data = [
    {
        "ticker": "QQQY",
        "name": "IncomeShares Nasdaq 100 Options ETP",
        "url": "https://incomeshares.com/en/etps/income-shares-nasdaq-100-options-etp",
    },
    {
        "ticker": "DSPY",
        "name": "IncomeShares S&P500 Options ETP",
        "url": "https://incomeshares.com/en/etps/income-shares-s-p-500-options-etp",
    },
    {
        "ticker": "TSLI",
        "name": "IncomeShares Tesla Options ETP",
        "url": "https://incomeshares.com/en/etps/income-shares-tesla-options-etp",
    },
    {
        "ticker": "COIY",
        "name": "IncomeShares Coinbase Options ETP",
        "url": "https://incomeshares.com/en/etps/income-shares-coinbase-options-etp",
    },
    {
        "ticker": "ONVD",
        "name": "IncomeShares NVIDIA",
        "url": "https://incomeshares.com/en/etps/income-shares-nvidia-options-etp",
    },
]

def get_account_cash():
    get_cash_url = "https://live.trading212.com/api/v0/equity/account/cash"
    headers = {"Authorization": API}
    cash = requests.get(get_cash_url, headers=headers)

    cash_data = cash.json()
    
    return cash_data

def request_data(ticker):
    _url = None
    title = None
    for item in incomeshares_data:
        if item["ticker"] == ticker:
            _url = item["url"]
            title = item["name"]
            break

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(_url, headers=headers)

    soup = bs(response.text, "html.parser")

    nav_section = soup.find(id="net-asset-value")

    if nav_section:
        dt = nav_section.find_all("dt")
        dd = nav_section.find_all("dd")

        if len(dt) == len(dd):
            for dt, dd in zip(dt, dd):
                return dt.get_text(strip=True), dd.get_text(strip=True), title
                break
    else:
        return None

