from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route("/")
def hello():
    deta = {
        "name": "keisuke",
        "age": 32,
        "message": "Hello API"
    }
    return jsonify(deta)


if __name__ == "__main__":
    app.run(debug=True)
