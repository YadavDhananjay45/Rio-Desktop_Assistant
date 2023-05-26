import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf
import datetime as dt

def stockChart():
    stock = input("Enter the stock name: ")
    ticker = ""
    if "tata communication services" in stock or "tcs" in stock:
        ticker = "TCS.NS"
    elif stock == "sbi life insurance" in stock:
        ticker = "SBILIFE.NS"
    elif "hdfc bank" in stock or "hdfc bank" in stock:
        ticker = "HDFCBANK.NS"
    elif "reliance Industries" in stock or "reliance" in stock:
        ticker = "RELIANCE.NS"
    elif "infosys limited" in stock or "infosys" in stock:
        ticker = "INFY.NS"
    elif "ITC" in stock or "itc" in stock:
        ticker = "ITC.NS"
    elif "grasim industries" in stock or "grasim" in stock:
        ticker = "GRASIM.NS"
    elif "bajaj auto" in stock:
        ticker = "BAJAJ-AUTO.NS"
    elif "DIVIS LAB" in stock or "divis lab" in stock:
        ticker = "DIVISLAB.NS"
    elif "TATA MOTORS" in stock or "tata motors" in stock:
        ticker = "TATAMOTOR.NS"
    elif "kotak" in stock or "kotak mahindra bank" in stock:
        ticker = "KOTAKBANK.NS"
    elif "hero motocorp" in stock or "hero" in stock:
        ticker = "HEROMOTOCO.NS"
    elif "nestle" in stock or "NESTLE" in stock:
        ticker = "NESTLEIND.NS"
    elif "ultra cement" in stock or "ULTRA CEMENT" in stock:
        ticker = "ULTRACEMCO.NS"
    elif "titan" in stock or "titan Company" in stock:
        ticker = "TITAN.NS"
    elif (
        stock == "hindustan unilever" in stock or "hindu nilver" in stock or "hul" in stock
    ):
        ticker = "HINDUNILVR.NS"
    elif stock == "larsen and tourbro" in stock or "L and T" in stock:
        ticker = "LT.NS"
    elif stock == "jsw steel" in stock or "JSW STEEL" in stock:
        ticker = "JSWSTEEL.NS"
    elif stock == "TATA STEEL" in stock or "tata steel" in stock:
        ticker = "TATASTEEL.NS"
    elif stock == "airtel" in stock or "bharti airtel" in stock:
        ticker = "BHARTIARTL.NS"
    elif stock == "AXIS BANK" in stock or "axis bank" in stock:
        ticker = "AXISBANK.NS"
    elif (
        stock == "m and m" in stock
        or "mahindra and mahindra limited" in stock
    ):
        ticker = "M&M.NS"
    elif stock == "eicher mototrs" in stock or "eicher motor" in stock:
        ticker = "EICHERMOT.NS"
    elif stock == "HINDALCO" in stock or "hindalco" in stock:
        ticker = "HINDALCO.NS"
    elif stock == "dr reddys lab" in stock or "dr reddy" in stock:
        ticker = "DRREDDY.NS"
    elif stock == "bharat petrolium and company" in stock or "bpcl" in stock:
        ticker = "BPCL.NS"
    elif stock == "adani enterprises" in stock:
        ticker = "ADANIENT.NS"
    elif stock == "BAJAJ FINANCE" in stock or "bajaj finance" in stock:
        ticker = "BAJFINANCE.NS"
    elif stock == "power grid corp" in stock or "power grid" in stock:
        ticker = "POWERGRID.NS"
    elif stock == "ADANI PORTS" in stock or "adani ports" in stock:
        ticker = "ADANIPORTS.NS"
    elif stock == "britannia industries" in stock or "britannia" in stock:
        ticker = "BRITANNIA.NS"
    elif stock == "maruti suzuki" in stock or "maruti" in stock:
        ticker = "MARUTI.NS"
    elif stock == "oil and gas corp" in stock or "ongc" in stock:
        ticker = "ONGC.NS"
    elif stock == "bajaj finserv" in stock:
        ticker = "BAJAFINSV.NS"
    elif stock == "sun pharma industries" in stock or "sun pharma" in stock:
        ticker = "SUNPHARMA.NS"
    elif stock == "state bank of india" in stock or "sbi" in stock:
        ticker = "SBIN.NS"
    elif stock == "apollo hospital enterprises" in stock or "apollo hospital" in stock:
        ticker = "APOLLOHOSP.NS"
    elif stock == "united phosphorus limited" in stock or "upl" in stock:
        ticker = "UPL.NS"
    elif stock == "coal india" in stock:
        ticker = "COALINDIA.NS"
    elif stock == "icici bank" in stock:
        ticker = "ICICIBANK.NS"
    elif stock == "tata consumer products" in stock or "tata consumer" in stock:
        ticker = "TATACONSUM.NS"
    elif stock == "tech mahindra" in stock:
        ticker = "TECHM.NS"
    elif stock == "wipro" in stock:
        ticker = "WIPRO.NS"
    elif stock == "cipla" in stock:
        ticker = "CIPLA.NS"
    elif stock == "hdfc life insurance" in stock or "hdfclife" in stock:
        ticker = "HDFCLIFE.NS"
    elif stock == "national thermal power corp" in stock or "ntpc" in stock:
        ticker = "NTPC.NS"
    elif stock == "asian paints" in stock:
        ticker = "ASIANPAINT.NS"
    elif stock == "hcl tech" in stock:
        ticker = "HCLTECH.NS"
    elif stock == "indusind bank" in stock or "indusind" in stock:
        ticker = "INDUSINDBK.NS"
    else:
        print("enter a valid stock from nifty 50")
    # ticker = input("Enter the Stock name:")

    data = yf.download(ticker, start="2021-01-01", end=dt.datetime.now())
    mpf.plot(data,type="candle",style='yahoo')
    plt.figure(figsize=(10, 5))
    plt.plot(data["Close"])
    plt.title(f"{ticker} stock chart")
    plt.xlabel("date")
    plt.ylabel("price")
    plt.show()

stockChart()
