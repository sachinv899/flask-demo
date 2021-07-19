from flask import Flask,render_template
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('view.html')

@app.route("/getStudent")
def hello_world():
    x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
    return json.dumps(x)

app.run()