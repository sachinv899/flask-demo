from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def hello():
    if request.method == 'POST':
        return render_template('view.html')
    return render_template('view.html')
    

# @app.route("/getStudent",methods=['POST','GET'])
# def hello_world():
#     x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
#     return json.dumps(x)

if __name__ == "__main__":
    app.run(debug=True)