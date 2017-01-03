# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stick.ui'
#
# Created: Tue Jan  3 18:01:12 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from GUI.edit import Ui_Dialog1

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 20, 161, 111))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.frame)
        self.plainTextEdit.setGeometry(QtCore.QRect(13, 11, 111, 91))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.pushButton_Add = QtGui.QPushButton(self.frame)
        self.pushButton_Add.setGeometry(QtCore.QRect(130, 10, 21, 43))
        self.pushButton_Add.setObjectName(_fromUtf8("pushButton_Add"))
        self.pushButton_Del = QtGui.QPushButton(Dialog)
        self.pushButton_Del.setGeometry(QtCore.QRect(150, 80, 21, 43))
        self.pushButton_Del.setObjectName(_fromUtf8("pushButton_Del"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        QtCore.QObject.connect(self.pushButton_Add, QtCore.SIGNAL(_fromUtf8("clicked()")), self.show_edit)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton_Add.setText(_translate("Dialog", "E", None))
        self.pushButton_Del.setText(_translate("Dialog", "D", None))

    def show_edit(self):
        self.edit_window = QtGui.QDialog()
        self.ui2 = Ui_Dialog1()
        self.ui2.setupUi(self.edit_window)
        self.edit_window.show()
        self.ui2.textEdit.setText(self.plainTextEdit.toPlainText())
        QtCore.QObject.connect(self.ui2.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.showMessage)

    def showMessage(self):
        message = self.ui2.textEdit.toPlainText()
        self.plainTextEdit.setPlainText(message)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

