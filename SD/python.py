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

    # 1. Récupérer le nom du Pokémon
    pokemon_name = data["name"].capitalize()

    # 2. Récupérer les statistiques
    pokemon_stats = {}
    for stat in data["stats"]:
        stat_name = stat["stat"]["name"]       
        stat_value = stat["base_stat"]         
        pokemon_stats[stat_name] = stat_value  

    # 3. Récupérer l'URL du sprite
    pokemon_sprite = data["sprites"]["front_default"]

    # 4. Construire le résultat final
    result = {
        "name": pokemon_name,
        "stats": pokemon_stats,
        "sprite": pokemon_sprite
    }

    # 5. Retour au frontend
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
