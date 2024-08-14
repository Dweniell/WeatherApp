from typing import List
from typing import Optional
from sqlalchemy.orm import session
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,Column,Integer,String,Float

engine = create_engine("sqlite:///weather.db", echo=True)

Base = declarative_base()

class WeatherData(Base):
    __tablename__ = 'WeatherData'
    id = Column(Integer, primary_key=True,autoincrement=True)
    date = Column(String(15))
    city = Column(String(20))
    maxtemp_c = Column(Integer)
    mintemp_c = Column(Integer)
    avgtemp_c = Column(Integer)
    avghumidity = Column(Float)
    maxwind_kph = Column(Float)
    totalprecip_mm = Column(Float)
    daily_chance_of_rain = Column(Integer)
    uv = Column(Integer)
    sunset_hour = Column(String(20))
    sunrise_hour = Column(String(20))

#Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session =Session()
c1 = WeatherData(id = 1,date ='2024-08-14', city='London',maxtemp_c=34,mintemp_c=29,avgtemp_c=30,avghumidity=68,maxwind_kph=7.9,totalprecip_mm=0.42,daily_chance_of_rain=87,uv=5,sunset_hour='08:24 PM',sunrise_hour='05:45 AM')
# session.add(c1)
# session.commit()
q= session.query(WeatherData).all()
for row in q:
    print("mintemp: ",row.mintemp_c, "maxtemp:",row.maxtemp_c,"Id",row.id,"City name: ",row.city)

# session.query(WeatherData).filter(WeatherData.date == '2024-08-14' and WeatherData.city=='London').update({WeatherData.maxtemp_c:200,WeatherData.mintemp_c:250,WeatherData.avgtemp_c:500,WeatherData.avghumidity:600,WeatherData.maxwind_kph:500,WeatherData.totalprecip_mm:600,WeatherData.daily_chance_of_rain:900,WeatherData.uv:500,WeatherData.sunset_hour:"5:99 AM",WeatherData.sunrise_hour:"9:99 AM"},synchronize_session = False)
# session.commit()
# q= session.query(WeatherData).all()
# for row in q:
#     print("id: ",row.id, "maxtemp:",row.maxtemp_c)