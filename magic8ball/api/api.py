import random

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "index"

@app.route("/answer")
def answer():
    list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    rand = random.Random()
    index = rand.randint(0, len(list) - 1)
    return list[index]

if __name__ == "__main__":
    app.run()
