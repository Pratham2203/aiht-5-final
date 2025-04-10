# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import numpy as np
# import joblib

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# # Load the pre-trained VotingClassifier (ensemble model)
# voting_clf = joblib.load('./models/ensemble.pkl')

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json
#     features = np.array(data['features']).reshape(1, -1)

#     # Make prediction using the ensemble model
#     prediction = voting_clf.predict(features)
#     risk = 'High' if prediction[0] == 1 else 'Low'

#     return jsonify({'risk': risk})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import numpy as np
# import joblib
# import os

# app = Flask(__name__)

# # Enable CORS only for the '/predict' route
# CORS(app, resources={r"/predict": {"origins": "*"}})

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the directory of app.py
# MODEL_PATH = os.path.join(BASE_DIR, "../models/ensemble.pkl")

# try:
#     voting_clf = joblib.load(MODEL_PATH)
# except FileNotFoundError:
#     print(f"Error: Model file not found at {MODEL_PATH}")
#     voting_clf = None  # Set to None to avoid crashes

# @app.route('/')
# def home():
#     return jsonify({"message": "Flask API is running!", "status": "OK"})

# @app.route('/predict', methods=['POST'])
# def predict():
#     if voting_clf is None:
#         return jsonify({"error": "Model not loaded"}), 500

#     try:
#         data = request.json
#         if "features" not in data:
#             return jsonify({"error": "Missing 'features' key in request JSON"}), 400
        
#         features = np.array(data["features"]).reshape(1, -1)

#         # Make prediction using the ensemble model
#         prediction = voting_clf.predict(features)
#         risk = "High" if prediction[0] == 1 else "Low"

#         return jsonify({"risk": risk})
    
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)


# from flask import Flask, request, jsonify, send_from_directory
# from flask_cors import CORS
# import numpy as np
# import joblib
# import os

# app = Flask(__name__, static_folder="static", template_folder="static")

# CORS(app, origins=['https://your-render-app-url.com','http://127.0.0.1:5000/predict', 'http://localhost:5000','http://localhost:3000'])


# # Load the trained model
# model_path = os.path.join(os.path.dirname(__file__), '../models/ensemble.pkl')
# voting_clf = joblib.load(model_path)

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json
#     features = np.array(data['features']).reshape(1, -1)
#     prediction = voting_clf.predict(features)
#     risk = 'High' if prediction[0] == 1 else 'Low'
#     return jsonify({'risk': risk})

# # Serve frontend
# @app.route("/", defaults={"path": ""})
# @app.route("/<path:path>")
# def serve_static(path):
#     if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
#         return send_from_directory(app.static_folder, path)
#     return send_from_directory(app.static_folder, "index.html")  # Serve index.html for SPA

# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 5000))  # Render assigns a port dynamically
#     # app.run(host='0.0.0.0', port=port, debug=False)
#     app.run(host='0.0.0.0', port=5000, debug=True)
 

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import numpy as np
import os
import random  # <-- Add this

app = Flask(__name__, static_folder="static", template_folder="static")

CORS(app, origins=[
    'https://your-render-app-url.com',
    'http://127.0.0.1:5000/predict',
    'http://localhost:5000',
    'http://localhost:3000'
])

# Randomized prediction (Fake results)
@app.route('/predict', methods=['POST'])
def predict():
    fake_risks = ['High', 'Low', 'Moderate', 'Extremely Risky']
    random_risk = random.choice(fake_risks)
    return jsonify({'risk': random_risk})

if __name__ == '__main__':
    #  port = int(os.environ.get("PORT", 5000))  # Render assigns a port dynamically
    #app.run(host='0.0.0.0', port=port, debug=False)
    app.run(host='0.0.0.0', port=5000, debug=True)