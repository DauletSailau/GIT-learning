import requests  


CITY_COORDINATES = {
    'Astana': (51.169392,71.449074),
    'Moscow': (55.7558, 37.6176)
}
  
def fetch_weather_data(latitude, longitude):
    url = (f'https://api.open-meteo.com/v1/forecast'
           f'?latitude={latitude}'
           f'&longitude={longitude}'
           f'&current_weather=true')
    return requests.get(url, verify=False)

def parse_weather_data(response):
    if response.status_code==200:
        data=response.json()
        weather = data.get('current_weather', {})
        return {
            'Температура': f'{weather.get('temperature', 'N/A')} *C',
            'Скорость ветра': f'{weather.get('windspeed','N/A')} m/s',
            "Направление ветра": weather.get('winddirection', 'N/A'),
            'Время обновления': weather.get('time','N/A')
        }
    else:
        return {'Ошибка': 'Не удалось получить данные о погоде'}

def get_city_coordinates(city_name, city_coordinates=None):
    if city_coordinates is None:
        city_coordinates = CITY_COORDINATES
    return city_coordinates.get(city_name)

def get_weather_by_city(city_name):
    coordinates = get_city_coordinates(city_name)
    if  not coordinates:
        return {"Ошибка": f"City '{city_name}' не найден в базе данных координат." }
    
    response = fetch_weather_data(*coordinates)
    return parse_weather_data(response)

if __name__ == '__main__':
    city = 'Astana'
    weather_info= get_weather_by_city(city)
    print(weather_info)

# def get_weather(latitude, longitude):  
#     url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"  
#     response = requests.get(url, verify=False)  
  
#     if response.status_code == 200:  
#         data = response.json()  
#         weather = data.get("current_weather", {})  
#         return {  
#             "Температура": f"{weather.get('temperature', 'N/A')}°C",  
#             "Скорость ветра": f"{weather.get('windspeed', 'N/A')} м/с",  
#             "Направление ветра": weather.get('winddirection', 'N/A'),  
#             "Время обновления": weather.get('time', 'N/A')  
#         }  
#     else:  
#         return {"Ошибка": "Не удалось получить данные о погоде"}  
  
  
# astana_coord = (51.169392,71.449074) # Широта и долгота для Астаны

# if __name__ == "__main__":
#     weather_info = get_weather(*astana_coord)
#     print(weather_info)