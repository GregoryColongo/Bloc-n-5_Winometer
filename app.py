import joblib
from flask import Flask, request, json, jsonify, render_template

MODEL_PATH = "Resources/model.joblib"

app = Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST","GET"])

def predict():
    # Check if request has a JSON content
    if request.json:
        # Get the JSON as dictionnary
        req = request.json
        # Check mandatory key
        if "input" in req.keys():
            # Load model
            classifier = joblib.load(MODEL_PATH)
            # Predict
            prediction = classifier.predict(req["input"])
            # Return the result as JSON but first we need to transform the
            # result so as to be serializable by jsonify()
            prediction = (str(prediction))
            return jsonify({"Quality prediction ": prediction}), 200
    return jsonify({"msg": "Error: not a JSON in your request"})




if __name__ == "__main__":
    app.run(debug=True)