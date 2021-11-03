from flask import Flask, Response, jsonify, request
import requests
import os

app = Flask(__name__)
api_url = "http://api.openweathermap.org/data/2.5/weather"
API_key = os.environ['API_key']


@app.route('/weather/', methods=['GET'])
def get_current_weather():
    '''Получение текущих данных о погоде c https://openweathermap.org/'''

    city = request.args.get('city')
    params = {
        "q": city,
        "units": "metric",
        "appid": API_key,
        "lang": "ru"
    }
    try:
        result = requests.get(api_url, params=params)
        data = result.json()

        result_str = {
            'city': data['name'],
            'weather': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'feels': data['main']['feels_like'],
            'wind': data['wind']['speed'],
            'cloud': data['clouds']['all'],
            'humidity': data['main']['humidity']
            }
        return jsonify(result_str), 200

    except (KeyError, TypeError, ValueError) as error:
        print(error)
        return Response({"Error"}, status=409)


if __name__ == '__main__':
    app.run(debug=True)