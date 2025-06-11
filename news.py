from flask import Flask, jsonify
import requests
from datetime import datetime
import json
import os

app = Flask(__name__)
NEWS_API_KEY = "ccd9f41274894b25961597cbb87d48c9"
NEWS_JSON_PATH = "news_cache.json"

PAIRS = {
    "audusd": "AUDUSD",
    "usdjpy": "USDJPY",
    "gbpusd": "GBPUSD",
    "nzdusd": "NZDUSD",
    "eurusd": "EURUSD"
}

def fetch_news(pair):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": pair,
        "language": "en",
        "pageSize": 5,
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY
    }
    r = requests.get(url, params=params)
    r.raise_for_status()
    return r.json().get("articles", [])

def fetch_and_save_all_news():
    results = {}
    for key, symbol in PAIRS.items():
        articles = fetch_news(symbol)
        news_list = []
        for a in articles:
            news_item = {
                "title": a.get("title"),
                "slug": a.get("title", "").lower().replace(" ", "-")[:80],
                "content": a.get("content"),
                "excerpt": a.get("description"),
                "image": a.get("urlToImage"),
                "created_at": a.get("publishedAt"),
                "source": a.get("source", {}).get("name"),
                "url": a.get("url")
            }
            news_list.append(news_item)
        results[key] = news_list
    # Simpan ke file JSON
    with open(NEWS_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

@app.route("/news", methods=["GET"])
def get_forex_news():
    # Baca dari file JSON cache
    if os.path.exists(NEWS_JSON_PATH):
        with open(NEWS_JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data)
    else:
        return jsonify({"error": "News cache not found."}), 404

if __name__ == "__main__":
    # Fetch dan simpan news saat server start
    print("Fetching news and saving to cache...")
    fetch_and_save_all_news()
    print("News cached. Starting server.")
    app.run(debug=True)