from googlesearch import search
from bs4 import BeautifulSoup   
import requests

class GoogleScraper :
    def __init__(self, query) :
        self.query = query
        self.Headers = {"User-Agent":
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"}
        self.top_url = None
        self.page_content = ""

    def get_top_url(self) :

        #searching for query in google
        search_results = search(self.query, num_results = 1)  #gets the top result
        if search_results:
            self.top_url = search_results[0]
            print(f"Top URL found: {self.top_url}")
        else:
            print("No results found for the query.")
            return None
        return self.top_url
    
    #getting the content of page
    def page_content(self) :
        if not self.top_url:
            print("No URL found. Please run get_top_url() first.")
            return None
        
        #fetching the page
        response = requests.get(self.top_url, headers = self.Headers)
        soup = BeautifulSoup(response.content, "html.parser")
        #getting the content of the page
        self.page_content = soup.get_text(strip = True)
        print("Page content fetched successfully.")

        return self.page_content

    #getting the content of the page
    def get_page_content(self) :
        if not self.page_content:
            print("No page content found. Please run page_content() first.")
            return None
        
        return self.page_content