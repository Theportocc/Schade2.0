import requests
from bs4 import BeautifulSoup

url = "https://www.schadeautos.nl/nl/zoek/schade/personenautos/1/1/0/0/0/0/1/0"

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

cars = soup.find_all("div", class_="row car")

for car in cars:
    price = car.find("div", class_="price").text.strip()
    brand = car.find("div", class_="brand").text.strip()
    model = car.find("div", class_="model").text.strip()

    print("Prijs:", price)
    print("Merk:", brand)
    print("Model:", model)
    print("------")

soup = BeautifulSoup(html_content, "html.parser")

cars = soup.find_all("div", class_="row car")

car_list = []

for car in cars:
    price = car.find("div", class_="price").text.strip()
    brand = car.find("div", class_="brand").text.strip()
    model = car.find("div", class_="model").text.strip()

    car_info = {
        "Prijs": price,
        "Merk": brand,
        "Model": model
    }

    car_list.append(car_info)

# Toon de resultaten
for car in car_list:
    print("Prijs:", car["Prijs"])
    print("Merk:", car["Merk"])
    print("Model:", car["Model"])
    print("------")
