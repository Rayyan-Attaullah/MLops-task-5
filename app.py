# app.py
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.joblib')

@app.route('/')
def home():
    return "Hello, World! This is a simple ML model deployment."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Assuming the data is a list of features
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# app.py
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.joblib')

@app.route('/')
def home():
    return "Hello, World! This is a simple ML model deployment."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Assuming the data is a list of features
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
