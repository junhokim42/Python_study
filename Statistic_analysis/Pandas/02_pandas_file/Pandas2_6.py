import googlemaps
import pandas as pd

my_key = "AIzaSyDy81EbO46BRSnX1DOgg_xxxxxxxxxxx"

maps = googlemaps.Client(key=my_key)

lat = []
lng = []

places = ['서울시청', '국립국악원', '해운대해수욕장', '칭화대학', '자유의여신상']

i = 0
for place in places:
    i = i + 1
    try:
        print(i, place)
        geo_location = maps.geocode(place)[0].get('geometry')
        lat.append(geo_location['location']['lat'])
        lng.append(geo_location['location']['lng'])
    except:
        lat.append('')
        lng.append('')
        print(i)

df = pd.DataFrame({'위도':lat, '경도': lng}, index = places)
print('\n')
print(df)