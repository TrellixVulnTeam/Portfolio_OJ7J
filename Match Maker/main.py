import random
import time
from tkinter import Tk, Button, DISABLED
from tkinter.constants import TRUE # This is an imported library

# Define Variables
def show_symbol(x,y):
    global first
    global previousx, previousy
    buttons[x,y]['text'] = button_symbols[x,y]
    buttons[x,y].update_idletasks()

    if first:
        previousx = x
        previousy = y
        first = False
    elif previousx != x or previousy != y:
        if buttons[previousx, previousy]['text']!= buttons[x,y]['text']:
            time.sleep(0.5) # This is where you set how much time that symbol will remain on the screen after an wrong answer
            buttons[previousx, previousy]['text'] = ' '
            buttons[x,y]['text'] =' '
        else:
            buttons[previousx, previousy] = DISABLED
            buttons[x,y] = DISABLED
        first = True

#
win = Tk()
win.title('Matchmaker') # This is where you can edit the Title
win.resizable(width=False, height=False)
first = True
previousx = 0
previousy = 0
buttons = {}
button_symbols = {}


# Create Symbols For Game
symbols=[u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
         u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728',
         u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
         u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728']


#
random.shuffle(symbols)

for x in range(6):
    for y in range(4):
        button = Button(command=lambda x=x, y=y: show_symbol(x,y), width=10, height=8)
        button.grid(column=x, row=y)
        buttons[x,y] = button
        button_symbols[x,y] = symbols.pop()

win.mainloop()
