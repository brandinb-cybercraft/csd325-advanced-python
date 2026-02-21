import requests

url = "http://api.open-notify.org/astros.json"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print("\nRaw JSON Response:")
print(data)

print("\nFormatted Output:")
print("Number of astronauts in space:", data["number"])
print("People currently in space:")

for person in data["people"]:
    print("-", person["name"], "on", person["craft"])

print("\n==============================")
print("Dog API Example")
print("==============================")

dog_url = "https://dog.ceo/api/breeds/image/random"

dog_response = requests.get(dog_url)

print("Status Code:", dog_response.status_code)

print("\nRaw Response:")
print(dog_response.text)

dog_data = dog_response.json()

print("\nFormatted Output:")
print("Random Dog Image URL:", dog_data["message"])
print("Request Status:", dog_data["status"])

print("\n==============================")
print("Weather API Example")
print("==============================")

weather_url = "https://api.open-meteo.com/v1/forecast?latitude=47.6&longitude=-122.3&current_weather=true"

weather_response = requests.get(weather_url)

print("Status Code:", weather_response.status_code)

print("\nRaw Response:")
print(weather_response.text)

weather_data = weather_response.json()

print("\nFormatted Output:")
current = weather_data["current_weather"]

print("Temperature:", current["temperature"])
print("Wind Speed:", current["windspeed"])
print("Wind Direction:", current["winddirection"])