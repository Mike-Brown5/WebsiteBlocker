import time, os
from datetime import datetime as dt

host_pathL = "/etc/hosts" # FOR LINUX!!
host_pathM = "/private/etc/hosts" # FOR MAC!!
host_patW = "C:\\Windows\\System32\\Drivers\\etc\\hosts" # FOR WINDOWS!!!
redirect = "127.0.0.1"
if os.path.exists(host_pathL) == True:
            host_path = host_pathL
elif os.path.exists(host_pathM) == True:
    host_path = host_pathM
elif os.path.exists(host_patW) == True:
    host_path = host_patW
#Defining the websites list
websites = ["facebook.com", "youtube.com", "myanimelist.net", "instagram.com", "twitter.com","https://www.youtube.com/","https://www.facebook.com/"]

#Blocking the websites on working hours (8AM:4PM)
def block():
    while True:
        
        if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
            with open(host_path, "r+") as file:
                content = file.read()
                for web in websites:
                    if web in content:
                        pass
                    else:
                        file.write(redirect + " "+web + "\n")
            print("Working...")
        else:
            with open(host_path, "r+") as file:
                content = file.readlines()
                file.seek(0)
                for web in content:
                    if not any(webs in web for webs in websites):
                        file.write(web)
                file.truncate()
            print("Not working....")
        time.sleep(20)

block()