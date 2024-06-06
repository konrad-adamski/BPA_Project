from functools import partial
import json

from src.MQTT_Camera import MQTTClient
from src.OPC_UA_Subscriber_AssemplyLine import OPC_UA_Subscriber
from src.utils.Logger import SingletonLogger


class InspectionHandler:
    def __init__(self):
        self.logger = SingletonLogger()
        self.opcua_subscriber = OPC_UA_Subscriber(self.logger)
        self.mqtt_client = MQTTClient(self.logger)

    def connect(self):
        self.mqtt_client.connect()
        self.opcua_subscriber.connect()

    def disconnect(self):
        self.opcua_subscriber.disconnect()
        self.mqtt_client.disconnect()

    def get_inspection_response(self, inspection_plan):
        camera_response = self.mqtt_client.request_response_cv(message="Triggering Camera", timeout=2)
        print("Kamera Informationen:")
        print(json.dumps(camera_response, indent=4))

        # TODO: Verarbeitung
        inspection_response = camera_response

        return inspection_response

    def run(self):
        # Erstellen eines gebundenen Callbacks, der self enthält
        bound_get_inspection_response = partial(self.get_inspection_response)

        # Callback mit gebundenem self registrieren
        self.opcua_subscriber.handler.register_callback(bound_get_inspection_response)

        try:
            self.opcua_subscriber.run()
        except Exception as e:
            print(f"An exception occurred: {e}")

    def main(self):
        self.connect()
        try:
            self.run()
        finally:
            self.disconnect()


if __name__ == "__main__":
    handler = InspectionHandler()
    handler.main()