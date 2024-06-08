import json

from src.utils.util_camera_inspection_response import get_simplified_inspection_response, get_value

# Gegebene JSON-Struktur als Dictionary
with open('inspectionResponse.json', 'r') as file:
    data = json.load(file)

simplified_inspection_response = get_simplified_inspection_response(data, schwellwert=0.6)
print(json.dumps(simplified_inspection_response, indent=4))

with open('inspectionResponseSimplified.json', 'w') as file:
    json.dump(simplified_inspection_response, file, indent=4)


print("_____________________________________________________________________________")

front_bumper_in_place = get_value(simplified_inspection_response, 'front_bumper', "in_place")
print(f"front_bumper_in_place: {front_bumper_in_place}")