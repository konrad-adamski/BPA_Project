from flask import Flask
from src.InspectionHandler import InspectionHandler
import threading
from app_webserver import webserver_bp


def run_handler():
    handler = InspectionHandler()
    handler.connect()
    # Logik zur Ausführung des Handlers hinzufügen


# Flask-Anwendung
def create_app():
    app = Flask(__name__)

    app.register_blueprint(webserver_bp, url_prefix='')

    # Starte den Handler in einem separaten Thread
    handler_thread = threading.Thread(target=run_handler)
    handler_thread.start()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
