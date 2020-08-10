# quandl_api
Get millions of financial and economic datasets from hundreds of publishers via a single free API.
The source for financial, economic, and alternative datasets, serving investment professionals.

To visual data, you need high quality, credible and accurate data sources. Quandl provides and an array of data sets for personal (free) and professional use. 

As part of my Data Engineering professional development, I am developing an array of data pipelines which extract, tranform and load the data from various sources such as this Quandl API, CSV, JSON and database such as Google BigQuery, Microsft SQL Server and PostgreSQL, just to name a few. 

Some pipelines are developed just for the purposes of my Data Engineering professional development. I practice working with a variety of data sources solving specific challenges that come as part of handling and building data pipelines from the ground up. 

So far, I have developed two data pipelines using the Quandl API. 

1. The first behive_stocks_in_united_kindom.py

This data pipeline extracts unfiltered time-series related to stock level for bees in the United Kindom between 1961 and 1987. The main purpose of this data pipeline was to understand and test the API itself. Later on, I will be visualising the data from this pipeline alongside other data such as air quality and such which would help understand why the bee population was at the particular level at the given point in time. 

This data pipeline is quite simple. It consists of the API key, followed by the payload execution, removal of the index from the retuned DataFrame, renaming of the columns, cleaning the date format from dd-mm-yyy to yyy, followed by of course writing the DataFrame to a CSV file.  

2. stock_market.py

The purpose of this data pipeline is to look at a variety of datasets available and different ways to process them. However, the intent is also to visual this data and create a compelling data visualisation using Tableau and or Google Data Studio. 

There are a few notable differences between this data pipeline and the previous. To start off with, I have broken down the process into two functions. 

1. get_latest_data(code, name, code_name):

The purpose of this function is to execute a request: unfiltered time-series, stock market data for one company, using the stock code for that company. 

This data pipeline is quite simple. It consists of the API key, followed by the payload execution, removal of the index from the retuned DataFrame, Additional code to add the stock code and descriptive name. 


2. get_markets():

The purpose of this function is to iterate through rows in a DataFrame containing the stock codes and descriptive name. The DataFrame in question pd_markets is built off, of a data dictionary that is built of two lists: codes and names. The stock code has an additional piece of code attached to it, required by the API "EOD". Each of the individual payload request (DataFrames) is appended to a list called pd_stocks. Finally, the list of stock DataFfames is Concatenated into one and saved to a CSV file.  
