import sys
import requests
import json
from conf import maps_api_key

url = f'https://maps.googleapis.com/maps/api/geocode/json?key={maps_api_key}&address='

with open(sys.argv[1]) as f:
    content = f.readlines()
content = [x.strip() for x in content]

lats = []
longs = []

for arg in content:
    arg = arg.replace(" ", "%20")
    results = requests.get(url + arg).json()
    lat_long = results['results'][0]['geometry']['location']
    lats.append(lat_long['lat'])
    longs.append(lat_long['lng'])

lat_sum:float = 0.0
lat_count = 0
long_sum:float = 0.0
long_count = 0

for lat in lats:
    lat_sum += float(lat)
    lat_count += 1

for lng in longs:
    long_sum += float(lng)
    long_count += 1

avg_lat = lat_sum/float(lat_count)
avg_long =long_sum/float(long_count)

print("avg_lat: " + str(avg_lat))
print("avg_long: " + str(avg_long))

reverse_geocode_url = f'https://maps.googleapis.com/maps/api/geocode/json?key={maps_api_key}&latlng='
arg = str(str(avg_lat) + ',' + str(avg_long))
reverse_results = requests.get(url + arg).json()
print(reverse_results['results'][0]['formatted_address'])