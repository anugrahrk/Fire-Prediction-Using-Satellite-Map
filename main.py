from scripts import _data_collection, _data_preprocessing, _model_training, _model_evaluation, _prediction

if __name__ == "__main__":
    # Step 1: Collect data
    _data_collection.run()

    # Step 2: Preprocess data
    _data_preprocessing.run()

    # Step 3: Train the model
    _model_training.run()

    # Step 4: Evaluate the model
    _model_evaluation.run()

    # Step 5: Make predictions
    _prediction.run()