import requests
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    data = request.get_json()
    city = data['city']

    api_key = "8cf0f3d44274fbb0c12e60330613b6eb"  

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    weather_data = response.json()

    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']

    return jsonify({
        "temperature": temperature,
        "humidity": humidity
    })

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    features = [[
        data['N'], data['P'], data['K'],
        data['temperature'],
        data['humidity'],
        data['ph'],
        data['rainfall']
    ]]
    
    prediction = model.predict(features)
    
    return jsonify({"crop": prediction[0]})


if __name__ == "__main__":
    app.run(debug=True)