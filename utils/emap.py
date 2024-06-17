import folium
import requests
from bs4 import BeautifulSoup


def single_map(user_location: str) -> None:
    url: str = f'https://pl.wikipedia.org/wiki/{user_location}'
    response = requests.get(url)
    response_html = BeautifulSoup(response.text, 'html.parser')
    latitude = response_html.select('.latitude')[1].text.replace(",", ".")
    longitude = response_html.select('.longitude')[1].text.replace(",", ".")
    map = folium.Map(location=[latitude, longitude], zoom_start=11)
    folium.Marker(location=[latitude, longitude], popup=f"{user_location} rządzi!!!").add_to(map)
    map.save(f'./{user_location}.html')

def full_map(users: str) -> None:
    lista_wspolrzednych = []
    map = folium.Map(location=[52, 21], zoom_start=8)
    for user in users:
        url: str = f'https://pl.wikipedia.org/wiki/{user["location"]}'
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        latitude = response_html.select('.latitude')[1].text.replace(",", ".")
        longitude = response_html.select('.longitude')[1].text.replace(",", ".")
        lista_wspolrzednych.append([latitude, longitude])
    for wspolrzedne in lista_wspolrzednych:
        folium.Marker(location=wspolrzedne).add_to(map)

    map.save(f'./common_map.html')

