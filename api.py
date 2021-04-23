from flask import Flask, request, redirect, url_for, flash, jsonify
import pandas as pd
import json
from firebase import firebase

app = Flask(__name__)

fb = firebase.FirebaseApplication('https://historicaldatafyp-default-rtdb.firebaseio.com/', None)

@app.route('/getlastval/', methods=['GET'])
def getlastval():
  ticker = request.args['Ticker']
  vals = fb.get('historicaldatafyp-default-rtdb/Stocks/'+ticker,'')
  df = pd.DataFrame(vals)
  return df.tail(1).T.to_dict()

@app.route('/get30val/',methods=['GET'])
def get30val():
  ticker = request.args['Ticker']
  vals = fb.get('historicaldatafyp-default-rtdb/Stocks/'+ticker,'')
  df = pd.DataFrame(vals)
  return df.tail(30).values

'''if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', use_reloader=False)'''
