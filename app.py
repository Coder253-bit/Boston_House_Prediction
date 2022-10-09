import pickle
import json
import numpy as np
from flask import Flask, request, app, jsonify, url_for, render_template
import pandas as pd

app = Flask(__name__)
## Load the model

regmodel = pickle.load(open("regmodel.pkl", 'rb'))
scaler = pickle.load(open('scaling.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])

def predict_api():
    data = request.json['data']
    print(data)
    to_scale = np.array(list(data.values())).reshape(1,-1) 
    print(to_scale)
    new_data = scaler.transform(to_scale)

    # Prediction
    output = regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_output = scaler.transform(np.array(data).reshape(-1,1))
    print(final_output)
    output = regmodel.predict(final_output)[0]
    return render_template("home.html",prediction_text="The House price prediction is {}".format(output))

if __name__ == '__main__':
    app.run(debug=True)
    


