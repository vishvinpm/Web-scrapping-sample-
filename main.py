import pandas as pd
from water_purifier.scraper import DataScraper
# from water_purifier.gpt_processing import GPTProcessing

def main():
    '''
    url = "https://www.livemint.com/technology/gadgets/top-5-best-water-purifiers-in-india-2025-ideal-for-indian-homes-battling-hard-water-and-impurities-for-safe-drinking-11748061235456.html"
    print("Fetching data from the URL...")
    '''

    #reading the url from the csv file
    df = pd.read_csv("urls_file.csv")

    url = df.iloc[0][1]  #first url

    # Create instance of DataScraper and get data
    scraper = DataScraper(url)
    data = scraper.get_data()

    print("Top 5 Water Purifiers:\n")
    for i, product in enumerate(data[:5], start=1):
        print(f"{i}. {product['name']} | {product['price']} | {product['amazon link']}")

    # Write to output.md
    with open("output.md", "w", encoding="utf-8") as f:
        f.write("## The source file is:\n")
        f.write(f"URL: {url}\n\n")
        f.write("## Data fetched from the URL:\n\n")

        f.write(data.__str__())

        f.write("\n\n## Top 5 Water Purifiers:\n")
        f.write("\n\n")
        for i, product in enumerate(data[:5], start=1):
            f.write(f"{i}. **Name:** {product['name']}\n")
            f.write(f"   - **Price:** {product['price']}\n")
            f.write(f"   - **Amazon Link:** {product['amazon link']}\n\n")
        
        # GPT response section
        '''
        print("Data fetched successfully. Processing data with GPT...")
        gpt_processor = GPTProcessing()
        response = gpt_processor.process_data(data)
        f.write("## Response from GPT:\n\n")
        f.write(response)
        '''

    print("\n📄 Data written to output.md successfully.")

if __name__ == "__main__":
    main()
