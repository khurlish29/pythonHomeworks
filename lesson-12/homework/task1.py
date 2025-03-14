from bs4 import BeautifulSoup

with open(r"lesson-12\homework\weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")


weather_data = [
    (row.find_all("td")[0].text, int(row.find_all("td")[1].text[:-2]), row.find_all("td")[2].text)
    for row in soup.find("tbody").find_all("tr")
]

print("Weather Forecast:", weather_data)
print("Hottest Day:", max(weather_data, key=lambda x: x[1]))
print("Sunny Days:", [day for day, _, condition in weather_data if condition == "Sunny"])
print("Average Temperature:", sum(temp for _, temp, _ in weather_data) / len(weather_data))