import os
from twilio.rest import Client
from twilio_config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN,PHONE_NUMBER,API_KEY_WAPI
import time

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from datetime import datetime


api_key = API_KEY_WAPI
query = ' Argentina  Misiones Posadas'

url_clima = 'http://api.weatherapi.com/v1/forecast.json?key='+api_key+'&q='+query+'&days=1&aqi=yes&alerts=no'


#obtener url
response = requests.get(url_clima).json()

def get_forecast(response,i):
    fecha = response['forecast']['forecastday'][0]['hour'][i]['time'] .split()[0]
    hora = int(response['forecast']['forecastday'][0]['hour'][i]['time'] .split()[1].split(':')[0])
    condicion = response['forecast']['forecastday'][0]['hour'][i]['condition']['text']
    temp = response['forecast']['forecastday'][0]['hour'][i]['temp_c']
    lluvia = response['forecast']['forecastday'][0]['hour'][i]['will_it_rain']
    prob_lluv = response['forecast']['forecastday'][0]['hour'][i]['chance_of_rain']
    
    return fecha, hora, condicion, temp, lluvia, prob_lluv

valores = []
for i in tqdm (range(len(response['forecast']['forecastday'][0]['hour'])), colour = 'Green'):
    valores.append(get_forecast(response, i))
    
col = ['Fecha', 'Hora', 'Condicion', 'Temp', 'Lluvia', 'Prob de lluvia']
dataFrame = pd.DataFrame(valores,columns=col)
# Valores climaticos para el df de msj
dataFrame_msj = dataFrame[(dataFrame['Lluvia']== 1) | (dataFrame['Lluvia']== 0) ]
dataFrame_msj = dataFrame_msj[['Hora', 'Condicion']]
dataFrame_msj.set_index('Hora', inplace = True)

print(dataFrame_msj)
