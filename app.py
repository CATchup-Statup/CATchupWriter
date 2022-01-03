import random
import os
from flask import Flask, request, jsonify
import json
import numpy as np



app = Flask(__name__)

array1 = []

#Default route
@app.route("/",methods=["GET"])
def func():
    return "ciao"

#Route Predict 
@app.route("/predict", methods=["POST"])
def predict():
    #access to data in the post request
    data1 = request.json
    #Transform data in json format
    row = json.loads(data1)["data"]
    #Extract the 7 parameters
    arr = row.split("@")
    #Add parameters to the global array
    array1.append(arr)
    #Write the global array in local ssd
    np.savetxt("provacsv.csv",
           array1,
           delimiter =", ",
           fmt ='% s')
    #Return a confirmation status
    return "Tutto ok"

#Flask default configuration
if __name__ == "__main__" :
    #0.0.0.0 is the default location (if the client is not che same machine see the ip of the server)
    app.run(debug=False, host= '0.0.0.0')
    #app.run(port=5000, debug=False)
