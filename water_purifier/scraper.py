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
        
        #getting the body with all details
        table_body = self.soup.select("tbody > tr")

        return table_body
    
 

'''        return product_details
if __name__ == "__main__":
    url = "https://www.livemint.com/technology/gadgets/top-5-best-water-purifiers-in-india-2025-ideal-for-indian-homes-battling-hard-water-and-impurities-for-safe-drinking-11748061235456.html"
    scraper = DataScraper(url)
    data = scraper.get_data()
    print(data)
'''
'''
        #initializing the data list including the products
        product_details = []

        for row in table_body:
            #name
            name_tag = row.select_one("div.product-des-box strong")
            name = name_tag.get_text(strip=True) if name_tag else "No result"

            #price
            price_tag = row.select_one("p.product-new-pricing")
            price = price_tag.get_text(strip=True) if price_tag else "No result"

            #link
            link_tag = row.select_one("div.product-buy-btn a")
            link = link_tag["href"] if link_tag else "No result"

            product_details.append({"name": name,
                                    "price": price,
                                    "amazon link": link})

        return product_details


if __name__ == "__main__":
    url = "https://www.livemint.com/technology/gadgets/top-5-best-water-purifiers-in-india-2025-ideal-for-indian-homes-battling-hard-water-and-impurities-for-safe-drinking-11748061235456.html"
    scraper = DataScraper(url)
    data = scraper.get_data()

    # Print the first 5 products
    for i, product in enumerate(data[:5], start=1):
        print(f"{i}. {product['name']} | {product['price']} | {product['amazon link']}")
    
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
        
        #iterating through the table body to get the data
        for i in range(0, len(table_body), 2) :
            try :
                r1 = table_body[i]
                r2 = table_body[i + 1]

                #name with details
                name_tag = r1.select_one("div.product-des-box strong")
                name = name_tag.get_text(strip = True) if name_tag else "No result"

                #price
                price_tag = r1.select_one("p.product-new-pricing")
                price = price_tag.get_text(strip = True) if price_tag else "No result"

                #link
                link_tag = r2.select_one("div.product-buy-btn a")
                link = link_tag["href"] if link_tag else "No result"

                product_details.append({"name" : name,
                        "price" : price,
                        "amazon link" : link})
                
            except Exception as e:
                print(f"Error at row {i}: {e}")

        return product_details


if __name__ == "__main__":
    url = "https://www.livemint.com/technology/gadgets/top-5-best-water-purifiers-in-india-2025-ideal-for-indian-homes-battling-hard-water-and-impurities-for-safe-drinking-11748061235456.html"
    scraper = DataScraper(url)
    data = scraper.get_data()
    
    # Print the first 5 products
    for i, product in enumerate(data[:5], start=1):
        print(f"{i}. {product['name']} | {product['price']} | {product['amazon link']}")
 '''