# Usage example:
import json

from src.MQTT_Camera import MQTTClient
from src.utils.Logger import SingletonLogger

logger = SingletonLogger()

mqtt_client = MQTTClient(logger)
mqtt_client.connect()  # Establish connection

response = mqtt_client.request_response_cv(message="Triggering Camera", timeout=2)

print(json.dumps(response, indent=4))

mqtt_client.disconnect()
