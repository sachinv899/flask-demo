from flask import Flask
import json

app = Flask(__name__)

@app.route("/getStudent")
def hello_world():
    x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
    return json.dumps(x)

app.run()