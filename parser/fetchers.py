from bs4 import BeautifulSoup   
import requests
import json
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def connect_to_database():
    try:
        return psycopg2.connect(
            database=os.environ.get(""),
            user=os.environ.get(),
            password=os.environ.get(),
            host=os.environ.get(),
            port=os.environ.get()
        )
    except:
        raise Exception("couldn't login to the database, try again")
    

base_url="https://wiki.warthunder.com/"

def fetch_vechicles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    vechicles = list()
    table = soup.find(class_="wt-ulist_instance")
    if not table:
        table = soup.find(class_="favorite-units px-1 px-sm-0 mb-3").find_all("a")
    else:
        table = table.find_all("a")
    for x in table:
        vechicles.append(x["href"])
    get_basic_vechicle_data(vechicles[0])
    return vechicles    

def fetch_country_dict():
    url = base_url+"collections/operator"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    country_dict = []
    container = soup.find(class_="unit-collections px-3 px-sm-0 mb-3").find_all("a")

    for c in container:
        country_dict.append(base_url+c["href"])

    for x in country_dict:
        fetch_vechicles(x)

"""
unit -> general and unit specific data

"""
def function_name_to_be_edited(soup):
    return (
        soup.find(id = "general"),
        soup.find(class_ = "game-unit_content")
    )

def get_basic_vechicle_data(url):
    url = base_url + url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    vechile_type = soup.find(class_ = "game-unit_nation")
    print(vechile_type.text.strip())
    
    if not vechile_type:
        print("something went wrong")
        return

    general, unit_content = function_name_to_be_edited(soup)

    match (vechile_type.text.strip().lower()):
        case "ground vehicles":
            get_ground(general, unit_content)
        case "aviation":
            get_aviation(soup)
        case "helicopters":
            get_helicopters(soup)
        case "bluewater fleet":
            get_bluewater_fleet(soup)
        case "coastal fleet":
            get_coastal_fleet(soup)
        case _:
            print("Error with the game unit nation div")

def get_ground(general, unit_content):
    # main_div = soup.find(id = "general")
    type = "ground"
    vehicle_name = general.find(class_ = "game-unit_name")
    rank = general.find(class_ = "game-unit_card-info_value").text.strip()
    test = general.find_all(class_ = "game-unit_br-item")
    brs = dict()
    for x in test:
        pass
    print(vehicle_name.text.strip())
    


def get_aviation(soup):
    pass

def get_helicopters(soup):
    pass

def get_bluewater_fleet(soup):
    pass

def get_coastal_fleet(soup):
    pass

# def fetch_vehicle_dict(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     vehicle_dict = {}
#     for row in soup.find_all("tr"):
#         data = row.find("a") 
#         if data is not None:
#             vehicle_dict[data.text] = base_url+data.get("href")
#     # fallback for countries with less vehicles
#     if not vehicle_dict:
#         for data in soup.find(id="collectionList").find_all("a"):
#             if data.find("span") is not None:
#                 vehicle_dict[data.find("span").text] = data.get("href")
#     return vehicle_dict

# def fetch_stat(unit):
#     stat_dict = {}
#     if unit.find(class_="game-unit_chars-subline"):
#         line = unit.find(class_="game-unit_chars-line").extract().text
#         previous_key = "foo"
#         for subline in unit.find_all(class_="game-unit_chars-subline")+unit.find_all(class_="game-unit_chars-line"):
#             spans = [span.text.strip() for span in subline.find_all("span")]
#             if len(spans) == 1:
#                 stat_dict[previous_key] = stat_dict[previous_key] + spans[0]
#             else:
#                 stat_dict.update({spans[0]:spans[1]})
#             previous_key = spans[0]
#     return stat_dict



        
        
        



# def fetch_vehicle_data(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     vehicle_data = {"specification":{},"weapon":{},"economy":{}}

#     for category in vehicle_data:
#         for block in soup.find_all(class_="block mb-3"):
#             header = block.find(class_="block-header")
#             vehicle_data[category].update(fetch_stat(block))

    



#     with open("op.txt", 'w') as f:
#         f.write(json.dumps(vehicle_data, indent=4))

            
                            




                     
                    
                         


#                 #chars_line = block.find(class_="game-unit_chars-line")
#                 #if chars_line is not None:
#                 #    vehicle_data[category][chars_line] = block.find(class_="game-unit_chars-subline").text
#                 #else:

            

                


                
            
            

                    
                    

# print(fetch_vehicle_data("https://wiki.warthunder.com/unit/uk_cruiser_leander"))