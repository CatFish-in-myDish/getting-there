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

def fetch_vehicle_dict(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    vehicle_dict = {}
    for row in soup.find_all("tr"):
        data = row.find("a") 
        if data is not None:
            vehicle_dict[data.text] = base_url+data.get("href")
    # fallback for countries with less vehicles
    if not vehicle_dict:
        for data in soup.find(id="collectionList").find_all("a"):
            if data.find("span") is not None:
                vehicle_dict[data.find("span").text] = data.get("href")
    return vehicle_dict

def fetch_vehicle_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    vehicle_data = {"specification":{},"weapon":{},"economy":{}}

    for category in vehicle_data:
        for column in soup.find(id=category).find_all(class_="game-unit_chars-block"):
            for row in column.find_all("div"):
                stat_name = row.find("span")
                if stat_name is None:
                    continue
                stat_name = stat_name.text
                for stat_container in row.find_all(class_="=game-unit_chars-subline"):
                    stat = stat_container.find_all("span")
                    vehicle_data[category][stat_name] = {stat[0].text:stat[1].text}

                    
                    

print(fetch_vehicle_data("https://wiki.warthunder.com/unit/uk_cruiser_leander"))