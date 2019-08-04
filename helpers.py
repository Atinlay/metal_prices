import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
import platform


def soup_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def get_metals_and_prices_from_table(metal_table):
    metals_and_prices = metal_table.find_all("td", {"class": ["indx_7", "indx_1"]})
    metals = [metal.get("class")[1].split("_")[1] for metal in metals_and_prices[0:][::2]]
    prices = [float(price.text.strip()) for price in metals_and_prices[1:][::2]]
    return metals, prices

def get_database_engine():
    if platform.system() == "Windows":
        engine = create_engine('mysql://remote:Albatross19B(@192.168.1.35:3306/projects')
    elif platform.system() == "Linux":
        engine = create_engine("mysql://remote:Albatross19B(@localhost:3306/projects")
    else:
        raise ConnectionError
    return engine