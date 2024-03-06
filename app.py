import requests
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def index():
    if request.method == "POST":
        cityName = request.form.get("cityName")
        if cityName:
            weatherApiLKey = '6df07c2e4abaf940c03773728a47f0fa'
            
            url_city = "http://api.openweathermap.org/geo/1.0/direct?q=" + cityName + "&appid=" + weatherApiLKey
            cordinates = requests.get(url_city).json()
            url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(cordinates[0]["lon"]) + "&appid=" + weatherApiLKey
            weatherData = requests.get(url).json()
        else:
            error = 1
            return render_template('index.html', data = weatherData, cityName = cityName, error = error)
if __name__ == "__main__":
    app.run()
    