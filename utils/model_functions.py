from ultralytics import YOLO
#from sendemail import send_email

# Load a YOLO model with specified weights file
def load_model(weights):
    return YOLO(weights)

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