import sys
import requests


# r = requests.get('https://api.github.com/events')
r = requests.get('https://repo.spring.io/', verify=True)
# otvet = requests.get("http://insite/")
# print(otvet)
print(r.text)