from opcua import ua, Server
import time
import threading

from src.utils.util_functions import get_rfid_forSimulation

url = "opc.tcp://0.0.0.0:4840"  # replace with the actual IP address of the OPCUA server
node = "RFID-Reader_Data"


server = Server()
server.set_endpoint(url)

name = "BMWFactory"
addspace = server.register_namespace(name)

objects = server.get_objects_node()

auto_id_obj = objects.add_object(addspace, node)
auto_id = auto_id_obj.add_variable(addspace, node, "No Data")
auto_id.set_writable()


def input_listener():
    while True:
        new_auto_id = input("Enter new car ID: ")
        rfid_string = get_rfid_forSimulation(new_auto_id)
        auto_id.set_value(rfid_string)
        print(rfid_string + " published to OPC UA server")


if __name__ == '__main__':
    server.start()
    print(f"Server started at {url}")
    try:
        input_thread = threading.Thread(target=input_listener)
        input_thread.daemon = True
        input_thread.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Server stopping...")
    finally:
        server.stop()
        print("Server stopped")
