import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

def run():
    # Load processed data
    data = pd.read_csv('data/processed/processed_data.csv')

    # Split data into features and target
    X = data[['NDVI', 'LST', 'mean_2m_air_temperature', 'total_precipitation']]
    y = data['fire']

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Random Forest model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save the model
    joblib.dump(model, 'models/random_forest.pkl')
    print("Model training completed. Model saved to 'models/'.")