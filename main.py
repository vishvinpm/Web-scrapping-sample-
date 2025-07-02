from water_purifier.scraper import DataScraper
from water_purifier.gpt_processing import GPTProcessing

def main() :
    url = "https://www.livemint.com/technology/gadgets/top-5-best-water-purifiers-in-india-2025-ideal-for-indian-homes-battling-hard-water-and-impurities-for-safe-drinking-11748061235456.html"
    print("Fetching data from the URL...")
    #creating an instance
    scraper = DataScraper(url)
    data = scraper.get_data()

    print("Data fetched successfully. Processing data with GPT...")
    #creating an instance for gpt
    gpt_processor = GPTProcessing()
    response = gpt_processor.process_data(data)


    #displaying the response in output.md
    with open("output.md", "w") as f :
        f.write("## The source file is :\n")
        f.write(f"URL: {url}\n\n")

        #writing the response from GPT
        f.write("## Response from GPT:\n")
        
        for i, product in enumerate(data, start = 1) :
            f.write(f"{i}. Name: {product['name']}, Price: {product['price']}, Link: {product['link']}\n")
        f.write("\n\n")
        f.write("### Summary:\n")
        f.write(response)

    print("Data processed successfully. Here is the response from GPT:")

if __name__ == "__main__" :
    main()