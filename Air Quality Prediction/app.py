# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'best_model.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        t = float(request.form['T'])
        tm = float(request.form['TM'])
        tmm = float(request.form['Tm'])
        slp = float(request.form['SLP'])
        h = float(request.form['H'])
        vv = float(request.form['VV'])
        v = float(request.form['V'])
        vm = float(request.form['VM'])
        
        data = np.array([[t, tm, tmm, slp, h, vv, v, vm]])
        my_prediction = classifier.predict(data)
        
        return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
	app.run(debug=True)