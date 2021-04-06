from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from utils import get_message

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    msg = request.form.get('Body')
    reply = get_message(msg)
    resp = MessagingResponse()

    resp.message(str(reply))
    return str(resp)

if __name__=='__main__':
    app.run(debug=True)
