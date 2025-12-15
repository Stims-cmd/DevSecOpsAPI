from flask import Flask, jsonify, send_file
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return send_file("html_pokeapi.html")

@app.route("/pokemon/<name>")
def get_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Pokémon non trouvé"}), 404

    data = response.json()
    result = {
        "name": data["name"].capitalize(),
        "stats": {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]},
        "sprite": data["sprites"]["front_default"]
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
