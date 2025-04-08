import pickle
from sklearn.metrics import accuracy_score
from ml.data_preprocessing import load_data, preprocess_data
from sklearn.model_selection import train_test_split

def evaluate_model():
    df = load_data()
    X, y = preprocess_data(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Load the model from the models folder
    with open('models/model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model Accuracy: {accuracy:.2f}")

if __name__ == '__main__':
    evaluate_model()
