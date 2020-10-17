import json

with open('MSOAs.txt', 'r') as read_file:
    msoas = json.load(read_file)

with open('Middle_Layer_Super_Output_Areas__December_2011__Boundaries.geojson', 'r') as read_file:
    uk_geojson = json.load(read_file)

lon_geojson = [x for x in uk_geojson['features'] if x['properties']['msoa11cd'] in msoas]
uk_geojson['features'] = lon_geojson

with open('lon_geojson.json', 'w') as write_file:
    json.dump(uk_geojson, write_file)