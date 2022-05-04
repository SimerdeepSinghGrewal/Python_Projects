import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(URL)
data = response.text
soup = BeautifulSoup(data, "html.parser")
movie_data = soup.find_all(name="h3", class_="title")
movies = [movie.get_text().replace(":", ")") for movie in movie_data]
movies.reverse()
with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
