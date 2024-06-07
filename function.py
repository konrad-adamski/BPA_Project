import json


# OPCU ID to AutoID
def get_auto_id(rfid):
    # JSON-Datei einlesen
    with open('src/utils/config.json', 'r') as file:
        data = json.load(file)

    # Durchsuchen aller Einträge im Dictionary
    for model, details in data.items():
        # Überprüfen, ob die RFID im aktuellen Modell vorhanden ist
        if any(d.get('RFID') == rfid for d in details):
            # Extrahieren der AutoID, wenn die RFID gefunden wird
            auto_id = next((d.get('AutoID') for d in details if 'AutoID' in d), None)
            return auto_id
    return "-1"