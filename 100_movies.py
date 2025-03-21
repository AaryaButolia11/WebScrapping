import requests
from bs4 import BeautifulSoup

# URL of the archived page
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Fetch the page
response = requests.get(URL)
website_html = response.text

# Parse HTML
soup = BeautifulSoup(website_html, "html.parser")

# Find all movie titles (Check class name in case it changes)
all_movies = soup.find_all(name="h3")

# Extract text from movie titles
movies_titles = [movie.getText() for movie in all_movies]

# Reverse the order to match correct ranking
movies = movies_titles[::-1]

# Print movie titles
for movie in movies:
    print(movie)

# Write to a file
with open(r"C:\Users\YourUsername\Desktop\movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")


print(len(movies))  # Should print 100
