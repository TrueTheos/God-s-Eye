import json
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

def check(target):
    print(target)
    result = requests.get(f"https://disposable.debounce.io?email={target}", headers=headers)
    parsedResult = json.loads(result.text)

    result2 = requests.get(f"https://api.trumail.io/v2/lookups/json?email={target}", headers=headers)
    parsedResult2 = json.loads(result2.text)
    
    disposableState = []

    if parsedResult["disposable"] == "false":
        disposableState.append(False)
    else:
        disposableState.append(True)

    if parsedResult2["disposable"]:
        disposableState.append(True)
    else:
        disposableState.append(False)

    return(disposableState)