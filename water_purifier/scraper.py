import pandas as pd
from bs4 import BeautifulSoup
import requests

class DataScraper :
    def __init__(self, url) :
        self.url = url
        self.Headers = {"User-Agent":
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"}
        
    def get_data(self) :
        #fetching the page
        self.page = requests.get(self.url, headers = self.Headers)
        #parsing the page
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        
        #initializing the data list including the products
        products = []

        for item in self.soup.find_all("div", class_ = "product-item"):
            #extracting name, price and link
            #name
            name_tag = item.find("h2", class_ = "product-title") 
            name = name_tag.get_text(strip = True) if name_tag else "No result"
            #price
            price_tag = item.find("p", class_ = "product-price")
            price = price_tag.get_text(strip = True) if price_tag else "No result"
            #link
            link_tag = item.find("a", class_ = "product-link")
            link = link_tag['href'] if link_tag else "No result"

            #appending the data to the products list
            products.append({
                "name": name,
                "price": price,
                "link": link
            })

        return products