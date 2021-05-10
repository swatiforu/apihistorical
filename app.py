from flask import Flask, request, redirect, url_for, flash, jsonify
import pandas as pd
import json
from firebase import firebase

app = Flask(__name__)

fb = firebase.FirebaseApplication('https://historicaldatafyp-default-rtdb.firebaseio.com/', None)

@app.route('/getlastval/', methods=['GET'])
def getlastval():
  with open('abc.txt','w') as file:
    file.write("123")
  with open('abc.txt', 'r') as file:
    lines = file.read()
    return lines
  """ticker = request.args['Ticker']
  vals = fb.get('historicaldatafyp-default-rtdb/Stocks/'+ticker,'')
  df = pd.DataFrame(vals)
  return df.tail(1).T.to_dict()"""

@app.route('/get30val/',methods=['GET'])
def get30val():
  ticker = request.args['Ticker']
  vals = fb.get('historicaldatafyp-default-rtdb/Stocks/'+ticker,'')
  df = pd.DataFrame(vals)
  return df.tail(30).T.to_dict()
