from flask import Flask, request, jsonify
from jsonrpcserver import dispatch, result
from ChatBot import chatBot
from Handlers import *
from Cache import *
from db import DB

app = Flask(__name__)
db = DB()
CHATBOT = chatBot()

@app.route('/post_json', methods=['POST'])
def process_json():
    data = request.get_json()
    CHATBOT = chatBot()
    loc = data["location"]
    hit, det_resp = checkCache(loc ,db)
    if not hit:
        det_resp = handleDetails(loc, CHATBOT)
        db.write(loc, det_resp)
    loc, month, day = data["location"], data["month"], data["day"]
    iter_resp = handleIternary((loc, day, month), CHATBOT)
    resp = mergeResponse(iter_resp, det_resp)
    return jsonify(resp)

if __name__ == "__main__":
    app.run()

