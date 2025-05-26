import requests

API = "22545232ZVKKxOZxPiTOhMgvmfUGbBnvGaloq"


def get_account_cash():
    get_cash_url = "https://live.trading212.com/api/v0/equity/account/cash"
    headers = {"Authorization": API}
    cash = requests.get(get_cash_url, headers=headers)

    cash_data = cash.json()
    
    return cash_data

