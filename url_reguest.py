import sys
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# url = sys.argv[1]

# r = requests.get('https://api.github.com/events')
r = requests.get('https://insite.emb.bank/', verify=False)
# otvet = requests.get("http://insite/")
# print(otvet)
print(r.status_code)