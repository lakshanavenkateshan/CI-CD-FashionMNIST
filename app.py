from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Fashion-MNIST API Running Successfully!"})

@app.route('/predict')
def predict():
    return jsonify({"prediction": random.choice(["Sneaker", "T-shirt", "Bag", "Coat"])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
