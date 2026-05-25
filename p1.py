import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle

# Load dataset
data = pd.read_csv("Heart_Disease_Prediction.csv")

# Check for missing values
print(data.isnull().sum())

# Prepare features and target
features = data[["Age", "Chest pain type", "BP", "Cholesterol", "Max HR", "ST depression", "Number of vessels fluro", "Thallium"]]
target = data['Heart Disease']

# Split the data
x_train, x_test, y_train, y_test = train_test_split(features, target, random_state=3136)

# Train the model
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Test the model and print results
y_pred = model.predict(x_test)
print(classification_report(y_test, y_pred))

# Save the trained model
with open("heartdiseaseprediction.model", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully.")
