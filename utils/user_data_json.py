import json
from geolocation import get_gps_coordinates
from pathlib import Path

location, [latitude, longitude] = get_gps_coordinates()

user = "Khalfreso"

data = {
    "Username": user,
    "E-mail": f"email_{user}@gmail.com",
    "Location": location,
    "GPS coordinates": [latitude, longitude],
    "Emergency contact e-mail": "email_emergency@gmail.com"
}

# Current file's directory (utils/)
root_dir = Path(__file__).resolve().parent.parent

json_data = json.dumps(data, indent=4)
with open(root_dir / "data" / "user_data" / f"{data["Username"]}_data.json", "w") as f:
    f.write(json_data)