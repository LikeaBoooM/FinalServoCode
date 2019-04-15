import os
import googlemaps
import elevation
gmaps = googlemaps.Client(key='AIzaSyBR-gJMNHXBhXZzdPauNAbtUZj0QfXLAAg')
APIKEY = "AIzaSyBR-gJMNHXBhXZzdPauNAbtUZj0QfXLAAg"

def evalute(long, latitiude):
    result = gmaps.elevation([(long, latitiude)])
    return(result[0]['elevation'])
