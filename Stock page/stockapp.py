import yfinance as yf
import datetime
import streamlit as st
st.write("""
# :orange[Simple Stock Price App]

Shown are the stock **closing price** and ***volume*** of Google!

""")

with st.sidebar:
    st.markdown(""" **Select your desired :orange[Ticker] to view** """)

    select_ticker = st.selectbox("Symbol eg. AAPL represents Apple",['MSFT','AAPL','TSLA','NVDA','AMZN','META','AMD','GOOG', 
                        'AS','NRBO','MINM','CCTG','GRI','SMCI','GOOGL','NYCB','FBLG','NXT','PLUG','QCOM'],
                        placeholder='Select One Ticker...',index=None)
    if (select_ticker==None):
        tickerSymbol = 'GOOGL'
    else:
        tickerSymbol = select_ticker

        # with st.container():
        #     col1,col2 = st.columns(2)
        #     with col1:
        #         st.write('START DATE')
        #         st.date_input(  )
    st.markdown(""" **Choose your desired :orange[Date] range to view** """)
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input('Start date',datetime.date(2010, 5, 31))
    with col2:
        end_date = st.date_input('End date',datetime.date(2020, 5, 31))

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
#tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
# Open	High	Low	Close	Volume	Dividends	Stock Splits
tickerDf = tickerData.history(period='1d', start = start_date, end = end_date)

st.write("""## Closing Price of """, tickerSymbol)

st.line_chart(tickerDf.Close)
st.write("""## Volume Price of """, tickerSymbol)

st.line_chart(tickerDf.Volume)
