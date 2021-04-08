from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
from array import *

url = "https://iknowwhatyoudownload.com/en/peer/?ip="

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}


def ikwd(target):
    html_content = requests.get(url + target, headers=headers).content

    soup = BeautifulSoup(html_content, "lxml")

    gdp = soup.find_all("tr", attrs={"class": ""})

    downloads = []

    for table in gdp:
        currentTable = table
        body = currentTable.find_all("td")
        newDownload = []
        for td in body:
            newDownload.append((td.text).strip())

        downloads.append(newDownload)

    downloads.pop(0)
    return downloads

