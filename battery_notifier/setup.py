from cx_Freeze import setup, Executable
  
setup(name = "Battery Notifier" ,
      version = "0.1" ,
      description = "" ,
      executables = [Executable("battery.py")])