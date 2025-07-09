import ccxt
import requests
import time
import datetime
import ta
import pandas as pd

# ========== CONFIGURACIÓN ==========
API_KEY = 'bg_04d83d60492c9c4320dec5f030d4fb3b'
API_SECRET = 'efaff97cdec19c00317754a8f8813d2ab9fdfbc8d3bc0e836ff551210e234404'
API_PASSWORD = 'Martomas1982'

symbol = 'BTCUSDT_UMCBL'
capital = 22.0
leverage = 3
max_loss_pct = 3
profit_partial_pct = 1.5

# ========== BITGET INIT ==========
bitget = ccxt.bitget({
    'apiKey': API_KEY,
    'secret': API_SECRET,
    'password': API_PASSWORD,
    'enableRateLimit': True,
    'options': {'defaultType': 'swap'}
})

bitget.load_markets()
market = bitget.market(symbol)
bitget.set_leverage(leverage, symbol, params={"productType": market['info']['productType']})

# ========== FUNCIONES ==========
def get_price(symbol):
    try:
        ticker = bitget.fetch_ticker(symbol)
        return ticker['last']
    except Exception as e:
        print(f"[ERROR] get_price: {e}")
        return None

def fetch_ohlcv(symbol):
    try:
        data = bitget.fetch_ohlcv(symbol, timeframe='1m', limit=100)
        df = pd.DataFrame(data, columns=['timestamp','open','high','low','close','volume'])
        return df
    except Exception as e:
        print(f"[ERROR] fetch_ohlcv: {e}")
        return None

def rsi_signal(df):
    try:
        df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()
        return df['rsi'].iloc[-1]
    except Exception as e:
        print(f"[ERROR] rsi_signal: {e}")
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
        print(f"[ERROR] get_news_signal: {e}")
        return False

def place_order(symbol, side, amount):
    try:
        order = bitget.create_order(symbol=symbol, type='market', side=side, amount=amount)
        print(f"[ORDEN] {side.upper()} ejecutada: {amount:.4f}")
        return order
    except Exception as e:
        print(f"[ERROR] place_order: {e}")
        return None

def trailing_stop(entry, current, stop):
    gain_pct = (current - entry) / entry * 100
    if gain_pct >= profit_partial_pct and current * 0.997 > stop:
        new_stop = current * 0.997
        print(f"[INFO] Ajuste de stop a: {new_stop:.2f}")
        return new_stop
    return stop

# ========== LOOP PRINCIPAL ==========
print("🤖 Bot scalping Bitget iniciado...\n")

position_open = False
entry_price = 0
stop_price = 0
amount = 0

while True:
    try:
        df = fetch_ohlcv(symbol)
        if df is None:
            time.sleep(30)
            continue

        price = get_price(symbol)
        if price is None:
            time.sleep(30)
            continue

        rsi = rsi_signal(df)
        news = get_news_signal()

        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Precio: {price:.2f} | RSI: {rsi:.2f} | Noticia: {'✅' if news else '❌'}")

        if not position_open:
            if rsi < 30 and news:
                amount = (capital * leverage) / price
                entry_price = price
                stop_price = entry_price * (1 - max_loss_pct / 100)
                place_order(symbol, 'buy', amount)
                print(f"📈 Entrada: {entry_price:.2f} | Stop inicial: {stop_price:.2f}")
                position_open = True
        else:
            if price < stop_price:
                print("🛑 Stop loss alcanzado. Cerrando posición.")
                place_order(symbol, 'sell', amount)
                position_open = False
            else:
                stop_price = trailing_stop(entry_price, price, stop_price)

        time.sleep(60)

    except Exception as e:
        print(f"[ERROR LOOP] {e}")
        time.sleep(60)
