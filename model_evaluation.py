from utils.model_functions import load_model

# Load weights file
weights = r"data/weights/best_weights.pt"

# Create model object
model = load_model(weights)

# Model evaluation
model.val()