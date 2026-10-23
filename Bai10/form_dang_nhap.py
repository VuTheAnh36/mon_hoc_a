# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_dang_nhap.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.o_nhap_tai_khoan = QLabel(Form)
        self.o_nhap_tai_khoan.setObjectName(u"o_nhap_tai_khoan")
        self.o_nhap_tai_khoan.setGeometry(QRect(60, 80, 61, 16))
        self.o_nhap_mat_khau = QLabel(Form)
        self.o_nhap_mat_khau.setObjectName(u"o_nhap_mat_khau")
        self.o_nhap_mat_khau.setGeometry(QRect(60, 110, 61, 16))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 70, 113, 26))
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(130, 100, 113, 26))
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.nut_dang_nhap = QPushButton(Form)
        self.nut_dang_nhap.setObjectName(u"nut_dang_nhap")
        self.nut_dang_nhap.setGeometry(QRect(140, 150, 81, 26))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.o_nhap_tai_khoan.setText(QCoreApplication.translate("Form", u"T\u00e0i Kho\u1ea3n", None))
        self.o_nhap_mat_khau.setText(QCoreApplication.translate("Form", u"M\u1eadt Kh\u1ea9u", None))
        self.nut_dang_nhap.setText(QCoreApplication.translate("Form", u"\u0110\u0103ng nh\u1eadp", None))
    # retranslateUi

