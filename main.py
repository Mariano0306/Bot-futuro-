import ccxt
import requests
import time
import datetime
import ta
import pandas as pd

# ✅ TUS CLAVES API Bitget (ya colocadas)
API_KEY = ''bg_04d83d60492c9c4320dec5f030d4fb3b
API_SECRET = 'efaff97cdec19c00317754a8f8813d2ab9fdfbc8d3bc0e836ff551210e234404'
API_PASSWORD = 'Martomas1982'

# ✅ Parámetros de operación (podés cambiar el capital cuando quieras)
symbol = 'BTC/USDT'
capital = 22.0  # Cambiá este número si querés operar con más USDT
leverage = 3
max_loss_pct = 3
profit_partial_pct = 1.5

# ✅ Configuración de la conexión con Bitget
bitget = ccxt.bitget({
    'apiKey': API_KEY,
    'secret': API_SECRET,
    'password': API_PASSWORD,
    'enableRateLimit': True,
    'options': {'defaultType': 'swap'}
})

bitget.load_markets()
bitget.set_leverage(leverage, symbol)

# ✅ Obtención de precio actual
def get_price(symbol):
    try:
        ticker = bitget.fetch_ticker(symbol)
        return ticker['last']
    except Exception as e:
        print(f"[get_price ERROR] {e}")
        return None

# ✅ Trae los últimos 100 velas de 1 minuto
def fetch_ohlcv(symbol):
    try:
        data = bitget.fetch_ohlcv(symbol, timeframe='1m', limit=100)
        df = pd.DataFrame(data, columns=['timestamp','open','high','low','close','volume'])
        return df
    except Exception as e:
        print(f"[fetch_ohlcv ERROR] {e}")
        return None

# ✅ Señal con RSI
def rsi_signal(df):
    try:
        df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()
        return df['rsi'].iloc[-1]
    except:
        return 50

# ✅ Revisa noticias importantes
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

# ✅ Ejecuta orden
def place_order(symbol, side, amount, stop_loss, take_profit):
    try:
        order = bitget.create_order(symbol=symbol, type='market', side=side, amount=amount)
        print(f"[ORDEN] {side.upper()} ejecutada a mercado")
        return order
    except Exception as e:
        print(f"[place_order ERROR] {e}")
        return None

# ✅ Calcula stop dinámico
def trailing_stop(entry_price, current_price, stop_price):
    gain = (current_price - entry_price) / entry_price * 100
    if gain >= profit_partial_pct:
        new_stop = current_price * 0.997  # Ajuste dinámico
        return new_stop
    return stop_price

# ✅ Loop principal
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
