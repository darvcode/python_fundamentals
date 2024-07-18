import requests

# Define the city for which to fetch weather information
city = 'Dallas'

# Construct the API URL with the city and your API key
url = 'http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=' + city + '&aqi=no'

# Make an HTTP GET request to fetch the weather data
response = requests.get(url)

# Parse the JSON response
weather_json = response.json()

# Extract the temperature in Fahrenheit
temp = weather_json.get('current').get('temp_f')

# Extract the weather description
description = weather_json.get('current').get('condition').get('text')

# Print the current weather information
print('Today in', city, 'is a', description, 'day and', temp, 'degrees')
