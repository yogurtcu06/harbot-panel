
from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

def get_mock_signals():
    # Gerçek analiz motoru buraya entegre edilebilir
    coins = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT"]
    signals = []
    for coin in coins:
        signal = random.choice(["BUY", "SELL", "NEUTRAL"])
        signals.append({"coin": coin, "signal": signal})
    return signals

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/signal", methods=["GET"])
def get_signals():
    result = get_mock_signals()
    return jsonify({"status": "success", "data": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
