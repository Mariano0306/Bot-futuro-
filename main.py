import ccxt
import requests
import time
import datetime
import ta
import pandas as pd
import json

# CONFIGURACIÓN
API_KEY = 'bg_04d83d60492c9c4320dec5f030d4fb3b'
API_SECRET = 'efaff97cdec19c00317754a8f8813d2ab9fdfbc8d3bc0e836ff551210e234404'
API_PASSWORD = 'Martomas1982'

symbol = "BTC/USDT"  # Cambiá esto si querés otra cripto
capital = 22         # Cambiá este valor para operar con otro capital
leverage = 3
max_loss_pct = 3
profit_partial_pct = 1.5

bitget = ccxt.bitget({
    'apiKey': API_KEY,
    'secret': API_SECRET,
    'password': API_PASSWORD,
    'enableRateLimit': True,
    'options': {'defaultType': 'swap'}
})

market = bitget.market(symbol)
bitget.set_leverage(leverage, symbol)

# FUNCIONES
def get_price(symbol):
    try:
        ticker = bitget.fetch_ticker(symbol)
        return ticker['last']
    except Exception as e:
        print(f"[get_price ERROR] {e}")
        return None

def fetch_ohlcv(symbol):
    try:
        data = bitget.fetch_ohlcv(symbol, timeframe='1m', limit=100)
        df = pd.DataFrame(data, columns=['timestamp','open','high','low','close','volume'])
        return df
    except Exception as e:
        print(f"[fetch_ohlcv ERROR] {e}")
        return None

def rsi_signal(df):
    try:
        df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()
        return df['rsi'].iloc[-1]
    except:
        return 50

def get_news_signal():
    try:
        res = requests.get("https://cryptopanic.com/api/v1/posts/?auth_token=demo&currencies=BTC")
        news = res.json()
        for post in news['results']:
            title = post['title'].lower()
            if any(x in title for x in ['etf', 'approval', 'hack', 'inflation', 'crash', 'bullish', 'bearish']):
                return True
        return False
    except Exception as e:
        print(f"[NEWS ERROR] {e}")
        return False

def place_order(symbol, side, amount, stop_loss, take_profit):
    try:
        order = bitget.create_order(symbol=symbol, type='market', side=side, amount=amount)
        print(f"[ORDEN] {side} ejecutada a mercado")
        return order
    except Exception as e:
        print(f"[place_order ERROR] {e}")
        return None

def trailing_stop(entry_price, current_price, stop_price):
    gain = (current_price - entry_price) / entry_price * 100
    if gain >= profit_partial_pct:
        new_stop = entry_price
        if current_price > entry_price:
            new_stop = current_price * 0.997
        return new_stop
    return stop_price

# LOOP PRINCIPAL
print("🤖 Iniciando bot de scalping conservador...\n")

position_open = False
entry_price = 0
stop_price = 0
amount = 0

while True:
    df = fetch_ohlcv(symbol)
    if df is None:
        time.sleep(60)
        continue

    price = get_price(symbol)
    rsi = rsi_signal(df)
    news = get_news_signal()

    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Precio: {price:.2f} | RSI: {rsi:.2f} | Noticia: {'✅' if news else '❌'}")

    if not position_open:
        if rsi < 30 and news:
            amount = (capital * leverage) / price
            entry_price = price
            stop_price = entry_price * (1 - max_loss_pct / 100)
            place_order(symbol, 'buy', amount, stop_price, 0)
            position_open = True
            print(f"📈 Entrada en {entry_price:.2f} | Stop inicial: {stop_price:.2f}")
    else:
        if price < stop_price:
            print("🛑 Stop loss alcanzado. Cerrando posición.")
            place_order(symbol, 'sell', amount, 0, 0)
            position_open = False
        else:
            stop_price = trailing_stop(entry_price, price, stop_price)

    time.sleep(60)
