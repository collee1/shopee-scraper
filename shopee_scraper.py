import requests
from bs4 import BeautifulSoup
import csv

url = "https://shopee.co.id/search?keyword=kaos%20pria"
headers = {
    "User-Agent": "Mozilla/5.0",
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

items = soup.find_all("div", class_="shopee-search-item-result__item")

with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Judul", "Harga", "Link"])

    for item in items:
        try:
            title = item.find("div", class_="ie3A+n bM+7UW Cve6sh").text
            price = item.find("span", class_="ZEgDH9").text
            link = "https://shopee.co.id" + item.find("a")["href"]
            writer.writerow([title, price, link])
        except:
            continue

print("✅ Data berhasil disimpan ke output.csv")
