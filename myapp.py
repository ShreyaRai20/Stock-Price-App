import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
### Simple Stock Market Price App

shown are the stock ***Closing Price*** and ***Volume*** of google!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-cOdeldf17e75
#define the ticker symbol
tickerSymbol = 'AAPL'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end = '2020-5-31')
# Open High Low Close Volume Dividends Stock Splits

st.write("""
        ***Closing Price***
""")

st.line_chart(tickerDf.Close)

st.write("""
***Volume***
""")

st.line_chart(tickerDf.Volume)
