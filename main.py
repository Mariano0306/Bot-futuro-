import requests
import time
import hmac
import hashlib
import json

# ===================== CONFIGURACIÓN =====================
API_KEY = 'bg_04d83d60492c9c4320dec5f030d4fb3b'
API_SECRET = 'efaff97cdec19c00317754a8f8813d2ab9fdfbc8d3bc0e836ff551210e234404'
API_PASSPHRASE = 'Martomas1982'
BASE_URL = 'https://api.bitget.com'
SYMBOL = 'BTCUSDT_UMCBL'
LEVERAGE = 3
CAPITAL_USDT = 33
STOP_LOSS_PERCENT = 3
TAKE_PROFIT_PERCENT = 3

# ===================== HEADERS =====================
def get_headers(timestamp, method, request_path, body=''):
    message = f'{timestamp}{method}{request_path}{body}'
    signature = hmac.new(API_SECRET.encode(), message.encode(), hashlib.sha256).hexdigest()
    return {
        'Content-Type': 'application/json',
        'ACCESS-KEY': API_KEY,
        'ACCESS-SIGN': signature,
        'ACCESS-TIMESTAMP': str(timestamp),
        'ACCESS-PASSPHRASE': API_PASSPHRASE
    }

# ===================== UTILIDADES =====================
def get_timestamp():
    return int(time.time() * 1000)

def get_price():
    url = f"{BASE_URL}/api/mix/v1/market/ticker?symbol={SYMBOL}"
    try:
        res = requests.get(url)
        data = res.json()
        return float(data['data']['last'])
    except:
        print("[get_price ERROR] No se pudo obtener precio")
        return None

def get_rsi(prices, period=14):
    if len(prices) < period + 1:
        return 50  # neutral
    deltas = [prices[i+1] - prices[i] for i in range(len(prices)-1)]
    gains = sum([d for d in deltas[-period:] if d > 0]) / period
    losses = -sum([d for d in deltas[-period:] if d < 0]) / period
    rs = gains / losses if losses != 0 else 0
    return 100 - (100 / (1 + rs))

def get_news_sentiment():
    try:
        res = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        if res.status_code == 200:
            return "neutral"
    except:
        print("[NEWS ERROR] No se pudo obtener noticias")
    return "neutral"

# ===================== OPERACIONES =====================
def place_order(side, price):
    timestamp = get_timestamp()
    margin = CAPITAL_USDT * LEVERAGE
    quantity = round(margin / price, 3)
    body = {
        "symbol": SYMBOL,
        "marginCoin": "USDT",
        "size": str(quantity),
        "side": side,
        "orderType": "market",
        "timeInForceValue": "normal"
    }
    headers = get_headers(timestamp, 'POST', '/api/mix/v1/order/placeOrder', json.dumps(body))
    url = f"{BASE_URL}/api/mix/v1/order/placeOrder"
    try:
        res = requests.post(url, headers=headers, data=json.dumps(body))
        print(f"[ORDER] {side.upper()} ejecutada. Respuesta: {res.text}")
    except Exception as e:
        print(f"[ORDER ERROR] {e}")

# ===================== BOT LOOP =====================
def bot_loop():
    precios = []
    stop_price = None
    entry_price = None
    position = None

    print("🤖 Bot de scalping con noticias funcionando...")

    while True:
        precio_actual = get_price()
        if not precio_actual:
            time.sleep(10)
            continue

        precios.append(precio_actual)
        if len(precios) > 100:
            precios = precios[-100:]

        rsi = get_rsi(precios)
        cambio = round(((precios[-1] - precios[-2]) / precios[-2]) * 100, 2) if len(precios) > 2 else 0
        noticias = get_news_sentiment()

        print(f"[{time.strftime('%H:%M:%S')}] Precio: {precio_actual} | RSI: {rsi:.2f} | Cambio: {cambio}% | News: {noticias}")

        if not position:
            if rsi < 30 and cambio > 0 and noticias == "neutral":
                entry_price = precio_actual
                stop_price = entry_price * (1 - STOP_LOSS_PERCENT / 100)
                target_price = entry_price * (1 + TAKE_PROFIT_PERCENT / 100)
                place_order('open_long', precio_actual)
                position = "long"
        else:
            if precio_actual <= stop_price:
                place_order('close_long', precio_actual)
                print("🛑 Stop activado")
                position = None
            elif precio_actual >= target_price:
                stop_price = entry_price  # se ajusta a break even
                print("✅ Profit parcial alcanzado, moviendo stop a entrada")

        time.sleep(20)

# ===================== INICIO =====================
if __name__ == "__main__":
    bot_loop()
