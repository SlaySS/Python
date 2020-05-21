import requests
from requests import HTTPError

try:
    response = requests.get("https://www.emb.ru")
except HTTPError as http_err:
    print(f'Error : {http_err}')
except Exception as err:
    print(f'Unknown error: {err}')
else:
    print(f'Connected Successfully + {response.status_code}')

print(response.text)