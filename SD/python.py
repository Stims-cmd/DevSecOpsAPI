from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Autorise le frontend à faire des requêtes

@app.route("/pokemon/<name>")
def get_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Pokémon non trouvé"}), 404

    data = response.json()

    # On récupère seulement ce qui nous intéresse
    result = {
        "name": data["name"].capitalize(),
        "stats": {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]},
        "sprite": data["sprites"]["front_default"]
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
