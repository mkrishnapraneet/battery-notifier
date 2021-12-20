import psutil
from plyer.utils import platform
from plyer import notification
import time
import tkinter
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from threading import *
import os
import sys

# function to exit from the application when called

def quit_prog():
    # sys.exit()
    os._exit(1)

# opens a new dialog box and has options to close the application in it

def the_close():
    last_window = tkinter.Tk()

    var = StringVar()
    label = Message(last_window, textvariable=var, width=500)
    # relief=RAISED
    var.set("The values have been set. The application is running in the background. You can : \n-> Use this window to exit the application, or \n-> Minimize this window to let it run in the background.")
    label.grid(row=0, column=0, columnspan=2)

    close_button = ttk.Button(last_window, text='Exit', command=quit_prog)
    # print("reached?")
    close_button.grid(padx=100, pady=50, row=4, column=0)

    last_window.protocol("WM_DELETE_WINDOW", quit_prog)

    last_window.mainloop()

# raise an error message when called

def error():
    messagebox.showerror(
        "Error", "The values you have entered are not correct.")

# starts a thread for running the gui

def threading():
    t1 = Thread(target=the_close)
    t1.start()

# called when 'Apply' button is pressed. Checks if the entered values are valid, then proceeds to periodically evaluate the battery status

def callback():
    global lower_lim
    try:
        lower_lim = int(e1.get())
    except:
        error()
        os.execv(sys.executable, ['python'] + sys.argv)
    # print(lower_lim)
    if (not(lower_lim >= 0 and lower_lim <= 100)):
        # print("Invalid Entry")
        error()
        os.execv(sys.executable, ['python'] + sys.argv)
        # quit()

    # higher_lim = int(input("Set Higher Limit for battery percentage : "))
    global higher_lim
    try:
        higher_lim = int(e2.get())
    except:
        error()
        os.execv(sys.executable, ['python'] + sys.argv)
    # print(higher_lim)
    if (not(higher_lim >= 0 and higher_lim <= 100 and higher_lim >= lower_lim)):
        # print("Invalid Entry")
        error()
        os.execv(sys.executable, ['python'] + sys.argv)
        # quit()

    window.destroy()
    # main_func(lower_lim,higher_lim)
    # return lower_lim, higher_lim

    threading()

    while (1):
        # print("inside")
        battery = psutil.sensors_battery()
        # apply_button.invoke()

        if ((battery.power_plugged == True) and (battery.percent >= higher_lim)):
            # print("battery percent : " , battery.percent , "power : " , battery.power_plugged , " higher lim : " , higher_lim)

            notification.notify(
                title='Battery Notifier',
                message='Your Battery Level has crossed ' +
                str(higher_lim) + '%. Please disconnect the charger',
                app_name='Battery Notifier',
                app_icon='./img.' + ('ico' if platform == 'win' else 'png')
            )
        if ((battery.power_plugged == False) and (battery.percent <= lower_lim)):
            # print("battery percent : " , battery.percent , "power : " , battery.power_plugged)
            notification.notify(
                title='Battery Notifier',
                message='Your Battery Level has gone below ' +
                str(lower_lim) + '%. Please connect the charger',
                app_name='Battery Notifier',
                app_icon='./img.' + ('ico' if platform == 'win' else 'png')
            )
        # window.mainloop()
        time.sleep(15)


# this section is setting up the main gui using tkinter
window = tkinter.Tk()

var = StringVar()
label = Message(window, textvariable=var, width=500)
# relief=RAISED
var.set("Use the below fields to set the desired values for the ideal upper and lower limits of battery charge percentage to prolong battery life.")
label.grid(row=0, column=0, columnspan=2)

Label(window, text='Minimum Desired Charging Percentage').grid(row=2)
Label(window, text='Maximum Desired Charging Percentage').grid(row=3)


e1 = Entry(window, bd=3)
e2 = Entry(window, bd=3)
e1.insert(END, '40')
e2.insert(END, '80')
e1.grid(row=2, column=1)
e2.grid(row=3, column=1)

lower_lim = 40
higher_lim = 80

# print("actual check : " , higher_lim)
apply_button = ttk.Button(window, text='Apply', command=callback)
# print("reached?")
apply_button.grid(padx=100, pady=50, row=4, column=0)

window.mainloop()
