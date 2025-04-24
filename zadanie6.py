import requests
from bs4 import BeautifulSoup
import webbrowser

def get_random_wikipedia_article():
    url = 'https://en.wikipedia.org/wiki/Special:Random'
    response = requests.get(url)
    final_url = response.url
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('h1').text
    print(f"Tytuł artykułu: {title}")
    user_input = input("Czy chcesz otworzyć ten artykuł? (tak/nie): ")
    if user_input.lower() == 'tak':
        webbrowser.open(final_url)


get_random_wikipedia_article()
