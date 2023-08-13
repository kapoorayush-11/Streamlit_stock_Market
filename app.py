import streamlit as st
import datetime
import yfinance as yf

st.title("**Stock Price Analyser**")

## Get data for Apple Stock
symbol  = st.selectbox(
    'Which Stock Symbol you want to analyze',
    ('AAPL','ADBE','ADP', 'GOOG', 'EBAY', 'TSLA', 'MSFT', 'NFLX'))

col1, col2 = st.columns(2)


with col1:
    start_date = st.date_input("Start Date",datetime.date(2019,7,6))

with col2:
    end_date = st.date_input("End Date",datetime.date(2020,7,10))

ticker_data = yf.Ticker(symbol)
ticker_df = ticker_data.history(period="1d", start=start_date, end=end_date)

st.write(f"""
   {symbol} Stock Price Data      
         """);

st.dataframe(ticker_df)


st.write(f"""
   {symbol} Closing price Chart   """);

st.line_chart(ticker_df["Close"])

st.write(f"""
   {symbol} Volume price Chart   """);

st.bar_chart(ticker_df["Volume"])


st.write(f"""
   {symbol} Open price Chart   """);

st.area_chart(ticker_df["Open"])
