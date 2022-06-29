import main_run
from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def chatbot_response():
    msg = request.form["msg"]
    return main_run.chatres(msg)


if __name__ == "__main__":
    app.run()