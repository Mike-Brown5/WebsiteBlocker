#from blocker import websites
websites = ["facebook.com", "youtube.com", "myanimelist.net", "instagram.com", "twitter.com","https://www.youtube.com/","https://www.facebook.com/"]

host_path = "/etc/hosts" # FOR LINUX!!
#host_path = "/private/etc/hosts" # FOR MAC!!
#host_path = "C:\\Windows\\System32\\Drivers\\etc\\hosts" # FOR WINDOWS!!!

with open(host_path, "r+") as file:
    content = file.readlines()
    file.seek(0)
    for web in content:
        if not any(webs in web for webs in websites):
            file.write(web)
    file.truncate()
    print("unblocked!!")