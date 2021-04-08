import re
import json
import cloudscraper

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
email = ""

def scrap_and_store(email):
	url = "https://haveibeenpwned.com/unifiedsearch/"+email
	scraper = cloudscraper.create_scraper()
	result = scraper.get(url)
	print("Info: Done Scrapping!")
	if(result.text!=""):
		data = json.loads(result.text)
		
		deleteKeys = ["AddedDate", "IsFabricated", "IsRetired", "IsSensitive", "IsSpamList", "IsVerified", "LogoPath", "ModifiedDate"]

		for i in range(len(data["Breaches"])):
			for key in deleteKeys:
				data["Breaches"][i].pop(key)

		return data
    
def haveibeenpwned(target):
	return scrap_and_store(target)