from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from fuzzywuzzy import process
import pandas as pd
import numpy as np


class DocumentNY:
    phone = '16072352907'
    data = None

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming messages"""

    if DocumentNY.data is None:
        DocumentNY.data = load_data()
    # print(DocumentNY.data)
    input = request.form.getlist('Body')[0]
    # print(input)

    # Get Wage Theft information from DocumentNY Data
    search_result = search_data(input)

    # Text Message Response
    resp = MessagingResponse()
    resp.message(search_result)

    return str(resp)

def load_data():
    return pd.read_excel('./data/Wage theft all zipcodes NYC.xlsx')

def search_data(input):
    local_data = DocumentNY.data    # DataFrame Format
    list_trade_names = list(local_data['trade_nm'])
    best_match = process.extractOne(input,list_trade_names)[0]
    index = list_trade_names.index(best_match)
    relevant_data = local_data.iloc[index]
    print(relevant_data)

    num_violated_cases = relevant_data['case_violtn_cnt']
    cmp_assd_cnt = relevant_data['cmp_assd_cnt']   # civil money penalty assessed count

    resp_msg = "Trade Name: " + relevant_data['trade_nm'] + "\n" + \
                "Number of Violated Cases: %.2f\n" % num_violated_cases + \
                "Civil Money Penalty Assessed Count: %.2f" % relevant_data['cmp_assd_cnt']

    return resp_msg

if __name__ == "__main__":
    doc = DocumentNY()
    app.run(port='8080', debug=True)
