import pandas as pd
dataf = pd.read_csv("urls_file.csv")
#print(dataf)

#first url
url = dataf.iloc[0][1]
print("first url is ", url)