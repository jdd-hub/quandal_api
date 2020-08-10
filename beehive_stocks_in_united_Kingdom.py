import quandl as qd_api

"""
SOURCE: United Nations Food and Agriculture.

TITLE: Beehive Stocks in United Kingdom

DESCRIPTION:
Beehive Stocks in United Kingdom. 
The Food and Agriculture Organization generates wide-ranging data on many agricultural 
products from most countries and areas on a world-wide basis. 
For more info, please visit http://faostat.fao.org/

FREQUENCY: Year
LAST UPDATED: 3 days ago, on 24 Jul 2020 

REF: https://www.quandl.com/data/UFAO/LV_BEE_GBR

"""

# My API key.
qd_api.ApiConfig.api_key = '####################'

# Execute payload request.
api_data = qd_api.get('UFAO/LV_BEE_GBR', collapse="yearly")

# Remove index.
api_data.reset_index(inplace=True)

# Rename API Columns.
api_data.rename(columns={'Date': 'Year', 'Stocks - No': 'Stock'}, inplace=True)

# Change Date format for date to year.
lst_year = []
for lab, row in api_data.iterrows():
    str_year = str(row["Year"]).split('-')[0]
    lst_year.append(str_year)

# Update the year series with the updated year date format.
api_data["Year"] = lst_year

# Write DataFrame to CVS File.
api_data.to_csv(r'/Users/julianmuscatdoublesin/PycharmProjects/PythonLibrary/ds_quandal/ufao_beehive_stock.csv', index=False, header=True)

# Display returned payload for verification.
print("")
print(api_data)
print("Keys: " + api_data.keys())
print("Size: " + str(api_data.size))
print("Shape: " + str(api_data.shape))
