from __future__ import unicode_literals
import requests
from bs4 import BeautifulSoup
import youtube_dl
import pafy


def find_search_content(search):
    request = requests.get("https://www.youtube.com/results?search_query={}".format(search))
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    return soup


def find_page_content(search):
    request = requests.get("https://www.youtube.com/results?{}".format(search))
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    return soup


def find_video(soup):
    all_item = {}
    i = 1
    for element in soup.find_all('a', {"rel": "spf-prefetch"}):
        video_title = element.get('title')
        video_link = element.get('href')
        img_value = element.get('href').split("=")[1]
        img = "https://i.ytimg.com/vi/{}/hqdefault.jpg".format(img_value)
        all_item['{}'.format(i)] = {"title": video_title, "link": "https://www.youtube.com{}".format(video_link), "img": img}
        i += 1
    return all_item


def page_bar(soup):
    page = {}
    for page_value in soup.find_all('a', {"class": True, "data-visibility-tracking": True, "data-sessionlink": True,
                                          "aria-label": True}):
        page[page_value.text] = page_value.get('href')
    return page


def download_mp3(url):
    ydl_opts = {'format': 'bestaudio/best',
                "nocheckcertificate": True,
                "outtmpl": "video/%(title)s.%(ext)s",
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_mp4(url):
    ydl_opts = {'format': 'best',
                "nocheckcertificate": True,
                "outtmpl": "video/%(title)s.%(ext)s"}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
