
from flask import Flask, request, json, jsonify,send_file
from flask_pymongo import PyMongo
from bson import json_util
from flask_cors import CORS
import json
import datetime
import jwt


# from report import report


def parse_json(data):
    return json.loads(json_util.dumps(data))


app=Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/EmailCo"
app.config["SECRET_KEY"] ="flow@master#alphaV1$%^#&@672"

mongo  = PyMongo(app)
CORS(app)

@app.route("/make/appointment",methods=["POST"])
def make_appointment():
    try:
        data  = request.get_json("data")
        print(data)


    except Exception as e  :
        print("ERROR:on /make/appointment",e)




if __name__  =="__main__":
    app.run(debug=True)