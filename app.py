import random
import os
from flask import Flask, request, jsonify
import json
import numpy as np



app = Flask(__name__)

array1 = []

@app.route("/",methods=["GET"])
def func():
    return "ciao"

@app.route("/predict", methods=["POST"])
def predict():
    #get audio file and save it
    data1 = request.json
    
    row = json.loads(data1)["data"]
    arr = row.split("@")
    
    array1.append(arr)

    np.savetxt("provacsv.csv",
           array1,
           delimiter =", ",
           fmt ='% s')
    
    return "ciao"

if __name__ == "__main__" :
    app.run(debug=False, host= '0.0.0.0')
    #app.run(port=5000, debug=False)
