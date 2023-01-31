from flask import Flask, request, render_template
import joblib
import requests
from flask import jsonify
app = Flask(__name__)  # initialising flask app
model = joblib.load('car performance') # load machine learning  model
@app.route('/', methods=['GET'])
def home():
    return render_template('ibm.html')
@app.route('/ibm.html')
def formpg():
    return render_template('ibm.html')
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        CYLINDERS = request.form['cylinders']
        DISPLACEMENT=request.form['displacement']
        HOESEPOWER=request.form['horsepower']
        WEIGHT = request.form['weight']
        MODEL_YEAR =request.form['model_year']
        ORIGIN =request.form['origin']
        prediction = model.predict([[int(CYLINDERS), int(DISPLACEMENT), int(HOESEPOWER), int(WEIGHT), int(MODEL_YEAR), int(ORIGIN)]])
        output=prediction[0]
        if(output<=9):
            return render_template('submit.html', prediction_text="Worst performance with mileage " + str(prediction[0]) +". Carry extra fuel")
        if(output>9 and output<=17.5):
            return render_template('submit.html', prediction_text="Low performance with mileage " +str(prediction[0]) +". Don't go to long distance")
        if(output>17.5 and output<=29):
            return render_template('submit.html', prediction_text="Medium performance with mileage " +str(prediction[0]) +". Go for a ride nearby.")
        if(output>29 and output<=46):
            return render_template('submit.html', prediction_text="High performance with mileage " +str(prediction[0]) +". Go for a healthy ride")
        if(output>46):
            return render_template('submit.html', prediction_text="Very high performance with mileage " +str(prediction[0])+". You can plan for a Tour")
    else:
        return render_template('ibm.html')

if __name__ == '__main__':
    app.run(debug=True)
