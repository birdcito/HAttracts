#!/usr/bin/env python3

import requests
import json

# Set up the OpenStreetMap API endpoint
OSM_API_ENDPOINT = "https://nominatim.openstreetmap.org/search"

# function to get user starting point
def get_location_coordinates(location):
    # Construct the URL for the API request
    url = f"{OSM_API_ENDPOINT}?q={location}&format=json"

    # Send the API request
    response = requests.get(url)

    # Parse the response JSON
    response_json = json.loads(response.text)

    # Get the latitude and longitude from the response
    lat = response_json[0]["lat"]
    lon = response_json[0]["lon"]

    return (lat, lon)

# Example usage
print("Enter your starting location")
location = input()
lat, lon = get_location_coordinates(location)
print(f"The coordinates of {location} are ({lat}, {lon})")
