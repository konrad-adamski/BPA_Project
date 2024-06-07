from src.OPC_UA_Subscriber_AssemplyLine import OPC_UA_Subscriber

subscriber = OPC_UA_Subscriber()
subscriber.connect()
subscriber.run()
subscriber.disconnect()


