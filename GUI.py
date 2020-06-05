#Note: I was able to use only 2 leds rather than 3 for this task
#due to having only 2 resistors
#importing libraries
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO
import time

#GPIO Setup and Config 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
timer = 0.25

GPIO.output(17,GPIO.LOW)
GPIO.output(22,GPIO.LOW)

#Main Window
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(313, 300)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.redButton = QtWidgets.QRadioButton(self.centralwidget)
        self.redButton.setGeometry(QtCore.QRect(110, 30, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.redButton.setFont(font)
        self.redButton.setObjectName("redButton")

        self.greenButton = QtWidgets.QRadioButton(self.centralwidget)
        self.greenButton.setGeometry(QtCore.QRect(110, 90, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.greenButton.setFont(font)
        self.greenButton.setObjectName("greenButton")
        
        self.allOffButton = QtWidgets.QRadioButton(self.centralwidget)
        self.allOffButton.setGeometry(QtCore.QRect(170, 140, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        self.allOffButton.setFont(font)
        self.allOffButton.setObjectName("allOffButton")
        self.allOnButton = QtWidgets.QRadioButton(self.centralwidget)
        self.allOnButton.setGeometry(QtCore.QRect(60, 140, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.allOnButton.setFont(font)
        self.allOnButton.setObjectName("allOnButton")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(100, 200, 121, 41))
        self.exitButton.setObjectName("exitButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 313, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.redButton.clicked.connect(self.redLed)
        self.greenButton.clicked.connect(self.greenLed)
        self.allOnButton.clicked.connect(self.allOn)
        self.allOffButton.clicked.connect(self.allOff)
        self.exitButton.clicked.connect(self.exit)
        self.actionExit.triggered.connect(self.exit)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lighting Leds"))
        self.redButton.setText(_translate("MainWindow", "Red"))
        self.greenButton.setText(_translate("MainWindow", "Green"))
        self.allOffButton.setText(_translate("MainWindow", "All Off"))
        self.allOnButton.setText(_translate("MainWindow", "All On"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.menuFile.setTitle(_translate("MainWindow", "GUI Interface"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+X"))

    #Functions for LED interactions
    def redLed(self):

        GPIO.output(22,GPIO.LOW)
        GPIO.output(17,GPIO.HIGH)

    def allOn(self):

        GPIO.output(17,GPIO.HIGH)
        GPIO.output(22,GPIO.HIGH)

    def allOff(self):

        GPIO.output(17,GPIO.LOW)
        GPIO.output(22,GPIO.LOW)

    def greenLed(self):

        GPIO.output(17,GPIO.LOW)
        GPIO.output(22,GPIO.HIGH)

    def exit(self):
        QtCore.QCoreApplication.instance().quit()

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
