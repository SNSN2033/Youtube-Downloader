import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.youtube.com/results?search_query=steins+gate")
content = request.content
soup = BeautifulSoup(content, "html.parser")
for element in soup.find_all('a',{"rel":"spf-prefetch"}):
    video_title = element.get('title')
    video_link = element.get('href')
    print(video_title)
    print("https://www.youtube.com{}".format(video_link))
    print(type(video_link))
    if "https://googleads" in video_link:
        continue