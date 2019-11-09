from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import pandas as pd
import numpy as np


class DocumentNY:
    phone = '16072352907'
    data = None

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hello World"

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming messages"""

    if DocumentNY.data is None:
        DocumentNY.data = load_data()
    print(DocumentNY.data)
    input = request.form.getlist('Body')[0]
    print(input)
    # Start our response
    resp = MessagingResponse()

    # Return data as a response
    resp.message("You texted us: '" + input + "'")

    return str(resp)

def load_data():
    return pd.read_excel('./data/Wage theft all zipcodes NYC.xlsx')

if __name__ == "__main__":
    doc = DocumentNY()
    app.run(port='8080', debug=True)
