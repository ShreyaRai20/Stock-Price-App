import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
### Simple Stock Market Price App

shown are the stock ***Closing Price*** and ***Volume*** of google!
""")

tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-5-31', end = '2020-5-31')


st.write("""
        ***Closing Price***
""")

st.line_chart(tickerDf.Close)

st.write("""
***Volume***
""")

st.line_chart(tickerDf.Volume)