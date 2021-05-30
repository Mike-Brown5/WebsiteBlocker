import sys , PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAction, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import time, os ,PyQt5
import threading
from datetime import datetime as dt

def window():
   app = QApplication(sys.argv)
   widget = QWidget()
   button1 = QPushButton(widget)
   button1.setText("BLOCK")
   button1.move(64,32)
   button1.clicked.connect(block)

   button2 = QPushButton(widget)
   button2.setText("UNBLOCK")
   button2.move(64,64)
   button2.clicked.connect(unblock)

   widget.setGeometry(50,50,320,200)
   widget.setWindowTitle("BLOCKER")
   text = button1.text()
   lable = PyQt5.QtWidgets.QLabel(text)
   lable.move(100,100)
   widget.show()
   sys.exit(app.exec_())


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
websites = ["facebook.com", "youtube.com", "myanimelist.net", "instagram.com", "twitter.com","https://www.youtube.com/","https://www.facebook.com/"]

def block():
        with open(host_path, "r+") as file:
            content = file.read()
            for web in websites:
                if web in content:
                    pass
                else:
                        file.write(redirect + " "+web + "\n")
            print("Working...")


def unblock():
    with open(host_path, "r+") as file:
        content = file.readlines()
        file.seek(0)
        for web in content:
            if not any(webs in web for webs in websites):
                file.write(web)
        file.truncate()
        print("unblocked!!")

 
   
if __name__ == '__main__':
   window()