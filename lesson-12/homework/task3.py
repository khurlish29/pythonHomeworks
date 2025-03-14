import json
import requests
from bs4 import BeautifulSoup

url = "https://demoblaze.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

laptops = soup.find_all("div", class_="card")

laptop_data = []
for laptop in laptops:
    name = laptop.find("h4", class_="card-title").text.strip()
    price = laptop.find("h5").text.strip()
    description = laptop.find("p", class_="card-text").text.strip()
    
    laptop_data.append({"name": name, "price": price, "description": description})

with open("laptops.json", "w", encoding="utf-8") as file:
    json.dump(laptop_data, file, indent=4)

print("Laptop data scraped and saved to laptops.json.")
