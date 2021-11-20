from tda import auth, client
import json
from selenium import webdriver

token_path = '/path/to/token.json'
api_key = '@AMER.OAUTHAP'
redirect_uri = 'http://localhost'
try:
    c = auth.client_from_token_file(token_path, api_key)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome(executable_path=r'C:\Users\\PycharmProjects\pythonProject\chromedriver.exe') as driver:
        c = auth.client_from_login_flow(
            driver, api_key, redirect_uri, token_path)

#    period_type=client.Client.PriceHistory.PeriodType.YEAR,
#        period=client.Client.PriceHistory.Period.TWENTY_YEARS,
#        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
#        frequency=client.Client.PriceHistory.Frequency.DAILY)
#assert r.status_code == 200, r.raise_for_status()
#print(json.dumps(r.json(), indent=4))

response = c.get_transactions(270482391)
response = c.get_watchlists_for_single_account(270482391)

with open('transactions.txt', 'w') as json_file:
    json.dump(response.json(), json_file, indent=4)