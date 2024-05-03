import requests
import csv
import datetime

basic_url = "https://www.alphavantage.co/query?function="
api_function = "TIME_SERIES_intraday"
symbol = "MSFT"
interval = "5min"
