from flask import Flask, request, jsonify
from flask_cors import CORS
from chat.chatbot import chatBot
from database.db import DB
from database.cache import *
from database.handlers import *

app = Flask(__name__)
CORS(app)
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
    app.run(host = "0.0.0.0")

