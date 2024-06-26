# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_settingdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(567, 431)
        self.applyButton = QtWidgets.QPushButton(Dialog)
        self.applyButton.setGeometry(QtCore.QRect(460, 350, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.applyButton.setFont(font)
        self.applyButton.setObjectName("applyButton")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 241, 191))
        self.groupBox.setObjectName("groupBox")
        self.serialPortInfoListBox = QtWidgets.QComboBox(self.groupBox)
        self.serialPortInfoListBox.setGeometry(QtCore.QRect(10, 20, 221, 22))
        self.serialPortInfoListBox.setObjectName("serialPortInfoListBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(270, 30, 281, 191))
        self.groupBox_2.setObjectName("groupBox_2")
        self.stopBitsBox = QtWidgets.QComboBox(self.groupBox_2)
        self.stopBitsBox.setGeometry(QtCore.QRect(140, 110, 121, 22))
        self.stopBitsBox.setObjectName("stopBitsBox")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.parityBox = QtWidgets.QComboBox(self.groupBox_2)
        self.parityBox.setGeometry(QtCore.QRect(140, 80, 121, 22))
        self.parityBox.setObjectName("parityBox")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.baudRateBox = QtWidgets.QComboBox(self.groupBox_2)
        self.baudRateBox.setGeometry(QtCore.QRect(140, 20, 121, 22))
        self.baudRateBox.setObjectName("baudRateBox")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(10, 110, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.dataBitsBox = QtWidgets.QComboBox(self.groupBox_2)
        self.dataBitsBox.setGeometry(QtCore.QRect(140, 50, 121, 22))
        self.dataBitsBox.setObjectName("dataBitsBox")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 80, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.flowControlBox = QtWidgets.QComboBox(self.groupBox_2)
        self.flowControlBox.setGeometry(QtCore.QRect(140, 140, 121, 22))
        self.flowControlBox.setObjectName("flowControlBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "串口配置"))
        self.applyButton.setText(_translate("Dialog", "Apply"))
        self.groupBox.setTitle(_translate("Dialog", "串口选择："))
        self.label_2.setText(_translate("Dialog", "Descripition:"))
        self.label_3.setText(_translate("Dialog", "Serial number:"))
        self.groupBox_2.setTitle(_translate("Dialog", "参数选择："))
        self.label_7.setText(_translate("Dialog", "数据位："))
        self.label_6.setText(_translate("Dialog", "波特率："))
        self.label_9.setText(_translate("Dialog", "停止位："))
        self.label_8.setText(_translate("Dialog", "校验位："))
        self.label_5.setText(_translate("Dialog", "控制流："))
