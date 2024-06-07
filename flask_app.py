from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def view_logs():
    with open("app.log", "r") as file:
        logs = file.read()
    return render_template("logs.html", logs=logs)


if __name__ == '__main__':
    app.run()
