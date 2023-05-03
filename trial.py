#!/usr/bin/env python3
import requests
import json

# Load the dictionary of cities and places
with open('cities_and_places.json', 'r') as file:
    cities_and_places = json.load(file)

# Create a dictionary to store the geocoded data
geocoded_data = {}

# Loop over each city and its associated places
for city, places in cities_and_places.items():
    # Loop over each place
    for place in places:
        # Construct the query string to geocode the place
        query = f'{place}, {city}, USA'
        print(query)
        url = f'https://nominatim.openstreetmap.org/search/{query}?format=json&limit=1'

        # Send a GET request to the Nominatim API
        response = requests.get(url)

        # Parse the JSON response
        data = response.json()

        # Check if the response contains any data
        if data:
            # Extract the latitude and longitude
            lat = data[0]['lat']
            lon = data[0]['lon']

            # Store the data in the geocoded_data dictionary
            if city in geocoded_data:
                geocoded_data[city][place] = {'latitude': lat, 'longitude': lon}
            else:
                geocoded_data[city] = {place: {'latitude': lat, 'longitude': lon}}

# Write the geocoded data to a JSON file
with open('geocoded_data.json', 'w') as file:
    json.dump(geocoded_data, file)
