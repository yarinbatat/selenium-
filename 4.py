import requests
from requests.exceptions import InvalidURL

try:
    response = requests.get("https://github.com")
    print(response)
    print(response.status_code)
except InvalidURL:
    print("invalid url was given")