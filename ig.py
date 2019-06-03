import requests
import re
from bs4 import BeautifulSoup

url = "https://instagram.com/" + input("Instagram User: ")
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
check = soup.find_all(text=re.compile('"is_private":true'))

isprivate = None

if len(check) != 0:
    isprivate = True
else:
    isprivate = False


if isprivate is True:
    print("Oh no, account is private!")
else:
    print("Hurray! Account is not private!")
