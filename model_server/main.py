from flask import Flask, request, jsonify
from jsonrpcserver import dispatch, result
from ChatBot import chatBot
from Handlers import *

app = Flask(__name__)

@app.route('/post_json', methods=['POST'])
def process_json():
    data = request.get_json()
    CHATBOT = chatBot()
    if data["call_type"] == "1":
        loc = data["location"]
        resp = handleDetails(loc, CHATBOT)
        print(resp)
    elif data["call_type"] == "0":
        loc, month, day = data["location"], data["month"], data["day"]
        resp = handleIternary((loc, day, month), CHATBOT)
        print(resp)
    else:
        return {}
    return resp
    return jsonify(resp)

if __name__ == "__main__":
    app.run()

