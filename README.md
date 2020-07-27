# quandal_api
Get millions of financial and economic datasets from hundreds of publishers via a single free API.
The source for financial, economic, and alternative datasets, serving investment professionals.

To visual data you need high quality, credible and accurtae data sources. Quandal provides and array of data sets for personal (free) and profesional use. 

As part of my Data Engineering profesional development, I am developing an array of data piplines which extract, tranform and load the data from various sources such as this Quandal API, CSV, JSON and database such as Google BigQuery, Microsft SQL Server and PostgreSQL, just to name a few. 

Some pipelines are developed jsut for the purposes of my Data Engineering profesional development. I partice working with a varity of data sources solving specic chanallanges that come as part of handeling and building data pipelnes from the ground up. 

So far I have developed two data pipelines using the Quandal API. 

1. The first behive_stocks_in_united_kindom.py

This data pipeline extracts unfilterd time-series related to stock level for bees in the United Kindom between 1961 and 1987. The main purpose of this datapiprline was to understand and test the API itslf. Later on I will be visualing the data from this pipeline alongside other data such as air quality and such which would help understand why the bee population was at the particular level at the given point in time. 

This data pipeline is quite simple. It consist of the my API key, followed by the payload execution, removal of the index from the retuned DataFrame, renaming of the columns, cleaning the date format from dd-mm-yyy to yyy. Followed by of course writing the DataFrame to a CSV file.  

2. stock_market.py

The purpose of this datapiple is to look at a varirty of datasets aviable and different ways to proccess them. However, the intent is also to visual this data and create a compeling data visualistion using Tableau and or Google Data Studio. 

There are a few notable differances between this data pipeline and the prevoious. To start of with i have broken down the proccess into two functions. 

1. get_latest_data(code, name, code_name):

The purpose of this function is to execute a request unfiltered time-series, stock market data for a one compnay, using the stocl code for that company. 

This data pipeline is quite simple. It consist of the my API key, followed by the payload execution, removal of the index from the retuned DataFrame, Additional code to add the stock code and descriptive name. 


2. get_markets():

The purpose of this function is to iterate through rows in a DataFrame containg the stock codes, descriptive name. The DataFrame in question pd_markets is built off, of a data dictionary that is internt built of two lists: codes and names. The stock code has an addtional piece of code attcahed to it, required by the API "EOD". Each of the indvidual payload request (DataFrames) is appanded to a list called pd_stocks. Finally the list of stock DataFfames are Concatenated into one and saved to a CSV file.  
