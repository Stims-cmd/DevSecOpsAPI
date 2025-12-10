
from flask import Flask, jsonify
from flask_cors import CORS
import requests as rq

app= Flask(__name__)
CORS(app)

@app.route("/catfact")

def get_cat_fact():

    lien = "https://catfact.ninja/fact"
    reponse = rq.get(lien)
    affichage = reponse.json()

    return jsonify(affichage)

if __name__=="__main__":
    app.run(debug=True)