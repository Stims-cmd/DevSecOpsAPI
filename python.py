from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Autorise toutes les requêtes cross-origin

@app.route("/getfact")
def getfact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
