from flask import Flask, render_template, request
import requests
import json
app = Flask(__name__)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from test import WeatherData
@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'POST':
        city_name= request.form['city']
        g = requests.get(f'https://api.weatherapi.com/v1/forecast.json?key=231997168bb5479ea3c105957241208&q={city_name}&days=3&aqi=yes&alerts=no')
        if(g.status_code)!=200:
            Error = True
            return render_template("form.html",error=Error)
        data =g.json()
        forecast_days=[
        {

            'value1':f'{data["forecast"]["forecastday"][0]["date"]}',
            'value2':f'{data["forecast"]["forecastday"][0]["day"]["maxtemp_c"]}C',
            'value3':f'{data["forecast"]["forecastday"][0]["day"]["mintemp_c"]}',
            'value4':f'{data["forecast"]["forecastday"][0]["day"]["avgtemp_c"]}',
            'value5':f'{data["forecast"]["forecastday"][0]["day"]["avghumidity"]}',
            'value6':f'{data["forecast"]["forecastday"][0]["day"]["maxwind_kph"]}',
            'value7':f'{data["forecast"]["forecastday"][0]["day"]["totalprecip_mm"]}',
            'value8':f'{data["forecast"]["forecastday"][0]["day"]["daily_chance_of_rain"]}',
            'value9':f'{data["forecast"]["forecastday"][0]["day"]["uv"]}',
            'value10':f'{data["forecast"]["forecastday"][0]["day"]["condition"]["icon"]}',
            'value11': f'{data["forecast"]["forecastday"][0]["astro"]["sunrise"]}',
            'value12': f'{data["forecast"]["forecastday"][0]["astro"]["sunset"]}'
        },


        {

            'value1':f'{data["forecast"]["forecastday"][1]["date"]}',
            'value2':f'{data["forecast"]["forecastday"][1]["day"]["maxtemp_c"]}C',
            'value3':f'{data["forecast"]["forecastday"][1]["day"]["mintemp_c"]}',
            'value4':f'{data["forecast"]["forecastday"][1]["day"]["avgtemp_c"]}',
            'value5':f'{data["forecast"]["forecastday"][1]["day"]["avghumidity"]}',
            'value6':f'{data["forecast"]["forecastday"][1]["day"]["maxwind_kph"]}',
            'value7':f'{data["forecast"]["forecastday"][1]["day"]["totalprecip_mm"]}',
            'value8':f'{data["forecast"]["forecastday"][1]["day"]["daily_chance_of_rain"]}',
            'value9':f'{data["forecast"]["forecastday"][1]["day"]["uv"]}',
            'value10':f'{data["forecast"]["forecastday"][1]["day"]["condition"]["icon"]}',
            'value11': f'{data["forecast"]["forecastday"][1]["astro"]["sunrise"]}',
            'value12': f'{data["forecast"]["forecastday"][1]["astro"]["sunset"]}'
         },

        {

            'value1':f'{data["forecast"]["forecastday"][2]["date"]}',
            'value2':f'{data["forecast"]["forecastday"][2]["day"]["maxtemp_c"]}C',
            'value3':f'{data["forecast"]["forecastday"][2]["day"]["mintemp_c"]}',
            'value4':f'{data["forecast"]["forecastday"][2]["day"]["avgtemp_c"]}',
            'value5':f'{data["forecast"]["forecastday"][2]["day"]["avghumidity"]}',
            'value6':f'{data["forecast"]["forecastday"][2]["day"]["maxwind_kph"]}',
            'value7':f'{data["forecast"]["forecastday"][2]["day"]["totalprecip_mm"]}',
            'value8':f'{data["forecast"]["forecastday"][2]["day"]["daily_chance_of_rain"]}',
            'value9':f'{data["forecast"]["forecastday"][2]["day"]["uv"]}',
            'value10':f'{data["forecast"]["forecastday"][2]["day"]["condition"]["icon"]}',
            'value11': f'{data["forecast"]["forecastday"][2]["astro"]["sunrise"]}',
            'value12': f'{data["forecast"]["forecastday"][2]["astro"]["sunset"]}'

         }


        ]
        engine = create_engine("sqlite:///weather.db", echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        for forecast in forecast_days:
            if not session.query(WeatherData).filter(and_(WeatherData.date == forecast['value1'],WeatherData.city==city_name)).first():
                weatherDay = WeatherData(
                    date=forecast['value1'],
                    city=city_name,
                    maxtemp_c=forecast['value2'],
                    mintemp_c=forecast['value3'],
                    avgtemp_c=forecast['value4'],
                    avghumidity=forecast['value5'],
                    maxwind_kph=forecast['value6'],
                    totalprecip_mm=forecast['value7'],
                    daily_chance_of_rain=forecast['value8'],
                    uv=forecast['value9'],
                    sunset_hour=forecast['value12'],
                    sunrise_hour=forecast['value11']
                )
                session.add(weatherDay)
                session.commit()


            session.query(WeatherData).filter(
                and_(WeatherData.date == forecast['value1'], WeatherData.city == city_name)).update(
                {
                    WeatherData.maxtemp_c: forecast['value2'],
                    WeatherData.mintemp_c: forecast['value3'],
                    WeatherData.avgtemp_c: forecast['value4'],
                    WeatherData.avghumidity: forecast['value5'],
                    WeatherData.maxwind_kph: forecast['value6'],
                    WeatherData.totalprecip_mm: forecast['value7'],
                    WeatherData.daily_chance_of_rain: forecast['value8'],
                    WeatherData.uv: forecast['value9'],
                    WeatherData.sunset_hour: forecast['value12'],
                    WeatherData.sunrise_hour: forecast['value11']
                },
                synchronize_session=False
            )
            session.commit()

        q = session.query(WeatherData).all()
        for row in q:
            print("mintemp:", row.mintemp_c, "maxtemp:", row.maxtemp_c, "Id", row.id)

        return render_template('form.html',city=city_name,items=forecast_days)
    return render_template('form.html')


app.run(host='localhost',port=5000)