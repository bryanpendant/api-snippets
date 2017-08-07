from flask import Flask, request
from twilio import twiml
from . import validate_twilio_request

app = Flask(__name__)


@app.route('/voice', methods=['POST'])
@validate_twilio_request
def incoming_call():
    """Twilio Voice URL - receives incoming calls from Twilio"""
    # Create a new TwiML response
    resp = twiml.Response()

    # <Say> a message to the caller
    from_number = request.values['From']
    body = """
    Thanks for calling!

    Your phone number is {0}. I got your call because of Twilio's webhook.

    Goodbye!""".format(' '.join(from_number))
    resp.say(body)

    # Return the TwiML
    return str(resp)


@app.route('/message', methods=['POST'])
@validate_twilio_request
def incoming_message():
    """Twilio Messaging URL - receives incoming messages from Twilio"""
    # Create a new TwiML response
    resp = twiml.Response()

    # <Message> a text back to the person who texted us
    body = "Your text to me was {0} characters long. Webhooks are neat :)" \
        .format(len(request.values['Body']))
    resp.message(body)

    # Return the TwiML
    return str(resp)


if __name__ == '__main__':
    app.run(debug=True)
