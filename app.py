from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_nia_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        Prgenencies= int(request.form['Prgenencies'])
        Glucoose=float(request.form['Glucoose'])
        Blood_Pressure=int(request.form['Blood_Pressure'])
        #Kms_Driven2=np.log(Kms_Driven)
        Skin_Thickness=int(request.form['Skin_Thickness'])
        Insulin=int(request.form['Insulin'])
        BMI=float(request.form['BMI'])
        Diabetesconstant=float(request.form['Diabetesconstant'])
        Age=int(request.form['Age'])
        
        
        prediction=model.predict([[Prgenencies,Glucoose,Blood_Pressure,Skin_Thickness,Insulin,BMI,Diabetesconstant,Age]])
        #output=r(prediction[1],2)
        if prediction==2:
            return render_template('index.html',prediction_texts="Invalid inputs {}".format(prediction) ) 
        elif prediction ==1:
            return render_template('index.html',prediction_text= "Sorry you have diabetes {}".format(prediction))  
        else:
            return render_template('index.html',prediction_text= "Congratulations you dont't have diabetes {}".format(prediction))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)