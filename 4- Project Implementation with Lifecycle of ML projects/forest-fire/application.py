import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

## import ridge regression and standard scaler pkl
ridge_model = pickle.load(open('models/ridge.pkl','rb'))
standard_scaler = pickle.load(open('models/scaler.pkl','rb'))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predictdata",methods=['GET','POST'])
def predict_data():
    if request.method == "POST":
        Temperature = float(request.form.get("Temperature"))
        RH = float(request.form.get("RH"))
        Ws = float(request.form.get("Ws"))
        Rain = float(request.form.get("Rain"))
        FFMC = float(request.form.get("FFMC"))
        DMC = float(request.form.get("DMC"))
        ISI = float(request.form.get("ISI"))
        Classes = float(request.form.get("Classes"))
        Region = float(request.form.get("Region"))

        new_data = [[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]] ## Convert value taken out of form into 2D format

        new_data_scaled = standard_scaler.transform(new_data) 
        results = ridge_model.predict(new_data_scaled) ## results as NumPy array 

        return render_template("home.html",result=results[0])
    else:
        return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True) ## flask app accesible from any device on the network interfaces instead of only localhost
    ## app is accessible from: Your computer, Other computers on same WiFi, Mobile phone on same WiFi

