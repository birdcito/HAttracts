#!/usr/bin/env python3

# from bs4 import BeautifulSoup, SoupStrainer
# import requests as r

# # Create a list of state links to visit
# #for state in states:
# base_url = f'http://theshadowlands.net/places/alabama.htm'
# page = r.get(base_url)
# strainer = SoupStrainer('p')
# soup = BeautifulSoup(page.content, "html.parser", parse_only=strainer)

# # Find all the <font> tags with a color of #ff9900 (city names)
# cities = soup.find_all('font', {'color': '#ff9900'})

# # Loop over each city and find the locations within that city
# for city in soup.find_all('b'):
#     print(city.get_text())
#     locations = city.find_next_siblings('font', {'color': '#ff6666'})
#     for location in locations:
#         print('\t', location.get_text())

# for p in soup.find_all('b')[-1]:
#     p.decompose()


# use BeautifulSoup to filter by common denominator/tag
# print soup first to test
#print(soup)

from bs4 import BeautifulSoup, SoupStrainer
import requests as r
import re

# Define regular expressions for matching city names and place descriptions
city_regex = r'<font color="#ff9900">([^<]+)'
place_regex = r'<font color="#ff6666">([^<]+)</font>(.+?)<br>'

# Create a list of state links to visit
state_links = ['http://theshadowlands.net/places/alabama.htm']

# Create a dictionary to store the parsed information
cities = {}

for state_link in state_links:
    # Visit the state link and parse the content
    page = r.get(state_link)
    strainer = SoupStrainer('p')
    soup = BeautifulSoup(page.content, "html.parser", parse_only=strainer)

    # Find all matches for city and place information within the strainer object
    city_matches = re.findall(city_regex, str(soup))
    place_matches = re.findall(place_regex, str(soup))

    # Loop through the matches and add them to the dictionary
    for i, city_match in enumerate(city_matches):
        city_name = city_match.strip(" -")
        city_places = []

        # Find all places for the current city
        for place_match in place_matches:
            if place_match[0].startswith(city_name):
                place_name = place_match[0].replace(city_name, "").strip()
                place_desc = place_match[1].strip()

                # Add the place to the current city's list of places
                city_places.append({"name": place_name, "description": place_desc})

        # Add the current city and its places to the dictionary
        cities[city_name] = city_places

print(cities)
