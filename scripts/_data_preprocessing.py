import pandas as pd

def run():
    # Load raw data
    data = pd.read_csv('data/raw/fire_data.csv')

    # Preprocess data (e.g., calculate NDVI, LST)
    # Use the correct band names: SR_B4 (Red), SR_B5 (NIR), ST_B10 (Thermal)
    data['NDVI'] = (data['SR_B5'] - data['SR_B4']) / (data['SR_B5'] + data['SR_B4'])
    data['LST'] = data['ST_B10'] * 0.1  # Convert thermal band to LST

    # Save processed data
    data.to_csv('data/processed/processed_data.csv', index=False)
    print("Data preprocessing completed. Processed data saved to 'data/processed/'.")