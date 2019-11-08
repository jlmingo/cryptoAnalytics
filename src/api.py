from dotenv import load_dotenv
import os
load_dotenv()
import requests

def usFundRequestAuthorized(resource):
    authToken = os.getenv("usFundTokenApi")
    if not authToken:
        raise ValueError("You need a token")
    else:
        print("We have a usFund token {}".format(authToken[0:4]))
    url = "https://api.usfundamentals.com{}&token=".format(resource)
    print("Requesting authorized {}".format(url))
    print(url+authToken)
    res = requests.get(url+authToken)
    return res