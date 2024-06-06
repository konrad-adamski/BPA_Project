import json

from src.utils.AASManager import AASManager
from src.utils.Logger import SingletonLogger

logger = SingletonLogger()

ass_manager = AASManager(logger)
inspectionPlan = ass_manager.get_inspection_plan("BMW_M4")
print(json.dumps(inspectionPlan, indent=4))

print("\n---------------------------------------------------\n")
inspectionResponse = ass_manager.get_inspection_response("BMW_M4")
print(json.dumps(inspectionResponse, indent=4))

print("\n---------------------------------------------------\n")

json_context = {
    "test": 1,
    "test2": 2,
    "new": 3
}

ass_manager.put_inspection_response("BMW_M4", json_context)
