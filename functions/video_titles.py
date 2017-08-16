import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.youtube.com/results?search_query=civilization+6+trailer")
content = request.content
soup = BeautifulSoup(content, "html.parser")
for element in soup.find_all('a', {"rel": "spf-prefetch"}):
    video_title = element.get('title')
    print(video_title)