# Form implementation generated from reading ui file 'c:\Users\Dimitry\ДМиТИ\long_arithmetic\UI\first_choice.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(734, 504)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 75, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.N_button = QtWidgets.QPushButton(Form)
        self.N_button.setObjectName("N_button")
        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.N_button)
        self.gridLayout.addWidget(self.N_button, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.C_button = QtWidgets.QPushButton(Form)
        self.C_button.setObjectName("C_button")
        self.buttonGroup.addButton(self.C_button)
        self.gridLayout.addWidget(self.C_button, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(119, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        self.R_button = QtWidgets.QPushButton(Form)
        self.R_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.R_button.setObjectName("R_button")
        self.buttonGroup.addButton(self.R_button)
        self.gridLayout.addWidget(self.R_button, 3, 1, 1, 1)
        self.P_button = QtWidgets.QPushButton(Form)
        self.P_button.setObjectName("P_button")
        self.buttonGroup.addButton(self.P_button)
        self.gridLayout.addWidget(self.P_button, 4, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 75, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem3, 5, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.N_button.setText(_translate("Form", "Натуральные числа"))
        self.C_button.setText(_translate("Form", "Целые числа"))
        self.R_button.setText(_translate("Form", "Рациональные числа"))
        self.P_button.setText(_translate("Form", "Многочлены"))
