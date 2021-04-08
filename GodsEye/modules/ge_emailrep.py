import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': "application/json"
}

def emailrep(target):
    result = requests.get(f"https://emailrep.io/" + target, headers=headers)

    return result.text