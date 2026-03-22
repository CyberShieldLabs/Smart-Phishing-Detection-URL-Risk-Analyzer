from flask import Flask, request, jsonify
from modules.pipeline import process_url

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is running"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    result = process_url(data)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
