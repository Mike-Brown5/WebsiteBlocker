import os
websites = ["facebook.com", "youtube.com", "myanimelist.net", "instagram.com", "twitter.com","https://www.youtube.com/","https://www.facebook.com/"]

host_pathL = "/etc/hosts" # FOR LINUX!!
host_pathM = "/private/etc/hosts" # FOR MAC!!
host_patW = "C:\\Windows\\System32\\Drivers\\etc\\hosts" # FOR WINDOWS!!!
if os.path.exists(host_pathL) == True:
            host_path = host_pathL
elif os.path.exists(host_pathM) == True:
    host_path = host_pathM
elif os.path.exists(host_patW) == True:
    host_path = host_patW
def unblock():
    with open(host_path, "r+") as file:
        content = file.readlines()
        file.seek(0)
        for web in content:
            if not any(webs in web for webs in websites):
                file.write(web)
        file.truncate()
        print("unblocked!!")
