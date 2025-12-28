import tkinter as tk
inFile = open('input2.txt', 'r', encoding='utf-8')
lines = inFile.readlines()
curline = 1
total = 1
correct = 0

def submit(lines):
    global curline
    global total
    global correctvalue
    check(correctvalue)
    if curline < len(lines):
        line = lines[curline]
        if line[:2] == 'q:':
            question_label.configure(text=line[2:])
            curline += 1
            total += 1
        while curline < len(lines):
            line = lines[curline]
            if line[:2] == '1.':
                if line.find('+') > -1:
                    correctvalue = 1
                    answer1.configure(text=line[2:-2])
                else:
                    answer1.configure(text=line[2:-1])
            elif line[:2] == '2.':
                if line.find('+') > -1:
                    correctvalue = 2
                    answer2.configure(text=line[2:-2])
                else:
                    answer2.configure(text=line[2:-1])
            elif line[:2] == '3.':
                if line.find('+') > -1:
                    correctvalue = 3
                    answer3.configure(text=line[2:-2])
                else:
                    answer3.configure(text=line[2:-1])
            elif line[:2] == 'q:':
                return
            curline += 1
    else:
        results()

def check(correctvalue):
    global correct
    if answer_radio.get() == correctvalue:
        correct += 1

def results():
    submit_button.destroy()
    answer1.destroy()
    answer2.destroy()
    answer3.destroy()
    question_label.configure(text='Ваш результат')
    correct_answers = tk.Label(text='Правильных ответов: ' + str(correct), font='Arial 18', pady='5px')
    correct_answers.pack()
    total_answers = tk.Label(text='Всего вопросов: ' + str(total), font='Arial 18', pady='5px')
    total_answers.pack()
    percentage = tk.Label(text='Процент правильных ответов: ' + str((correct / total) * 100) + '%', font='Arial 18', pady='5px')
    percentage.pack()

mainWindow = tk.Tk()
mainWindow.title('Тестирование')
mainWindow.geometry('1024x720')
question_label = tk.Label(mainWindow, font='Arial 18', pady='5px', text=lines[0][2:])
question_label.pack()
answer_radio = tk.IntVar()
answer1 = tk.Radiobutton(mainWindow, font='Arial 18', value='1', variable=answer_radio)
answer1.pack()
answer2 = tk.Radiobutton(mainWindow, font='Arial 18', value='2', variable=answer_radio)
answer2.pack()
answer3 = tk.Radiobutton(mainWindow, font='Arial 18', value='3', variable=answer_radio)
answer3.pack()
submit_button = tk.Button(mainWindow, text='Отправить ответ', font='Arial 18', bg='#ff9933', command=lambda: submit(lines))
submit_button.pack()
while lines[curline][:2] != 'q:':
    line = lines[curline]
    if line[:2] == '1.':
        if line.find('+') > -1:
            correctvalue = 1
            answer1.configure(text=line[2:-2])
        else:
            answer1.configure(text=line[2:-1])
    elif line[:2] == '2.':
        if line.find('+') > -1:
            correctvalue = 2
            answer2.configure(text=line[2:-2])
        else:
            answer2.configure(text=line[2:-1])
    elif line[:2] == '3.':
        if line.find('+') > -1:
            correctvalue = 3
            answer3.configure(text=line[2:-2])
        else:
            answer3.configure(text=line[2:-1])
    curline += 1

mainWindow.mainloop()