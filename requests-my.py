import requests
from requests import HTTPError
from getpass import getpass
from getpass import getuser

try:
    response = requests.get("https://github.com", auth=(getuser(), getpass()))
except HTTPError as http_err:
    print(f'Error : {http_err}')
except Exception as err:
    print(f'Unknown error: {err}')
else:
    print(f'Connected Successfully + {response.status_code}')

print(response.json())
