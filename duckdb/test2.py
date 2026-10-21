from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="tourism_project")

location = geolocator.geocode("Victoria Memorial, Kolkata")

print(location.latitude)
print(location.longitude)