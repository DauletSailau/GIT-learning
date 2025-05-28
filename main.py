import requests  
  
  
def get_weather(latitude, longitude):  
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"  
    response = requests.get(url, verify=False)  
  
    if response.status_code == 200:  
        data = response.json()  
        weather = data.get("current_weather", {})  
        return {  
            "Температура": f"{weather.get('temperature', 'N/A')}°C",  
            "Скорость ветра": f"{weather.get('windspeed', 'N/A')} м/с",  
            "Направление ветра": weather.get('winddirection', 'N/A'),  
            "Время обновления": weather.get('time', 'N/A')  
        }  
    else:  
        return {"Ошибка": "Не удалось получить данные о погоде"}  
  
  
astana_coord = (51.169392,71.449074) # Широта и долгота для Астаны

if __name__ == "__main__":
    weather_info = get_weather(*astana_coord)
    print(weather_info)