import requests
key = "60bf8081ca92895f23b232fb4b2abc91"
print("Введите город")
city = input()
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric&lang=ru"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    weather = data['weather'][0]['description']
    print(f"Погода в городе {city}: {temp} градусов Цельсия, {weather}")
else:
    print(f"Ошибка: {response.status_code}")