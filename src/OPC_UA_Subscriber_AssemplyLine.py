import json
import time
import threading
from opcua import Client

from src.utils.AASManager import AASManager
from src.utils.Logger import SingletonLogger

OPCUA_URL_MOCKUP = "opc.tcp://localhost:4840"


class OPC_UA_Subscriber:
    def __init__(self, logger):
        self.logger = logger
        self.ass_manager = AASManager(self.logger)
        self.opcua_url = OPCUA_URL_MOCKUP
        self.latest_auto_id_lock = threading.Lock()
        self.latest_auto_id = None
        self.client = Client(self.opcua_url)
        self.sub = None
        self.handler = self.SubHandler(self)

    class SubHandler:
        def __init__(self, outer):
            self.outer = outer
            self.callback = None

        def datachange_notification(self, node, val, data):
            with self.outer.latest_auto_id_lock:
                self.outer.latest_auto_id = val
                print(f"Auto ID: {val}")
            inspection_plan = self.outer.ass_manager.get_inspection_plan(auto_id=val)

            # Aufrufen der Callback-Funktion, wenn sie existiert
            if self.callback:
                inspection_response = self.callback(inspection_plan)
                print("Inspection Response: ", inspection_response)

        def register_callback(self, callback):
            self.callback = callback

    def connect(self):
        try:
            self.client.connect()
            self.logger.info("Connected to OPC UA server")
            objects = self.client.get_objects_node()
            auto_id_obj = objects.get_child(["2:AutoID"])
            auto_id_node = auto_id_obj.get_child(["2:AutoID"])
            self.sub = self.client.create_subscription(100, self.handler)
            self.sub.subscribe_data_change(auto_id_node)
        except Exception as e:
            self.logger.exception(f"Error connecting to OPC UA server, error: {e}")
            self.disconnect()

    def run(self):
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.logger.info("Stopping OPC UA Subscriber.")

    def disconnect(self):
        if self.client:
            self.client.disconnect()
            self.logger.info("Disconnected from OPC UA server")

