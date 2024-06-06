from flask import Blueprint, render_template

webserver_bp = Blueprint('webserver', __name__)


@webserver_bp.route("/")
def view_logs():
    with open("app.log", "r") as file:
        logs = file.read()
    return render_template("logs.html", logs=logs)
