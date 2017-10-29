import json

from flask import Flask

# Connect to Redis
app = Flask(__name__)

@app.route("/hello/<name>")
def hello(name):
    return json.dumps({"message": f"Hello {name.capitalize()}"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9001)

