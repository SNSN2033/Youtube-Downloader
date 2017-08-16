# import requests
# from bs4 import BeautifulSoup
#
# request = requests.get("https://www.youtube.com/results?search_query=harry+potter")
# content = request.content
# soup = BeautifulSoup(content, "html.parser")
# all_item = {}
# i = 0
#
# for element in soup.find_all('a', {"rel": "spf-prefetch"}):
#     video_title = element.get('title')
#     video_link = element.get('href')
#     img_value = element.get('href').split("=")[1]
#     img = "https://i.ytimg.com/vi/{}/hqdefault.jpg".format(img_value)
#     all_item['{}'.format(i)] = {"title": video_title, "link": "https://www.youtube.com{}".format(video_link),
#                                     'img': img}
#     print(all_item['{}'.format(i)])
#     i += 1
# print("The total number of videos is:", i)
# i = 0
# for time in soup.find_all('span', {"class": "video-time"}):
#      print(time.text)
#      i += 1
# print("The total number of time indexes is:", i)

import requests
import pafy
from bs4 import BeautifulSoup

url = "https://www.youtube.com/results?search_query=harry+potter"
request = requests.get(url)
content = request.content
soup = BeautifulSoup(content, "html.parser")

for all_mv in soup.select(".yt-lockup-video"):
    # 抓取title & link
    data = all_mv.select("a[rel='spf-prefetch']")
    print("名稱: {}".format(data[0].get("title")))
    link = "https://www.youtube.com{}".format(data[0].get("href"))
    print("連結: ", link)

    # 抓取时间
    video = pafy.new(link)
    video_seconds = video.length
    video_time = str(int(video_seconds / 60)) + ":"
    if video_seconds%60 < 10:
        video_time += "0" + str(video_seconds%60)
    else:
        video_time += str(video_seconds%60)
    print(video_time)


    # 抓取IMG
    img = all_mv.select("img")
    if img[0].get("src") != "/yts/img/pixel-vfl3z5WfW.gif":
        print("照片: {}".format(img[0].get("src")))
    else:
        print("照片: {}".format(img[0].get("data-thumb")))
    print("-------------------")