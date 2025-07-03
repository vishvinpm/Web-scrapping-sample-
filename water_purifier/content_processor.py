#importing the content(table_body) from thescraper
from water_purifier.scraper import DataScraper

class WebContentProcessor :
    def __init__(self, url) :
        self.url = url

        #creating instance of DataScraper
        self.data_scraper = DataScraper(self.url)
        self.table_body = self.data_scraper.get_data()

    def extract_content(self) :
        #extracting the required content form the table_body
        product_details = []

        for i in range(0, len(self.table_body), 2) :
            try :
                r1 = self.table_body[i]
                r2 = self.table_body[i + 1]

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
'''
if __name__ == "__main__":
    url = "https://www.livemint.com/technology/gadgets/top-5-best-water-purifiers-in-india-2025-ideal-for-indian-homes-battling-hard-water-and-impurities-for-safe-drinking-11748061235456.html"
    content_processor = WebContentProcessor(url)
    data = content_processor.extract_content()

    print(data)

'''