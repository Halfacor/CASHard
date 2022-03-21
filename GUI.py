# https://www.pythontutorial.net/tkinter/
# https://www.tutorialspoint.com/python/python_gui_programming.htm
# https://htmlcolorcodes.com/
# https://stackoverflow.com/questions/36582244/tkinter-dynamically-updating-text-field-with-incoming-messages

import tkinter as tk
from tkinter import *
import threading
import time

plName = 'UCC'
plFee = 4.52
statId = -1
all_possible_status = ['full', 'Welcome', 'Drive Safe',
                       'Unregiestered or Too Much Overdue', 'Maintainance', 'Available']
plnVar = None
plfVar = None
statVar = None


def gui_func():
    root = tk.Tk()
    # constants
    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    global plnVar, plfVar, statVar, plName, plFee, all_possible_status, statId
    plnVar = StringVar()
    plfVar = StringVar()
    statVar = StringVar()

    plnVar.set(f'Parking Lot Name: {plName}')
    plfVar.set(f'Fee per Hour: {plFee}$')
    statVar.set('STATUS: ' + all_possible_status[statId])

    # set the position of the window to the center of the screen
    root.geometry(f'{screen_width}x{screen_height}')
    root.title('Cash Parking Onsite Display')
    root.resizable(0, 0)

    # Name label
    name_label = Label(root, text='CASH PARKING SYSTEM',
                       font=('Helvetica', screen_height//20, 'bold'), bg='cyan')
    name_label.pack(ipadx=screen_width/20)

    # Parking Lot Info
    parkinglot_name_label = Label(root, textvariable=plnVar, font=(
        'Helvetica', screen_height//30, 'bold'), bg='#92B5F5')
    parkinglot_fee_label = Label(root, textvariable=plfVar, font=(
        'Helvetica', screen_height//30, 'bold'), bg='#EBB254')

    parkinglot_name_label.pack()
    parkinglot_fee_label.pack()

    # Status Frame
    status_label = Label(root, textvariable=statVar, font=(
        'Helvetica', screen_height//20, 'bold'), bg='#F18583')
    status_label.pack()
    root.mainloop()


def changing():
    time.sleep(5)
    global plFee, statId, plfVar, plnVar, statVar
    while True:
        plFee += 1
        statId = (statId + 1) % 6
        plfVar.set(f'Fee per Hour: {plFee}$')
        statVar.set('STATUS: ' + all_possible_status[statId])
        time.sleep(1)


t1 = threading.Thread(target=gui_func)
t1.start()
t2 = threading.Thread(target=changing)
t2.start()
