from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return "index"


@app.route("/answer")
def answer():
    question = request.args.get('question')
    eightball = eightball()
    return eightball.ask_question(question)


if __name__ == "__main__":
    app.run()
