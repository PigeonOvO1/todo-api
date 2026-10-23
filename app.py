from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello,Flask!"

@app.route("/api/echo", methods = ["POST"])
def echo():
    data = request.get_json()
    return jsonify({"receiver":data})

if __name__ == "__main__":
    app.run(debug=True,port=5000)