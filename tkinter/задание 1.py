import tkinter as tk
output = open('output.txt', 'w', encoding='utf-8')

def write(line, current):
    line = str(line)
    if current == 1:
        output.write('Любимый жанр игр пользователя: ')
    elif current == 2:
        output.write('Отношение к сюжету: ')
        if line == '1':
            output.write('(Очень важен) ')
        elif line == '2':
            output.write('(Немного важен) ')
        elif line == '3':
            output.write('(Неважен) ')
        else:
            output.write('(Не отвечен) ')
    elif current == 3:
        output.write('Частота игры в компьютер: ')
    elif current == 4:
        output.write('Предпочитаемая платформа: ')
    else:
        output.write('Отношение к мультиплееру: ')
        if line == '1':
            output.write('(Люблю их) ')
        elif line == '2':
            output.write('(Что-то между) ')
        elif line == '3':
            output.write('(Не люблю их) ')
        else:
            output.write('(Не отвечен) ')
    output.write(line + '\n')

def onClick():
    text = [genre_entry.get(), story_radio.get(), length_entry.get(), platform_entry.get(), multi_radio.get()]
    send_button.configure(bg="#eaff00", text="Отправлено!")
    current = 1
    for line in text:
        write(line, current)
        current += 1

mainWindow = tk.Tk()
mainWindow.title("Анкета по компьютерным играм")
mainWindow.geometry("1024x720")
main_title = tk.Label(mainWindow, text="Анкета по компьютерныым играм", font="Arial 24", pady="5px")
main_title.pack()
genre_title = tk.Label(mainWindow, text="Какой ваш любимый жанр игр?", font="Arial 18", pady="5px")
genre_title.pack()
genre_entry = tk.Entry(mainWindow, font="Arial 18", justify="center" )
genre_entry.pack()
story_title = tk.Label(mainWindow, text="Какое значение для вас имеет сюжет в игре", font="Arial 18", pady="5px")
story_title.pack()
story_radio = tk.IntVar()
story1 = tk.Radiobutton(mainWindow, text="Очень важен", font="Arial 18", value="1", variable=story_radio)
story1.pack()
story2 = tk.Radiobutton(mainWindow, text="Немного важен", font="Arial 18", value="2", variable=story_radio)
story2.pack()
story3 = tk.Radiobutton(mainWindow, text="Неважен", font="Arial 18", value="3", variable=story_radio)
story3.pack()
length_title = tk.Label(mainWindow, text="Как часто вы играете в компьютерные игры?", font="Arial 18", pady="5px")
length_title.pack()
length_entry = tk.Entry(mainWindow, font="Arial 18", justify="center")
length_entry.pack()
platform_title = tk.Label(mainWindow, text="Какой тип платформы для игр вам больше всего нравится?", font="Arial 18", pady="5px")
platform_title.pack()
platform_entry = tk.Entry(mainWindow, font="Arial 18", justify="center")
platform_entry.pack()
multi_title = tk.Label(mainWindow, text="Как вы относитесь к мультиплеерным играм?", font="Arial 18", pady="5px")
multi_title.pack()
multi_radio = tk.IntVar()
multi1 = tk.Radiobutton(mainWindow, text="Люблю их", font="Arial 18", value="1", variable=multi_radio)
multi1.pack()
multi2 = tk.Radiobutton(mainWindow, text="Что-то между", font="Arial 18", value="2", variable=multi_radio)
multi2.pack()
multi3 = tk.Radiobutton(mainWindow, text="Не люблю их", font="Arial 18", value="3", variable=multi_radio)
multi3.pack()
send_button = tk.Button(mainWindow, text="Отправить", font="Arial 18", bg="#ff9933", command=onClick)
send_button.pack()

mainWindow.mainloop()