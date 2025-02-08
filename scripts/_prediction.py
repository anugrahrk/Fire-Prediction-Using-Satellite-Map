import joblib

def run():
    # Load the trained model
    model = joblib.load('models/random_forest.pkl')

    # Make predictions on new data
    new_data = [[0.5, 30, 25, 0]]  # Example: [NDVI, LST, Temperature, Precipitation]
    prediction = model.predict(new_data)
    print("Prediction:", prediction)