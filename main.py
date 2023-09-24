'''
This file contains a basic system tray application using Python, PyQt and more.
The main.py file handels the main function of creating and intializing the application
'''
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()          #Inherit QMainWindow through a parent constructor
        self.setGeometry(200,200,300,300)         #Setting the position of the window, the parameters are (xpos, ypos, width and height)
    #(0,0) in graphics is top left, increasing the x pos moves the window to the right while increasing y pos moves the window down

        self.setWindowTitle("Homework Tracker 1.0")
        self.initUI()


    def initUI(self): #Create all the UI we want in the window
        self.label = QtWidgets.QLabel(self)    #Create the label
        self.label.setText("my first label!")
        self.label.move(100,100)

        self.b1 = QtWidgets.QPushButton(self)   #Create the button
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self): #Create a function that connects to the clicking event
        self.label.setText("Change the description")
        self.update()

    def update(self): #Update the width of the window text after clicking/changing the window
        self.label.adjustSize()





#Test window
def window():
    app = QApplication(sys.argv)  #Getting the application set up
    win = MyWindow()           #Setting up the window
    win.show()                 #Show the window
    sys.exit(app.exec_())




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
