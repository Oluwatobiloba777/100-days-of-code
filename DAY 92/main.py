from bs4 import BeautifulSoup
import requests

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
