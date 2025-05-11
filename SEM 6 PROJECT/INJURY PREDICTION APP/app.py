from flask import Flask, request, render_template
import pickle
import numpy as np
import os

app = Flask(__name__, static_folder="static")

# Load the model
model_path = os.path.join(os.path.dirname(__file__), "injury_model.pkl")
model = pickle.load(open(model_path, "rb"))

# Feature names (must match the 10 features used in training)
feature_names = [
    'age', 'season_minutes_played', 'season_games_played', 'pace', 'physic',
    'bmi', 'minutes_per_game_prev_seasons', 'avg_days_injured_prev_seasons',
    'cumulative_minutes_played', 'cumulative_games_played'
]

# Print model details
print("Number of features expected by model:", model.n_features_in_)
print("Feature importances:", dict(zip(feature_names, model.feature_importances_)))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Map form inputs to the exact 10 features
        features = [
            float(request.form['age']),
            float(request.form['season_minutes_played']),
            float(request.form['season_games_played']),
            float(request.form['pace']),
            float(request.form['physic']),
            float(request.form['bmi']),
            float(request.form['minutes_per_game_prev_seasons']),
            float(request.form['avg_days_injured_prev_seasons']),
            float(request.form['cumulative_minutes_played']),
            float(request.form['cumulative_games_played'])
        ]
        print("Raw form inputs:", request.form)
        print("Features for prediction:", features)
        
        # Verify feature count
        if len(features) != model.n_features_in_:
            raise ValueError(f"Expected {model.n_features_in_} features, got {len(features)}")
        
        # Predict
        prediction = model.predict([features])[0]
        
        # Determine result and check for high risk
        if prediction == 1:
            # High risk: find the most important feature
            importances = model.feature_importances_
            max_importance_idx = np.argmax(importances)
            key_feature = feature_names[max_importance_idx]
            result = f"⚡️ High Risk of Injury ⚠️<br>Key Factor: {key_feature.replace('_', ' ').title()}"
        else:
            result = "✅ Low Risk of Injury"
        
        return render_template("index.html", prediction=result)
    except Exception as e:
        return render_template("index.html", prediction=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)