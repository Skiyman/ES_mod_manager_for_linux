# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GreetingWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(700, 700)
        Dialog.setMinimumSize(QSize(700, 700))
        Dialog.setMaximumSize(QSize(700, 700))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_2.setIndent(8)

        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        self.label.setFont(font1)
        self.label.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setIndent(10)

        self.verticalLayout.addWidget(self.label)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setIndent(10)

        self.verticalLayout.addWidget(self.label_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.enable_folder_label = QLabel(Dialog)
        self.enable_folder_label.setObjectName(u"enable_folder_label")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.enable_folder_label.setFont(font2)
        self.enable_folder_label.setMargin(0)
        self.enable_folder_label.setIndent(8)

        self.horizontalLayout_3.addWidget(self.enable_folder_label)

        self.enable_folder_name = QLineEdit(Dialog)
        self.enable_folder_name.setObjectName(u"enable_folder_name")
        self.enable_folder_name.setEnabled(True)
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        self.enable_folder_name.setFont(font3)
        self.enable_folder_name.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.enable_folder_name)

        self.browse_enable_folder_button = QPushButton(Dialog)
        self.browse_enable_folder_button.setObjectName(u"browse_enable_folder_button")
        self.browse_enable_folder_button.setFont(font3)

        self.horizontalLayout_3.addWidget(self.browse_enable_folder_button)

        self.horizontalLayout_3.setStretch(0, 11)
        self.horizontalLayout_3.setStretch(1, 20)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.disable_folder_label = QLabel(Dialog)
        self.disable_folder_label.setObjectName(u"disable_folder_label")
        self.disable_folder_label.setFont(font2)
        self.disable_folder_label.setMargin(0)
        self.disable_folder_label.setIndent(8)

        self.horizontalLayout_4.addWidget(self.disable_folder_label)

        self.disable_folder_name = QLineEdit(Dialog)
        self.disable_folder_name.setObjectName(u"disable_folder_name")
        self.disable_folder_name.setEnabled(True)
        self.disable_folder_name.setFont(font3)
        self.disable_folder_name.setReadOnly(True)
        self.disable_folder_name.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.disable_folder_name)

        self.browse_disable_folder_button = QPushButton(Dialog)
        self.browse_disable_folder_button.setObjectName(u"browse_disable_folder_button")
        self.browse_disable_folder_button.setFont(font3)

        self.horizontalLayout_4.addWidget(self.browse_disable_folder_button)

        self.horizontalLayout_4.setStretch(0, 11)
        self.horizontalLayout_4.setStretch(1, 20)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.apply_button = QPushButton(Dialog)
        self.apply_button.setObjectName(u"apply_button")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apply_button.sizePolicy().hasHeightForWidth())
        self.apply_button.setSizePolicy(sizePolicy)
        self.apply_button.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout.addWidget(self.apply_button)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 5)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e.", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u043d\u043d\u044b\u0439 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0435\u0442 \u0443\u043f\u0440\u043e\u0441\u0442\u0438\u0442\u044c \u0437\u0430\u043f\u0443\u0441\u043a \u0432\u0438\u0437\u0443\u0430\u043b\u044c\u043d\u043e\u0439 \u043d\u043e\u0432\u0435\u043b\u043b\u044b\u0439 \"\u0411\u0435\u0441\u043a\u043e\u043d\u0435\u0447\u043d\u043e\u0435 \u043b\u0435\u0442\u043e\" \u043f\u0440\u0438 \u0431\u043e\u043b\u044c\u0448\u043e\u043c \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0435 \u043c\u043e\u0434\u043e\u0432.", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u2014 \u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043c\u043e\u0434\u043e\u0432 \u043c\u0435\u043d\u0435\u0436\u0434\u0435\u0440 \u043f\u043e\u043b\u0443\u0447\u0430\u0435\u0442 \u0438\u0437 \u043c\u0430\u0441\u0442\u0435\u0440\u0441\u043a\u043e\u0439 Steam. \u041f\u043e\u0442\u043e\u043c\u0443 \u0434\u043b\u044f \u043f\u0435\u0440\u0432\u043e\u0433\u043e \u0437\u0430\u043f\u0443\u0441\u043a\u0430 \u0438 \u043f\u043e\u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0433\u043e \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0441\u043f\u0438\u0441\u043a\u0430 \u043c\u043e\u0434\u043e\u0432 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u043a \u0438\u043d\u0442\u0435\u0440\u043d\u0435\u0442\u0443. \n"
"\n"
"\u2014 \u041d\u0430\u0441\u0442\u043e\u044f\u0442\u0435\u043b\u044c\u043d\u043e \u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u0442\u0441\u044f \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u0442"
                        "\u044c \u043f\u0430\u043f\u043a\u0443 \u0434\u043b\u044f \u0432\u044b\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u043c\u043e\u0434\u043e\u0432, \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u043d\u0443\u044e \u043d\u0430 \u0442\u043e\u043c \u0436\u0435 \u0434\u0438\u0441\u043a\u0435, \u0433\u0434\u0435 \u0438 \u043c\u043e\u0434\u044b. \u042d\u0442\u043e \u043f\u043e\u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0441\u0442\u0440\u0435\u0435 \u043f\u0435\u0440\u0435\u043d\u043e\u0441\u0438\u0442\u044c \u043c\u043e\u0434\u044b\n"
"\n"
"\u2014 \u0415\u0441\u043b\u0438 \u043f\u0440\u0438 \u0432\u044b\u0431\u043e\u0440\u0435 \u043f\u0430\u043f\u043a\u0438 \u043d\u0435 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u044e\u0442\u0441\u044f \u0441\u043a\u0440\u044b\u0442\u044b\u0435 \u043f\u0430\u043f\u043a\u0438, \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u041f\u041a\u041c \u0438 \u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043e\u043e\u0442\u0432\u043a\u0435\u0442\u0441\u0442\u0432\u0443"
                        "\u044e\u0449\u0438\u0439 \u043f\u0443\u043d\u043a\u0442 \u0432 \u043a\u043e\u043d\u0442\u0435\u043a\u0441\u0442\u043d\u043e\u043c \u043c\u0435\u043d\u044e.", None))
        self.enable_folder_label.setText(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043c\u043e\u0434\u043e\u0432:", None))
        self.browse_enable_folder_button.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.disable_folder_label.setText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u043f\u043a\u0430 \u0434\u043b\u044f \u0432\u044b\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f: ", None))
        self.browse_disable_folder_button.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.apply_button.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

