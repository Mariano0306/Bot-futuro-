import time
import math
import requests
from bitget.mix import Mix
from bitget.market import Market
from event import api_key, api_secret, api_passphrase

# === CONFIGURACIÓN ===
SYMBOLS = ["BTCUSDT_UMCBL", "ETHUSDT_UMCBL"]
MARGIN = 40  # USDT por operación
LEVERAGE = 3
STOP_LOSS_ROE = -0.025  # -2.5%
ADJUST_SL_AT_PROFIT = 0.02  # Si la ganancia supera +2%, mover SL a +1%
ADJUSTED_SL_ROE = 0.01
TAKE_PROFIT_ROE = 0.04

# === INICIALIZACIÓN ===
market = Market()
mix = Mix(api_key, api_secret, api_passphrase)

def get_rsi(symbol):
    candles = market.get_candles(symbol, "1m", limit=15)['data']
    closes = [float(c[4]) for c in candles]
    deltas = [closes[i] - closes[i - 1] for i in range(1, len(closes))]
    gains = [delta if delta > 0 else 0 for delta in deltas]
    losses = [-delta if delta < 0 else 0 for delta in deltas]
    avg_gain = sum(gains) / 14
    avg_loss = sum(losses) / 14
    if avg_loss == 0:
        return 100
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def get_news_sentiment():
    try:
        rss_url = "https://www.criptonoticias.com/feed/"
        r = requests.get(rss_url)
        content = r.text.lower()
        keywords = ["caída", "regulación", "prohibición", "venta masiva", "fuga", "quiebra"]
        if any(kw in content for kw in keywords):
            return "negativo"
    except:
        pass
    return "neutral"

def get_position(symbol):
    pos = mix.get_all_position("umcbl", symbol)['data']
    for p in pos:
        if p['holdSide'] == 'long':
            return float(p['total']) if p['total'] else 0
    return 0

def open_long(symbol):
    mix.set_leverage("umcbl", symbol, LEVERAGE, "long")
    mix.place_order("umcbl", symbol, "open_long", "market", sz=str(MARGIN), lever=str(LEVERAGE))

def close_long(symbol):
    mix.place_order("umcbl", symbol, "close_long", "market", sz="100", lever=str(LEVERAGE))

def check_and_trade(symbol):
    rsi = get_rsi(symbol)
    print(f"{symbol} RSI: {rsi}")
    news = get_news_sentiment()
    print(f"Sentimiento de noticias: {news}")
    pos = get_position(symbol)

    if rsi < 30 and news != "negativo" and pos == 0:
        print(f"Abriendo long en {symbol}")
        open_long(symbol)
        time.sleep(5)

    elif pos > 0:
        pos_info = mix.get_single_position("umcbl", symbol)['data']
        roe = float(pos_info['unrealizedRoe']) / 100
        print(f"{symbol} ROE actual: {roe:.2%}")

        if roe <= STOP_LOSS_ROE:
            print("Stop Loss alcanzado. Cerrando posición.")
            close_long(symbol)

        elif roe >= TAKE_PROFIT_ROE:
            print("Take Profit alcanzado. Cerrando posición.")
            close_long(symbol)

        elif roe >= ADJUST_SL_AT_PROFIT:
            new_stop = ADJUSTED_SL_ROE
            print(f"Ajustando Stop Loss a {new_stop:.2%}")
            # En Bitget real, usar trailing o update manual del SL

# === BUCLE PRINCIPAL ===
while True:
    for symbol in SYMBOLS:
        try:
            check_and_trade(symbol)
        except Exception as e:
            print(f"Error en {symbol}: {e}")
    time.sleep(60)

