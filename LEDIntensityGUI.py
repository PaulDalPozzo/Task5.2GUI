# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LEDSliders.ui'
#
# Created by: PyQt5 UI code generator 5.15.9

from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO


class Ui_MyWindow(object):
    def setupUi(self, MyWindow):
        MyWindow.setObjectName("MyWindow")
        MyWindow.resize(330, 160)
        self.centralwidget = QtWidgets.QWidget(MyWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # RED SLIDER
        self.sld_red = QtWidgets.QSlider(self.centralwidget)
        self.sld_red.setGeometry(QtCore.QRect(120, 10, 200, 30))
        self.sld_red.setOrientation(QtCore.Qt.Horizontal)
        self.sld_red.setObjectName("sld_red")
        self.sld_red.setMinimum(0)
        self.sld_red.setMaximum(100)
        self.sld_red.setValue(0)
        self.sld_red.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.sld_red.setTickInterval(10)
        self.sld_red.setSingleStep(10)
        self.sld_red.valueChanged.connect(self.red_changed)
        # RED LABEL
        self.lbl_red = QtWidgets.QLabel(self.centralwidget)
        self.lbl_red.setGeometry(QtCore.QRect(10, 10, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_red.setFont(font)
        self.lbl_red.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_red.setObjectName("lbl_red")
        # GREEN SLIDER
        self.sld_green = QtWidgets.QSlider(self.centralwidget)
        self.sld_green.setGeometry(QtCore.QRect(120, 50, 200, 30))
        self.sld_green.setOrientation(QtCore.Qt.Horizontal)
        self.sld_green.setObjectName("sld_green")
        self.sld_green.setMinimum(0)
        self.sld_green.setMaximum(100)
        self.sld_green.setValue(0)
        self.sld_green.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.sld_green.setTickInterval(10)
        self.sld_green.setSingleStep(10)
        self.sld_green.valueChanged.connect(self.green_changed)
        # GREEN LABEL
        self.lbl_green = QtWidgets.QLabel(self.centralwidget)
        self.lbl_green.setGeometry(QtCore.QRect(10, 50, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_green.setFont(font)
        self.lbl_green.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_green.setObjectName("lbl_green")
        # BLUE SLIDER
        self.sld_blue = QtWidgets.QSlider(self.centralwidget)
        self.sld_blue.setGeometry(QtCore.QRect(120, 90, 200, 30))
        self.sld_blue.setOrientation(QtCore.Qt.Horizontal)
        self.sld_blue.setObjectName("sld_blue")
        self.sld_blue.setMinimum(0)
        self.sld_blue.setMaximum(100)
        self.sld_blue.setValue(0)
        self.sld_blue.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.sld_blue.setTickInterval(10)
        self.sld_blue.setSingleStep(10)
        self.sld_blue.valueChanged.connect(self.blue_changed)
        # BLUE LABEL
        self.lbl_blue = QtWidgets.QLabel(self.centralwidget)
        self.lbl_blue.setGeometry(QtCore.QRect(10, 90, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_blue.setFont(font)
        self.lbl_blue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_blue.setObjectName("lbl_blue")
        
        self.led_blue = GPIO.PWM(11, 500) # (pin number, frequency)
        self.led_blue.start(0) # starts at 0 duty cycle
        self.led_red = GPIO.PWM(13, 500) # (pin number, frequency)
        self.led_red.start(0) # starts at 0 duty cycle
        self.led_green = GPIO.PWM(15, 500) # (pin number, frequency)
        self.led_green.start(0) # starts at 0 duty cycle
        
        MyWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MyWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 330, 21))
        self.menubar.setObjectName("menubar")
        MyWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MyWindow)
        self.statusbar.setObjectName("statusbar")
        MyWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MyWindow)
        QtCore.QMetaObject.connectSlotsByName(MyWindow)

    def retranslateUi(self, MyWindow):
        _translate = QtCore.QCoreApplication.translate
        MyWindow.setWindowTitle(_translate("MyWindow", "LED Intensity GUI"))
        self.lbl_red.setText(_translate("MyWindow", "RED"))
        self.lbl_green.setText(_translate("MyWindow", "GREEN"))
        self.lbl_blue.setText(_translate("MyWindow", "BLUE"))
        
    def red_changed(self):
        value = self.sld_red.value()
        self.led_red.ChangeDutyCycle(value)
    
    def green_changed(self):
        value = self.sld_green.value()
        self.led_green.ChangeDutyCycle(value)
    
    def blue_changed(self):
        value = self.sld_blue.value()
        self.led_blue.ChangeDutyCycle(value)
        
        
def window():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MyWindow = QtWidgets.QMainWindow()
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT) #blue
    GPIO.setup(13, GPIO.OUT) #red
    GPIO.setup(15, GPIO.OUT) #green
    
    ui = Ui_MyWindow()
    ui.setupUi(MyWindow)
    MyWindow.show()
    sys.exit(app.exec_())

    
window()
GPIO.cleanup()
