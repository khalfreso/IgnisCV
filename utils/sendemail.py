# Required email modules
import smtplib
from email.message import EmailMessage

# JSON module
import json

def send_email(image):
    # Load the json into a variable
    with open('Khalfreso_data.json', 'r') as f:
        data = json.load(f)

    # Email template
    msg = EmailMessage()

    msg['From'] = data["E-mail"]
    msg['To'] = data["Emergency contact e-mail"]
    msg['Subject'] = f"Dangerous fire detected at: {data["Location"]}, {data["GPS coordinates"]}"
    msg.set_content(f"""IgnisCV automatically detected a fire at:
                    {data["Location"]}, {data["GPS coordinates"]}.
                    The user confirmed themselves that the fire was dangerous and requires aid.
                    Attached is an image of the detected fire.
                    Please get in contact with the user as soon as possible.""")
    attachment = image

    with open(attachment, 'rb') as fp:
        img_data = fp.read()
    msg.add_attachment(img_data, maintype='image', subtype='jpg')

    # Send the message via a SMTP server (localhost by default)
    s = smtplib.SMTP('localhost', 1025)
    s.send_message(msg)
    s.quit()