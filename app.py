from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

# Ta clé API NewsAPI
NEWS_API_KEY = "6de822b5d43943f280de002acc208fcf"

@app.route("/get-news", methods=["GET"])
def get_news():
    country = request.args.get("country", "us")  # Par défaut, "fr" pour la France
    try:
        # Appel à l'API NewsAPI
        url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}"
        response = requests.get(url)

        # Vérifie si la requête est réussie
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "Failed to fetch news", "status_code": response.status_code}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/')
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
