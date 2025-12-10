from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/getfact")
def getfact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
