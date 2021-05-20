import time
from datetime import datetime as dt

host_path = "/etc/hosts" # FOR LINUX!!
#host_path = "/private/etc/hosts" # FOR MAC!!
#host_path = "C:\\Windows\\System32\\Drivers\\etc\\hosts" # FOR WINDOWS!!!
redirect = "127.0.0.1"
#Defining the websites list
websites = ["facebook.com", "youtube.com", "myanimelist.net", "instagram.com", "twitter.com","https://www.youtube.com/","https://www.facebook.com/"]

#Blocking the websites on working hours (8AM:4PM)
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