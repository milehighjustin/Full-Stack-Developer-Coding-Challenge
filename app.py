from flask import Flask, request, jsonify
import json
app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

@app.route('/adduser/', methods=['POST'])
def add_user():
    req_data = request.get_json()
    if req_data:
        try:
            req_data['userfirst']
        except:
            return jsonify({
                "status": f"error",
                "message": f"Please include user's first name"
            })
        try:
            req_data['userlast']
        except:
            return jsonify({
                "status": f"error",
                "message": f"Please include user's last name"
            })
        try:
            req_data['useremail']
        except:
            return jsonify({
                "status": f"error",
                "message": f"Please include user's email"
            })
        try:
            req_data['userpass']
        except:
            return jsonify({
                "status": f"error",
                "message": f"Please include a strong password"
            })
        return jsonify({
            "Message": f"Welcome {req_data['userfirst']} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "error": "Invalid Request"
        })

@app.route('/')
def index():
    return "<h1>Welcomet to SpaceFlask 🚀</h1>"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)