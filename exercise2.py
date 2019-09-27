# Name: YOUR NAME HERE 
# Assignment title: ENTER ASSIGNMENT TITLE HERE.
# Time to complete: ENTER YOUR TIME HERE.
# Description: ENTER A DESCRIIPTION ABOUT WHAT YOUR CODE IS SUPPOSED TO DO HERE.

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
for day in forecast_list:
    day = day.replace('\n',': ')
    # add your code here
    print day
