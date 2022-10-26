from bs4 import BeautifulSoup
import requests
# import lxml

#
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.a)
#
# response = requests.get("https://news.ycombinator.com/")
# yNewsPage = response.text
#
# soup = BeautifulSoup(yNewsPage, "html.parser")
# articleTag = soup.find(name="span", class_="titleline")
# articleText = articleTag.getText()
# articleLink = articleTag.get("a")
# articlePoints = soup.find(name="span", class_="score").getText()
# print(articleTag)
# print(articleText)
# print(articleLink)
# print(articlePoints)

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
websiteData = response.text

soup = BeautifulSoup(websiteData, "html.parser")
movies = soup.find_all(name="h3", class_="title")

moviesTitles = [movie.getText() for movie in movies]
moviess = moviesTitles[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as newFile:
    for movie in moviess:
        newFile.write(f"{movie}\n")
