from ultralytics import YOLO

# Load a YOLO model with specified weights file
def load_model(weights):
    return YOLO(weights)

# Object detection
def detection(model, image):
    # Run inference with the YOLO model on the specified image
    results = model(image, save=True, save_crop=True)

    # If object detected
    if results[0].boxes:
        # Show object
        results[0].show()
        confirm = input("""Press Y to confirm there's a fire in the image: """).capitalize
        
        if confirm == "Y":
            print("""Fire was detected.
                  We're going to warn your correspondent security organisation immediately.
                  Please stay safe.""")
            #send_email(image)
        else:
            print("False positive.")

# Load weights file
weights = r"data/models/IgnisCV.pt"

# Load an image to check possible fire
image = r"data/fire_test.jpg"

# Create model object
model = load_model(weights)

# Object detection
detection(model, image)