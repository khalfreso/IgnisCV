from utils.model_functions import load_model, detection

# Load weights file
weights = r"data/weights/best_weights.pt"

# Load an image to check possible fire
image = r"data/fire_test.jpg"

# Create model object
model = load_model(weights)

# Object detection
detection(model, image)