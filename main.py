from tkinter import *
from tkinter import ttk

color1 = '#3b3b3b'
color2 = '#feffff'
color3 = '#38576b'
color4 = '#ECEFF1'
color5 = '#FFAB40'

window = Tk()
window.title('Calculator')
window.geometry('235x310')
window.config(bg=color1)

def create_btn(txt, command, width, height, x, y, color, fg='#3b3b3b'):
    btn = Button(body_frame, text=txt, command=command, width=width, height=height, bg=color, fg=fg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, justify=RIGHT, )
    btn.place(x=x, y=y)

#Frames
window_frame = Frame(window, width=235, height=50, bg=color3)
window_frame.grid(row=0, column=0)

body_frame = Frame(window, width=235, height=268)
body_frame.grid(row=1, column=0)

all_values = ''

#Setting the clicks on the calc
def set_result(event):
    global all_values
    if not all_values == '':
        check_string = all_values[-1]
    if not ((all_values == '') and (event in['%', '/', '*', '-', '+', '=', '.'])):
        if not ((event in['%', '/', '*', '-', '+', '=', '.']) and (check_string in['%', '/', '*', '-', '+', '=', '.'])):
            all_values = all_values + str(event)
            txt_value.set(all_values)

# calc results
def calc():
    global all_values
    check_string = all_values[-1]
    if not ((all_values == '') | (check_string in['%', '/', '*', '-', '+', '=', '.'])): 
        all_values = str(eval(all_values))
        txt_value.set(all_values)

def clear():
    global all_values
    all_values = ''
    txt_value.set(all_values)

#Label
txt_value = StringVar()

app_label = Label(window_frame, textvariable=txt_value, width=16, height=2, padx=7, relief=FLAT, anchor='e',  font=('Ivy 18'), bg=color3, fg=color2)
app_label.place(x=0, y=0)

#Creating Buttons
create_btn(txt='C', command= clear, width=11, height=2, x=0, y=0, color=color4)
create_btn(txt='%', command= lambda: set_result('%'), width=5, height=2, x=118, y=0, color=color4)
create_btn(txt='/', command= lambda: set_result('/'), width=5, height=2, x=177, y=0, color=color5, fg=color4)

create_btn(txt='7', command= lambda: set_result('7'), width=5, height=2, x=0, y=52, color=color4)
create_btn(txt='8', command= lambda: set_result('8'), width=5, height=2, x=59, y=52, color=color4)
create_btn(txt='9', command= lambda: set_result('9'), width=5, height=2, x=118, y=52, color=color4)
create_btn(txt='*', command= lambda: set_result('*'), width=5, height=2, x=177, y=52, color=color5, fg=color4)

create_btn(txt='4', command= lambda: set_result('4'), width=5, height=2, x=0, y=104, color=color4)
create_btn(txt='5', command= lambda: set_result('5'), width=5, height=2, x=59, y=104, color=color4)
create_btn(txt='6', command= lambda: set_result('6'), width=5, height=2, x=118, y=104, color=color4)
create_btn(txt='-', command= lambda: set_result('-'), width=5, height=2, x=177, y=104, color=color5, fg=color4)

create_btn(txt='1', command= lambda: set_result('1'), width=5, height=2, x=0, y=156, color=color4)
create_btn(txt='2', command= lambda: set_result('2'), width=5, height=2, x=59, y=156, color=color4)
create_btn(txt='3', command= lambda: set_result('3'), width=5, height=2, x=118, y=156, color=color4)
create_btn(txt='+', command= lambda: set_result('+'), width=5, height=2, x=177, y=156, color=color5, fg=color4)

create_btn(txt='0', command= lambda: set_result('0'), width=11, height=2, x=0, y=208, color=color4)
create_btn(txt='.', command= lambda: set_result('.'), width=5, height=2, x=118, y=208, color=color4)
create_btn(txt='=', command= calc, width=5, height=2, x=177, y=208, color=color5, fg=color4)

window.mainloop()