import requests

def request(url):
    try:
        return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
        pass

targetUrl ="turkcell.com.tr"

with open("subdomainlist.txt","r") as ListFile:
    for line in ListFile:
        word = line.strip()
        testUrl = word + "." + targetUrl
        response = request(testUrl)
        if response:
            print("Found subdomain --> " + testUrl)