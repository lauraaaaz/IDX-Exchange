import pandas as pd
import glob

#sold files:

sold_files = glob.glob("CRMLSSold*.csv")

sold_list = []

for file in sold_files:
    df = pd.read_csv(file)
    print(f"{file}: {len(df)} rows (before concat)")
    sold_list.append(df)

sold_combined = pd.concat(sold_list)

print("Total sold rows after concat:", len(sold_combined))
print("Sold rows before filter:", len(sold_combined)) #filter res

sold_res = sold_combined[sold_combined["PropertyType"] == "Residential"]

print("Sold rows after filter:", len(sold_res))

sold_res.to_csv("sold_residential.csv", index=False)


#listing files:

listing_files = glob.glob("CRMLSListing*.csv")

listing_list = []

for file in listing_files:
    df = pd.read_csv(file)
    print(f"{file}: {len(df)} rows (before concat)")
    listing_list.append(df)

listing_combined = pd.concat(listing_list)

print("Total listing rows after concat:", len(listing_combined))
print("Listing rows before filter:", len(listing_combined)) #filter res

listing_res = listing_combined[listing_combined["PropertyType"] == "Residential"]

print("Listing rows after filter:", len(listing_res))

listing_res.to_csv("listings_residential.csv", index=False)