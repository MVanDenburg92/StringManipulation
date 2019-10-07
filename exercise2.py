# Name: Miles Van Denburg 
# Assignment title: Lab 5 Part 2
# Time to complete: 20 min
# Description: The code cleans the scraped data from the National Weather Service by removing extra whitespace, lines, and inserts spaces/commas where needed bewteen capitalized words. 

# -*- coding: utf-8 -*-
# Keep the line above when running script
# Tells python what encoding the string is stored in

# Scraped multi-line String
forecast = '''

Tonight
ClearLow: 55 F

Thursday
Sunny thenChanceShowersHigh: 77 F

Friday
SunnyHigh: 73 F

Saturday
Mostly SunnyHigh: 77 F

Sunday
Mostly SunnyHigh: 71 F
'''

# Split string into a list
# Use two blank lines (\n\n) as the separator
# Creates a list item at every instance of separator
forecast_list = forecast.split('\n\n')

# Loop through list to make string replacements to each item
# Remove extra whitespaces or lines for a cleaner format
# Separates Capitalized words and inserts a comma to separate the values
for day in forecast_list:
    day = day.replace('\n',': ')
    # You don't necessarily have to create new variables for replacements
    # You can update the existing string
    day2 = day.replace("SunnyHigh", "Sunny, High")
    day3 = day2.replace("thenChanceShowersHigh", "then Chance Showers, High")
    day4 = day3.replace("ClearLow", "Clear, Low")
    print day4
