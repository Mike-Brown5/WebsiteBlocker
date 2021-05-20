import sys , PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
   app = QApplication(sys.argv)
   widget = QWidget()
#    PyQt5.QtTextToSpeech.QTextToSpeech.__text_signature__("text")
#    widget
   button1 = QPushButton(widget)
   button1.setText("BLOCK")
   button1.move(64,32)
   button1.clicked.connect(button1_clicked)

   button2 = QPushButton(widget)
   button2.setText("UNBLOCK")
   button2.move(64,64)
   button2.clicked.connect(button2_clicked)

   widget.setGeometry(50,50,320,200)
   widget.setWindowTitle("BLOCKER")
   widget.show()
   sys.exit(app.exec_())


def button1_clicked():
   print("Button 1 clicked")

def button2_clicked():
   print("Button 2 clicked")   
   
if __name__ == '__main__':
   window()