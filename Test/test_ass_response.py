import json

from src.utils.util_ass_response import get_response_plan

with open('inspectionPlan.json', 'r') as file:
    inspection_plan_data = json.load(file)

with open('inspectionResponseSimplified.json', 'r') as file:
    inspection_response_simplified_data = json.load(file)


# Funktion aufrufen, um den 'Inspection_Plan'-Teil des Inspektionsplans zu durchlaufen
responsePlan = get_response_plan(inspection_plan_data, inspection_response_simplified_data)
print("____________________________________________________________________________________________________________")
print(json.dumps(responsePlan, indent=4))
