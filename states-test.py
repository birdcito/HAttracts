#!/usr/bin/env python3
import requests as r
from bs4 import BeautifulSoup as bs, SoupStrainer as Strain
import json

states = ["alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut", 
          "delaware", "florida", "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa", 
          "kansas", "kentucky", "louisiana", "maine", "maryland", "massachusetts", "michigan",
          "minnesota", "mississippi", "missouri", "montana", "nebraska", "nevada", "newhampshire",
          "newjersery", "newmexico", "newyork", "northcarolina", "northdakota", "ohio", "oklahoma",
          "oregon", "pennsylvania", "rhodeisland", "southcarolina", "southdakota", "tennessee",
          "texas", "utah", "vermont", "virginia", "washington", "westvirginia", "wisconsin", "wyoming"]

# Create a list of state links to visit
#for state in states:
base_url = f'http://theshadowlands.net/places/alabama.htm'
page = r.get(base_url)
strainer = Strain('p')
soup = bs(page.content, "html.parser", parse_only=strainer)

# Extract the location and name data for each state
state_data = []
# loop to find all <b> tags in html doc
for tag in soup.find_all('b'):
    # loop to filter the data down based on city names ending in '-' in html doc
    for text in tag.strings:
        # conditional to strip the '-' at the end of "significant point" strings
        if text.endswith('- '):
            text = text.strip(' - ')
            # replacing remaining '-' and '\n' characters to set into JSON dictionary
            new_text = text.replace('- ', '')
            filtered_text = new_text.replace('\n', ' ')
            if '""' not in filtered_text:
                state_data.append({'text': filtered_text})

with open('rawjsonoutput.json', 'w') as file:
    json.dump(state_data, file)

        
