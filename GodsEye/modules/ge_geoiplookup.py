import requests
import re
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': "application/json"
}


def geoipLookup(target):
    request = requests.get(f"https://whatismyipaddress.com/ip/" + target, headers=headers)

    soup = BeautifulSoup(request.text, 'html.parser')

    info = soup.findAll("p", {"class": "information"})

    result = ""
    for i in info:
        _i = str(i)
        result += re.sub('<.*?>', '', _i) + "\n"

    return result