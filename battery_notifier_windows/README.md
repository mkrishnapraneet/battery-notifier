# README

Created: December 20, 2021 4:55 PM
Description (Project Name): For Battery Notifier
Last Edited Time: December 22, 2021 12:50 AM
Status: In Progress
Type: README

# Battery Notifier (Windows)

## Description :

Battery Notifier (Windows) is an application designed to work on a Windows PC. Once you run the application, it notifies you when : 

1. Your Laptop battery is charging and the battery level is above the level you set
2. Your Laptop battery is discharging and the battery level is below the level you set

So, essentially, this app allows you to maintain your laptop battery levels in the optimum range (for ex. 40% - 80%) easily, and thereby help in prolonging your laptop’s battery life. Since it is a very light program, it doesn’t waste any memory.

My motivation for this was straightforward, I just wanted automated notifications for the abovementioned cases.

I used Python to program this application, and made an .exe file out of it. Important modules and libraries used are ‘tkinter’ for GUI , ‘psutils’ for battery status querying , and ‘plyer’ for notifications.

## How to run :

To run the application, simply : 

battery_notifier_windows → battery.exe

In the dialog box that appears, set the lower bound and upper bound for battery percentage in their respective fields. Type in only integers between 0-100, without any other symbols (like ‘%’ for example). Also make sure lower bound is actually lower than the higher bound. After this, click ‘Apply’.

Now, the application runs in the background, and a new dialog box appears. Use the ‘Exit’ option in this dialog box if you want to stop the application altogether. Otherwise, minimise this dialog box, and continue with your work.

## Note :

It is to be noted that, sometimes, antivirus software might flag the application or any part of this as malware. (I experienced this issue personally, but I assure you, there is no malware in the program). I later found out that this flagging might be caused due to the use of pyinstaller to make an executable from the python script, or could also be due to the use of icon. Both these processes are malware -free. To confirm, I sent the file to AVG for testing, here is their response : 

![Screenshot (590).png](README%203aff022905dd437389349ddb45eeb74c/Screenshot_(590).png)

But if you are a cautious programmer, feel free to make an .exe file yourself from the python script named ‘battery.py’. Go through the code and make sure for yourself that this is safe. The command I used to turn this into an .exe file is 

```markdown
pyinstaller --onefile battery.py --hidden-import plyer.platforms.win.notification --windowed
```

(This assumes you have the required python setup for this)

## Extras

I learnt the basics of threading through this project.

In the future, I’m interested in making this a minimized app in the system tray, and also enhancing some other features.