import geocoder

def get_gps_coordinates():
    g = geocoder.ip('me')
    if g.latlng and g.city:
        return g.city, g.latlng
    else:
        print("Unable to retrieve your GPS coordinates.")
        return None, [None, None]