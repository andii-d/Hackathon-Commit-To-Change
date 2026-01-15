from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/sms", methods=["POST"])
def sms():
    incoming = request.form.get("Body", "")
    resp = MessagingResponse()
    resp.message(f"Got it: {incoming}. What habit did you complete?")
    return str(resp)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
