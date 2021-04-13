import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('input_design.html')

@app.route('/predict',methods=['POST'])
def predict():
    a=request.form['male']
    b=request.form['age']
    c=request.form['currentSmoker']
    d=request.form['cigsPerDay']
    e=request.form['prevalentHyp']
    f=request.form['totChol']
    g=request.form['sysBP']
    h=request.form['diaBP']
    i=request.form['BMI']
    j=request.form['heartRate']
    k=request.form['glucose']
    prediction = model.predict([[a,b,c,d,e,f,g,h,i,j,k]])
    #output='{0:.{1}f}'.format(prediction[0][1], 2)
    
    if prediction[0]==0:
        r="You are at risk!"
    else:
        r="You are not at risk!"

    return render_template('output_design.html',prediction_text=r)

if __name__ == "__main__":
    app.run(debug=True)