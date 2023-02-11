from flask import Flask, request, json, jsonify,render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps
from bson import json_util
from flask_cors import CORS
import json

import datetime
from pymongo import MongoClient



def parse_json(data):
    return json.loads(json_util.dumps(data))


app=Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/School"

mongo  = PyMongo(app)
CORS(app)
def parse_json(data):
    return json.loads(json_util.dumps(data))


app=Flask(__name__)
CORS(app)

@app.route("/make/appointment",methods=["POST"])
def make_appointment():
    resp ={}
    status = 0
    try:
        data  = request.get_json("data")
        payload = data["data"]
        with open("./databases/appointment.json","r")as infile:
            data = json.load(infile)
            print(data)
            data["data"].append(payload)
            print(data["data"])
            with open("./databases/appointment.json","w")as outfile:
                new_data ={
                    "data":data["data"]
                }
                json.dump(new_data,outfile)
            resp  = {"message":"new appointment made ",status:200}
            status = 200


    except Exception as e  :
        print("ERROR:on /make/appointment",e)
    return jsonify(resp),status
@app.route("/get/appointment",methods=["POST"])
def get_appointment():
    resp ={}
    status = 0
    try:
        data  = request.get_json("data")
        user_id = data["user_id"]
        user_ap= []
        with open("./databases/appointment.json","r")as infile:
                data = json.load(infile)
                for i in data["data"]:
                    if i["user_id"] == user_id:
                        user_ap.append(i)
        resp ={
            "appointments":user_ap
        }
        status = 200
    except Exception as e  :
        print("ERROR:on /get/appointment",e)
    return jsonify(resp),status
@app.route("/appointment/reminder",methods=["GET"])
def appointment_reminder():
    resp ={}
    status = 0
    try:
        today = datetime.date.today()
        today_ap = []
        with open("./databases/appointment.json","r")as infile:
                data = json.load(infile)
                for i in data["data"]:
                    if i["date"] == today:
                        today_ap.append(i)
        resp ={
            "appointments":today_ap
        }
        status = 200

    except Exception as e  :
        print("ERROR:on /appointment/reminder",e)
    return jsonify(resp),status
@app.route("/make/user",methods=["POST"])
def make_user():
    resp ={}
    status = 0
    try:
        data  = request.get_json("data")
        payload = data["data"]
        with open("./databases/user.json","r")as infile:
            data = json.load(infile)
            print(data)
            data["data"].append(payload)
            print(data["data"])
            with open("./databases/user.json","w")as outfile:
                new_data ={
                    "data":data["data"]
                }
                json.dump(new_data,outfile)
            resp  = {"message":"new usermade ",status:200}
            status = 200


    except Exception as e  :
        print("ERROR:on /make/user",e)
    return jsonify(resp),status
@app.route("/get/user",methods=["POST"])
def get_user():
    resp ={}
    status = 0
    try:
        data  = request.get_json("data")
        user_id  = data["data"]["user_id"]
        user ={}
        with open("./databases/appointment.json","r")as infile:
                data = json.load(infile)
                for i in data["data"]:
                    if i["user_id"] == user_id:
                        user = i
         
        if user== {}:
            resp ={"mesasage":"Please sign up yto the platform"} 
            status  = 400
            return jsonify(resp),status
                        
        resp ={
            "user":user
        }
        status = 200


    except Exception as e  :
        print("ERROR:on /make/user",e)
    return jsonify(resp),status
@app.route("/get/contacts",methods=["GET"])
def get_contacts():
    resp ={}
    status = 0
    try:
        contacts  = []
        with open("./databases/appointment.json","r")as infile:
                data = json.load(infile)
                for i in data["data"]:
                    contacts.append(i)
                    
        resp ={
                "contacts ":contacts 
            }
        status = 200

    except Exception as e  :
        print("ERROR:on /get/contacts",e)
    return jsonify(resp),status

@app.route("/send/email",methods=["POST"])
def send_email():
    try:
        data  = request.get_json("data")
        print(data)


    except Exception as e  :
        print("ERROR:on /send/email",e)

@app.route("/send/email/nouser",methods=["POST"])
def send_email_nu():
    try:
        data  = request.get_json("data")
        print(data)


    except Exception as e  :
        print("ERROR:on /send/email",e)

@app.route("/send/email/invite",methods=["POST"])
def send_email_invite():
    try:
        data  = request.get_json("data")
        print(data)


    except Exception as e  :
        print("ERROR:on /send/email/invite",e)

if __name__  =="__main__":
    app.run(debug=True)