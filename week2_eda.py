import pandas as pd

sold = pd.read_csv("sold_residential.csv")

#dataset structure
print("Shape (rows, columns):", sold.shape)
print("\nColumns:")
print(sold.columns)
print("\nFirst 5 rows:")
print(sold.head())
print("\nData types:")
print(sold.dtypes)

#prop types/validation
print("\nUnique Property Types:")
print(sold["PropertyType"].unique())

#missing values
print("\nNull count per column:")
print(sold.isnull().sum())
missing_counts = sold.isnull().sum()
missing_percent = (missing_counts / len(sold)) * 100
#missing percent
missing_df = pd.DataFrame({
    "MissingCount": missing_counts,
    "MissingPercent": missing_percent
})
print("\nMissing Value Summary:")
missing_percent = (sold.isnull().sum() / len(sold)) * 100

print("\nMissing % per column:")
print(missing_percent)

#flag >90%
high_missing = missing_df[missing_df["MissingPercent"] > 90]
print("\nColumns with >90% missing:")
print(high_missing)

#summary
# cols = [
#     "ClosePrice", "ListPrice", "OriginalListPrice", "LivingArea", "LotSizeAcres",
#     "BedroomsTotal", "BathroomsTotalInteger", "DaysOnMarket", "YearBuilt"
# ]
cols = ["ClosePrice", "LivingArea", "DaysOnMarket"]
print("\nNumeric Summary:")
print(sold[cols].describe())

print("\nColumns with >90% missing:")
print(high_missing.index.tolist())

# #histogram
# import matplotlib.pyplot as plt
# for col in cols:
#     sold[col].hist()
#     plt.title(col)
#     plt.show()

# #eda qs
# #mean & median price
# print("\nMean ClosePrice:", sold["ClosePrice"].mean())
# print("Median ClosePrice:", sold["ClosePrice"].median())

# #above vs below list
# sold["AboveList"] = sold["ClosePrice"] > sold["ListPrice"]
# print("\nPercent sold above list:")
# print(sold["AboveList"].mean())

# #    Days on Market distribution:
# #date consistency check
# sold["CloseDate"] = pd.to_datetime(sold["CloseDate"])
# sold["ListingContractDate"] = pd.to_datetime(sold["ListingContractDate"])
# bad_dates = sold[sold["CloseDate"] < sold["ListingContractDate"]]
# print("\nRows with CloseDate before ListingDate:", len(bad_dates))

# #county median prices
# print("\nMedian price by county:")
# print(sold.groupby("CountyOrParish")["ClosePrice"].median())

#save
sold.to_csv("sold_residential_cleaned.csv", index=False)