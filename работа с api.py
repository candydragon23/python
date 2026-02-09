import geocoder
import requests
import tkinter as tk
from datetime import datetime
flag = True
sunrise_label = None
sunset_label = None
def submitfunc(town):
    global flag, sunrise_label, sunset_label
    current_date = datetime.now().strftime('%Y-%m-%d')
    try:
        city = geocoder.arcgis(town)
        crdnt = [city.json['lat'], city.json['lng']]
        URL = 'https://api.sunrise-sunset.org/json'
        params = {
            'lat': crdnt[0],
            'lng': crdnt[1],
            'date': current_date,
            'tzid': 'Asia/Irkutsk'
        }
        sun_r_s = requests.get(URL, params=params)
        sun_r_s_dict = sun_r_s.json()
    except TypeError:
        warning_label.configure(text='Город не найден')
        raise Exception('Город не найден')
    if sunrise_label is None and sunset_label is None:
        sunrise_label = tk.Label(mainWindow, text='Время восхода: ' + sun_r_s_dict['results']['sunrise'], font='Arial 18', pady='5px')
        sunrise_label.pack()
        sunset_label = tk.Label(mainWindow, text='Время заката: ' + sun_r_s_dict['results']['sunset'], font='Arial 18', pady='5px')
        sunset_label.pack()
        flag = False
    else:
        sunrise_label.configure(text='Время восхода: ' + sun_r_s_dict['results']['sunrise'])
        sunset_label.configure(text='Время заката: ' + sun_r_s_dict['results']['sunset'])
        warning_label.configure(text='')
    return
mainWindow = tk.Tk()
mainWindow.title('Данные о восходе и закате')
mainWindow.geometry('1024x720')
insert = tk.Label(mainWindow, text='Введите город для получения информации', font='Arial 18', pady='5px')
insert.pack(pady='15px')
cityEntry = tk.Entry(mainWindow, width=30, font='Arial 18')
cityEntry.pack()
submit = tk.Button(mainWindow, text='Получить данные', font='Arial 18', bg='#ff9933', pady='5px', command=lambda: submitfunc(cityEntry.get()))
submit.pack(pady='15px')
warning_label = tk.Label(mainWindow, font='Arial 18', pady='5px')
warning_label.pack()
mainWindow.mainloop()
