from flask import Flask, request, jsonify
import json
import mysql.connector as mysql
import bcrypt
import secrets
import os

app = Flask(__name__)

db = mysql.connect(
            host = os.getenv('DBHOST'),
            user = os.getenv('DBUSER'),
            passwd = os.getenv('DBPASS'),
            database = os.getenv('DBNAME')
        )

def getuserbyemail(email):
    try:
        cursor = db.cursor(buffered=True)
        query = "SELECT * from users WHERE email = %s"
        values = (email, )
        cursor.execute(query, values)
        return cursor.fetchone()
    except:
        return "error"

def createtoken(user):
    token = secrets.token_hex(20)
    query = "INSERT into tokens (userid, token) VALUES (%s, %s)"
    values = (user, token)
    cursor = db.cursor(buffered=True)
    cursor.execute(query, values)
    db.commit()
    return token

@app.route('/refreshdata/', methods=['GET'])
def refresh_data():
    fileObject = open("alerts.json", "r")
    jsonContent = fileObject.read()
    jsonObj = json.loads(jsonContent)
    for alert in jsonObj:
        query = "INSERT into alerts (errorId, errorSeverity, errorCategory, errorMessage, longMessage, errorTime, selected, new, expanded) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (alert['errorId'], alert['errorSeverity'], alert['errorCategory'], alert['errorMessage'], alert['longMessage'], alert['errorTime'], alert['selected'], alert['new'], alert['expanded'])
        cursor = db.cursor(buffered=True)
        cursor.execute(query, values)
        db.commit()
    fileObject2 = open("contacts.json", "r")
    jsonContent = fileObject2.read()
    jsonObj = json.loads(jsonContent)
    for contact in jsonObj:
        query = "INSERT into contacts (_id, contactId, contactStatus, contactName, contactGround, contactSatellite, contactEquipment, contactState, contactStep, contactDetail, contactBeginTimestamp, contactEndTimestamp, contactLatitude, contactLongitude, contactAzimuth, contactElevation, contactResolution, contactResolutionStatus) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (contact['_id'], contact['contactId'], contact['contactStatus'], contact['contactName'], contact['contactGround'], contact['contactSatellite'], contact['contactEquipment'], contact['contactState'], contact['contactStep'], contact['contactDetail'], contact['contactBeginTimestamp'], contact['contactEndTimestamp'], contact['contactLatitude'], contact['contactLongitude'], contact['contactAzimuth'], contact['contactElevation'], contact['contactResolution'], contact['contactResolutionStatus'])
        cursor = db.cursor(buffered=True)
        cursor.execute(query, values)
        db.commit()



@app.route('/login/', methods=['POST'])
def login_user():
    req_data = request.get_json()
    if req_data:
        try:
            record = getuserbyemail(req_data['useremail'])
            storedpw = record[4]
            if(bcrypt.checkpw(req_data['userpass'].encode(), storedpw.encode())):
                return jsonify({
                    "status": f"success",
                    "message": createtoken(record[0])
                })
            else:
                return jsonify({
                    "status": f"error",
                    "message": f"Invalid Login"
                })
        except:
            return jsonify({
                "status": "Invalid Login"
            })
    else:
        return jsonify({
            "status": f"error",
            "message": f"Invalid Request"
        })


@app.route('/adduser/', methods=['POST'])
def add_user():
    req_data = request.get_json()
    if req_data:
        try:
            userf = req_data['userfirst']
        except:
            return jsonify({
                "status": "error",
                "message": "Please include user's first name"
            })
        try:
            userl = req_data['userlast']
        except:
            return jsonify({
                "status": "error",
                "message": "Please include user's last name"
            })
        try:
            useremail = req_data['useremail']
        except:
            return jsonify({
                "status": "error",
                "message": "Please include user's email"
            })
        try:
            userpass = req_data['userpass']
        except:
            return jsonify({
                "status": "error",
                "message": "Please include a strong password"
            })
        # We good
        hashpw = bcrypt.hashpw(userpass.encode(), bcrypt.gensalt())
        cursor = db.cursor()
        query = "INSERT into users (userf, userl, email, password) VALUES (%s, %s, %s, %s)"
        values = (userf, userl, useremail, hashpw)
        cursor.execute(query, values)
        db.commit()
        getuser = getuserbyemail(useremail)
        token = createtoken(getuser[0])
        return jsonify({
            "status": "success",
            "message": token
        })

    else:
        return jsonify({
            "error": "Invalid Request"
        })

@app.route('/')
def index():
    return "<h1>Welcome to SpaceFlask 🚀</h1>"

if __name__ == '__main__':
    app.run(threaded=True)