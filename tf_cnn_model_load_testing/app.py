import numpy as np
from flask import Flask, request, jsonify, render_template
import flask
import h5py
app = Flask(__name__)
from model import predictor
import io

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/',methods=['POST'])
def predict():
    image=request.files["file"].read()
    image=io.BytesIO(image)

    result=predictor(image)

    return render_template('index.html', prediction_text='Prediction : {}'.format(result))




if __name__ == "__main__":
    app.run('127.0.0.1', port=5000,debug=True)
