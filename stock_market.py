import quandl as qd_api
import pandas as pd
import numpy as np

"""
SOURCE: Quotemedia.

TITLE: End of Day US Stock Prices

DESCRIPTION:
Professional-grade EOD stock prices, dividends, adjustments and splits for publicly-traded US stocks. 
Updated daily. History to 1996. Quotemedia data.

Coverage: NYSE, NASDAQ, AMEX, ARCA

Data: Prices, dividends, splits for multiple corporations. 

FREQUENCY: Daily
LAST UPDATED: Daily, 1-day lag. 

REF: https://www.quandl.com/data/EOD-End-of-Day-US-Stock-Prices?filterSelection=sample

"""
# My API key.
qd_api.ApiConfig.api_key = 'qNJwrfms5zNB77vk4qkw'


def get_latest_data(code, name, code_name):

    # Execute payload request.
    api_data = qd_api.get(code)

    # Remove index.
    api_data.reset_index(inplace=True)

    # Add additional columns required for the report.
    api_data["Code"] = code_name
    api_data["Name"] = name

    # Change column order.
    api_data = api_data[["Code", "Name", "Date", "Open",
                         "High", "Low", "Close", "Volume", "Dividend", "Split",
                         "Adj_Open", "Adj_High", "Adj_Low", "Adj_Close", "Adj_Volume"]]

    # Write DataFrame to individual CVS File. This DataFrame is for an single company.
    api_data.to_csv(
        r'/Users/julianmuscatdoublesin/PycharmProjects/PythonLibrary/ds_quandal/quote_media_stock_markets/stock_market_eod_' + code_name + '.csv',
        index=False, header=True)

    return api_data


def get_markets():

    pd_stocks = []
    for lab, row in pd_markets.iterrows():
        pd_stocks.append(get_latest_data("EOD/" + row["code"], row["name"], row["code"]))

        # Concatenate the array of DataFrames into a single DataFrame
        pd_markets_concat = pd.concat(pd_stocks)

        # Write DataFrame to CVS File. This DataFrame is for the list of companies combined.
        pd_markets_concat.to_csv(
            r'/Users/julianmuscatdoublesin/PycharmProjects/PythonLibrary/ds_quandal/stock_market_eod.csv',
            index=False, header=True)

    return pd_markets_concat


# The list of codes required by the API.
lst_code = ["DIS", "MSFT", "INTC", "IBM", "AAPL", "MMM", "PFE", "JNJ", "PG", "NKE"]

# List of names as a reference to each code.
lst_names = ["The Walt Disney Company (DIS)",
             "Microsoft Corporation (MSFT)", "Intel Corporation (INTC)",
             "International Business Machines Corporation (IBM)", "Apple Inc. (AAPL)",
             "3M Company (MMM)", "Pfizer inc. (PFE)", "Johnson & Johnson (JNJ)",
             "Procter & Gamble Company (PG)", "Nike Inc. (NKE)"]

# Converts both lists into on data dictionary.
dict_markets = {
    "name": lst_names,
    "code": lst_code
}

# Converts the data dictionary to a DataFrame.
pd_markets = pd.DataFrame(dict_markets)

# Created a sequential list of numbers to be used as an index for the DataFrame.
row_labels = np.arange(10)

# Specify row labels for the DataFrame.
pd_markets.index = row_labels

# GET LATEST STOCK MARKET DATA.
api_data = get_markets()

# Display returned payload for verification.
print("")
print(api_data)
print(api_data.keys())
print("Size: " + str(api_data.size))
print("Shape: " + str(api_data.shape))
