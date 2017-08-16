import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.youtube.com/results?search_query=civilization+6+trailer")
content = request.content
soup = BeautifulSoup(content, "html.parser")
print(soup)