import requests
import json

# Set up the parameters we want to pass to the API
# This is the latitude and longitude of New York City
parameters = {"lat": 40.71, "lon": -74}

# Make a get request with the parameters
response = requests.get("http://api.open-notify.org/astros.json")

# Converts the json string into its original format, a dictionary
data = response.json()

# prints the value of the key "number", which is the number of people in space
print(data["number"])

# prints the entire value of the json dict
print(data)
