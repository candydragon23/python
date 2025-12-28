import tkinter as tk


def onClick():
    x = entry1.get()
    y = entry2.get()
    z = int(x) + int(y)
    lbl3.configure(text=str(z))


basewindow = tk.Tk()
basewindow.title("Работа с tkinter")
basewindow.geometry("1200x800")

# создаем элементы интерфейса и добавляем в окно

lbl1 = tk.Label(basewindow, text="Слагаемое", fg="red", bg="lightblue", font="Arial 18")
lbl1.pack()
entry1 = tk.Entry(basewindow, fg="red", bg="orange", font="Arial 18", borderwidth="3", width="40")
entry1.pack()
lbl2 = tk.Label(basewindow, text="Слагаемое", fg="red", bg="lightblue", font="Arial 18")
lbl2.pack()
entry2 = tk.Entry(basewindow, fg="red", bg="orange", font="Arial 18", borderwidth="3", width="40")
entry2.pack()
btn1 = tk.Button(text="Сложить", fg="red", bg="lightgreen", font="Arial 18", command=onClick)
btn1.pack()
lbl3 = tk.Label(basewindow, text="Результат: ", fg="red", bg="lightblue", font="Arial 18")
lbl3.pack()
basewindow.mainloop()
