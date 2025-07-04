import pandas as pd
from water_purifier.scraper import DataScraper
from water_purifier.llm_processing import LLMClient
from water_purifier.write_to_file import DataWriter
def main() :

    #reading the url from the csv file
    df = pd.read_csv("urls_file.csv")

    url = df.iloc[0][1]  #first url 
    #getting output from scraper
    scraper = DataScraper(url)
    data = scraper.get_data()

    #creating instance of LLMClient
    llm_client = LLMClient()
    #Process the data

    prompt = ""
    output = llm_client.run(prompt, data)

    #output data
    writer = DataWriter(output, url)
    writer.write_output_to_file()
    print("\n Data written to output.md successfully.")

if __name__ == "__main__" :
    main()