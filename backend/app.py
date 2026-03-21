from flask import Flask, request, jsonify
from modules.validator import validate_url_input

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is running "

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Step 1: Validate input
    result = validate_url_input(data)

    # If error → stop pipeline
    if result["status"] == "error":

        return jsonify(result)

    # If success → continue (next step later)
    return jsonify({
        "status": "success",
        "message": "Validation passed",
        "clean_url": result["clean_url"]
    })

if __name__ == "__main__":
    app.run(debug=True)
