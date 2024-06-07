import json
from src.MQTT_Camera import MQTTClient


mqtt_client = MQTTClient()
mqtt_client.connect()  # Establish connection

response = mqtt_client.request_response_cv(message="Triggering Camera", timeout=2)

with open('inspectionResponse.json', 'w') as file:
    json.dump(response, file, indent=4)

print(json.dumps(response, indent=4))

mqtt_client.disconnect()
