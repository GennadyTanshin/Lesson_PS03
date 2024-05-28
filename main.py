import requests
from bs4 import BeautifulSoup
url =  "https://randomword.com/"

response = requests.get(url)
print(response.text)
