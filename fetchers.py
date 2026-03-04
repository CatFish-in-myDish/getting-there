from bs4 import BeautifulSoup
import requests

base_url="https://wiki.warthunder.com/"


def fetch_country_dict():
    url = base_url+"collections/operator"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    country_dict = {}
    for container in soup.find(class_="unit-collections px-3 px-sm-0 mb-3").find_all("a"):
        country_name = container.find(class_="unit-collection-card_title").text
        country_link = container.get("href")
        country_dict[country_name] = base_url+country_link
    return country_dict

def fetch_vehicle_dict(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    vehicle_dict = {}
    for row in soup.find_all("tr"):
        data = row.find("a") 
        if data is not None:
            vehicle_dict[data.text] = base_url+data.get("href")
    return vehicle_dict