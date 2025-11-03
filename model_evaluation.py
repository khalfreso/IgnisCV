from utils.model_functions import load_model

# Load weights file
weights = r"data/models/IgnisCV.pt"

# Create model object
model = load_model(weights)

# Model evaluation
model.val()