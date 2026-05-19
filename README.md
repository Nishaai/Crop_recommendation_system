# Crop_recommendation_system 🌱🌦️

The Crop Recommendation System is a full-stack web application that helps users (especially farmers) choose the most suitable crop to cultivate based on environmental conditions and soil parameters.

This system integrates Machine Learning with real-time weather data fetched using a weather API, making the predictions more accurate and practical.

🚀 Features
🌦️ Real-time weather data integration using API
🌱 Machine Learning-based crop prediction
🧾 User-friendly web interface
⚡ Fast and accurate recommendations
🌍 Location-based input support
📊 Data-driven decision making

🛠️ Tech Stack
🔹 Frontend
HTML
CSS
JavaScript
🔹 Backend
Python (Flask)
🔹 Machine Learning
Pandas
NumPy
Scikit-learn
🔹 API Integration
OpenWeatherMap API (for real-time weather data)

🧠 How It Works
The user enters their location (city name).
The system fetches real-time weather data using the API.
The user inputs soil parameters such as Nitrogen (N), Phosphorus (P), and Potassium (K).
The Machine Learning model processes the data.
The system predicts and displays the most suitable crop.

📂 Project Structure
project/
│── static/           # CSS, JS files  
│── templates/        # HTML files  
│── model/            # Trained ML model  
│── app.py            # Main Flask app  
│── requirements.txt  # Dependencies  
│── dataset.csv       # Dataset  


▶️ Installation & Setup
git clone https://github.com/Nishaai/Crop_recommendation_system
cd repository-name
pip install -r requirements.txt
python app.py

💻 Usage
Open your browser and go to:
http://127.0.0.1:5000/
Enter location and soil values
Click Predict
View the recommended crop

📸 Output
Weather details display
Input form for soil nutrients
Predicted crop result


🔮 Future Enhancements
🌿 Fertilizer recommendation system
📱 Mobile application version
🌐 Multi-language support
🗺️ GPS-based auto location detection

🎯 Applications
Smart farming
Agricultural decision support
Precision agriculture
