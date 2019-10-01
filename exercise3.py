# Name: Miles Van Denburg
# Assignment title: Python Exercise 3 
# Time to complete: 20 minutes
# Description: The code splits the longitude and latitude values within the scraped URL and prints out the longitude and latitue results. 


#url with latitude and longitude information
url = 'https://www.google.com/maps/@42.2509428,-71.8249939,17z.'

#splitter function which separates the url based on the @ symbol and stores the list in splitter
#splitter1 takes the converted string values of splitter
#splitter 2 takes a split list of the elements from splitter1 now split by the "," value
#long takes the longitude value stored in splitter 2 which is cleaned by the replace method
#lat takes the latitude value stored in the splitter2 list at index [2]
#print returns the values and separates them by a line
#the funciton is then called at the end with the argument of 'url' defined above the function code

def splitterFunct(x):
  splitter = x.split("@")
  splitter1  = str(splitter)
  splitter2 = splitter1.split(",")
  long = splitter2[1].replace("'", "")
  lat = splitter2[2]
  print("Longitude: " + long + "\n" + "Latitude: " + lat)
  
splitterFunct(url)
