import yfinance as yf
import pandas as pd
import pandas_ta as ta
import streamlit as st
import requests

# API Key z secrets.toml
FMP_API_KEY = st.secrets["FMP_API_KEY"]

def load_data(ticker):
    data = yf.download(ticker, period="6mo", interval="1d")
    data['RSI'] = ta.rsi(data['Close'])
    data['SMA_50'] = ta.sma(data['Close'], length=50)
    data['SMA_200'] = ta.sma(data['Close'], length=200)
    return data

def get_fundamentals(ticker):
    url = f"https://financialmodelingprep.com/api/v3/profile/{ticker}?apikey={FMP_API_KEY}"
    r = requests.get(url)
    if r.status_code == 200 and r.json():
        return r.json()[0]
    return {}

def main():
    st.set_page_config(layout="wide")
    st.title("📊 Analýza akcií: Technická + Fundamentální")

    ticker = st.text_input("Zadej ticker (např. AAPL)", value="AAPL").upper()
    if ticker:
        data = load_data(ticker)
        fundamentals = get_fundamentals(ticker)

        st.subheader("📈 Technická analýza")
        st.line_chart(data[['Close', 'SMA_50', 'SMA_200']].dropna())
        st.line_chart(data[['RSI']].dropna())

        st.subheader("🧾 Fundamentální ukazatele")
        if fundamentals:
            st.write(f"**Společnost:** {fundamentals.get('companyName')}")
            st.write(f"**P/E Ratio:** {fundamentals.get('pe')}")
            st.write(f"**EPS:** {fundamentals.get('eps')}")
            st.write(f"**Dluh / Vlastní kapitál:** {fundamentals.get('debtToEquity')}")
            st.write(f"**ROE:** {fundamentals.get('returnOnEquity')}")
        else:
            st.warning("Nepodařilo se načíst fundamentální data.")

        st.subheader("🧠 Hodnocení")
        rsi = data['RSI'].iloc[-1]
        if rsi < 30:
            st.success("RSI naznačuje přeprodaný trh – možná příležitost k nákupu.")
        elif rsi > 70:
            st.warning("RSI naznačuje překoupený trh – možná korekce.")
        else:
            st.info("RSI v normálním pásmu – neutrální výhled.")

if __name__ == "__main__":
    main()