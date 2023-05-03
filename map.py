#!/usr/bin/env python3

import folium

# Create a map object centered on the United States
map_usa = folium.Map(location=[37.6480, -110.6169], zoom_start=7)

# Display the map
map_usa.save("map_usa.html")
