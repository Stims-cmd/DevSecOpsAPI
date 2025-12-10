
from flask import Flask, jsonify
import requests as rq

app= Flask(__name__)

@app.route("/catfact")

def get_cat_fact():

    lien = "https://catfact.ninja/fact"
    reponse = rq.get(lien)
    affichage = reponse.json()

    return jsonify(affichage)

if __name__=="__main__":
    app.run(debug=True)