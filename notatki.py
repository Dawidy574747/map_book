import requests
from bs4 import BeautifulSoup


def get_cordinates(miejscowosc:str) -> list[float,float]:
    url:str=f"https://en.wikipedia.org/wiki/{miejscowosc}"
    response = requests.get(url)
    response_html=BeautifulSoup(response.text,"html.parser")
    latitude= float(response_html.select(".latitude")[1].text.replace(",",""))
    longitude= float(response_html.select(".longitude")[1].text.replace(",",""))
    return [latitude,longitude]


miejscowosc=input("Podaj miejscowosc: ")



print(get_cordinates(miejscowosc))
