from src.OPC_UA_Subscriber_AssemplyLine import OPC_UA_Subscriber
from src.utils.Logger import SingletonLogger

logger = SingletonLogger()

subscriber = OPC_UA_Subscriber(logger)
subscriber.connect()
subscriber.run()
subscriber.disconnect()


