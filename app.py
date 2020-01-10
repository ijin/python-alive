from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "what's up?"

@app.route("/alive")
def alive():
    return "Number 5 is alive!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
