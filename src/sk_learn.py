import numpy as np
from typing import Any, Text
from pydantic import BaseModel
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_wine, load_iris, load_breast_cancer, load_digits

class ScikitLearningConfig(BaseModel):
    dataset: Any = load_wine()

class ScikitLearning(ScikitLearningConfig):
    def __init__(self, dataset_name: Text = 'wine') -> None:
        super().__init__()
        self.dataset = self.load_data(dataset_name)

    def load_data(self, name: Text) -> Any:
        if name == 'wine':
            return load_wine()
        elif name == 'iris':
            return load_iris()
        elif name == 'breast_cancer':
            return load_breast_cancer()
        elif name == 'digits':
            return load_digits()
        else:
            return None

    def __call__(self):
        return self.dataset

def train_and_test(dataset_name: str = 'wine'):
    # Load the dataset
    app = ScikitLearning(dataset_name=dataset_name)
    dataset = app()

    # Extract features (X) and labels (y)
    X = dataset['data']
    y = dataset['target']

    # Split data into training and testing sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Train a logistic regression model
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)

    # Predict on the test set
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    print("Accuracy on the test set:", accuracy)

def main():
    train_and_test(dataset_name='wine')

if __name__ == '__main__':
    main()
