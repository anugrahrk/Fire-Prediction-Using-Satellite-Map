import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
import joblib

def run():
    # Load processed data
    data = pd.read_csv('data/processed/processed_data.csv')

    # Split data into features and target
    X = data[['NDVI', 'LST', 'mean_2m_air_temperature', 'total_precipitation']]
    y = data['fire']

    # Load the trained model
    model = joblib.load('models/random_forest.pkl')

    # Make predictions
    y_pred = model.predict(X)

    # Evaluate the model
    print("Accuracy:", accuracy_score(y, y_pred))
    print("Classification Report:\n", classification_report(y, y_pred))