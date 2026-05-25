import pickle

# Load the model
with open("heartdiseaseprediction.model", "rb") as f:
    model = pickle.load(f)

print("Model loaded successfully.")
