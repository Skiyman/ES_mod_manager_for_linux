# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(700, 500)
        SettingsWindow.setMinimumSize(QSize(700, 500))
        SettingsWindow.setMaximumSize(QSize(700, 500))
        self.verticalLayout_3 = QVBoxLayout(SettingsWindow)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.mod_move_method_label = QLabel(SettingsWindow)
        self.mod_move_method_label.setObjectName(u"mod_move_method_label")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.mod_move_method_label.setFont(font)
        self.mod_move_method_label.setMargin(10)

        self.verticalLayout_5.addWidget(self.mod_move_method_label)

        self.before_game_start_rb = QRadioButton(SettingsWindow)
        self.mod_move_method_group = QButtonGroup(SettingsWindow)
        self.mod_move_method_group.setObjectName(u"mod_move_method_group")
        self.mod_move_method_group.addButton(self.before_game_start_rb)
        self.before_game_start_rb.setObjectName(u"before_game_start_rb")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.before_game_start_rb.setFont(font1)

        self.verticalLayout_5.addWidget(self.before_game_start_rb)

        self.on_switch_rb = QRadioButton(SettingsWindow)
        self.mod_move_method_group.addButton(self.on_switch_rb)
        self.on_switch_rb.setObjectName(u"on_switch_rb")
        self.on_switch_rb.setFont(font1)

        self.verticalLayout_5.addWidget(self.on_switch_rb)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.when_update_label = QLabel(SettingsWindow)
        self.when_update_label.setObjectName(u"when_update_label")
        self.when_update_label.setEnabled(True)
        self.when_update_label.setFont(font)
        self.when_update_label.setMargin(10)

        self.verticalLayout_4.addWidget(self.when_update_label)

        self.on_launch_update_rb = QRadioButton(SettingsWindow)
        self.update_group = QButtonGroup(SettingsWindow)
        self.update_group.setObjectName(u"update_group")
        self.update_group.addButton(self.on_launch_update_rb)
        self.on_launch_update_rb.setObjectName(u"on_launch_update_rb")
        self.on_launch_update_rb.setFont(font1)

        self.verticalLayout_4.addWidget(self.on_launch_update_rb)

        self.on_button_click_rb = QRadioButton(SettingsWindow)
        self.update_group.addButton(self.on_button_click_rb)
        self.on_button_click_rb.setObjectName(u"on_button_click_rb")
        self.on_button_click_rb.setFont(font1)

        self.verticalLayout_4.addWidget(self.on_button_click_rb)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.path_label = QLabel(SettingsWindow)
        self.path_label.setObjectName(u"path_label")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.path_label.setFont(font2)
        self.path_label.setIndent(10)

        self.verticalLayout_2.addWidget(self.path_label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.enabel_folder_label = QLabel(SettingsWindow)
        self.enabel_folder_label.setObjectName(u"enabel_folder_label")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        self.enabel_folder_label.setFont(font3)
        self.enabel_folder_label.setMargin(0)
        self.enabel_folder_label.setIndent(8)

        self.horizontalLayout_3.addWidget(self.enabel_folder_label)

        self.enabel_folder_name = QLineEdit(SettingsWindow)
        self.enabel_folder_name.setObjectName(u"enabel_folder_name")
        self.enabel_folder_name.setEnabled(True)
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        self.enabel_folder_name.setFont(font4)
        self.enabel_folder_name.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.enabel_folder_name)

        self.browse_enabel_folder_button = QPushButton(SettingsWindow)
        self.browse_enabel_folder_button.setObjectName(u"browse_enabel_folder_button")
        self.browse_enabel_folder_button.setFont(font4)

        self.horizontalLayout_3.addWidget(self.browse_enabel_folder_button)

        self.horizontalLayout_3.setStretch(0, 11)
        self.horizontalLayout_3.setStretch(1, 20)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.disabel_folder_label = QLabel(SettingsWindow)
        self.disabel_folder_label.setObjectName(u"disabel_folder_label")
        self.disabel_folder_label.setFont(font3)
        self.disabel_folder_label.setMargin(0)
        self.disabel_folder_label.setIndent(8)

        self.horizontalLayout_4.addWidget(self.disabel_folder_label)

        self.disabel_folder_name = QLineEdit(SettingsWindow)
        self.disabel_folder_name.setObjectName(u"disabel_folder_name")
        self.disabel_folder_name.setEnabled(True)
        self.disabel_folder_name.setFont(font4)
        self.disabel_folder_name.setReadOnly(True)
        self.disabel_folder_name.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.disabel_folder_name)

        self.browse_disable_folder_button = QPushButton(SettingsWindow)
        self.browse_disable_folder_button.setObjectName(u"browse_disable_folder_button")
        self.browse_disable_folder_button.setFont(font4)

        self.horizontalLayout_4.addWidget(self.browse_disable_folder_button)

        self.horizontalLayout_4.setStretch(0, 11)
        self.horizontalLayout_4.setStretch(1, 20)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_3.setStretch(0, 6)

        self.retranslateUi(SettingsWindow)

        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.mod_move_method_label.setText(QCoreApplication.translate("SettingsWindow", u"\u041f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u043c\u043e\u0434\u043e\u0432:", None))
        self.before_game_start_rb.setText(QCoreApplication.translate("SettingsWindow", u"\u041f\u0435\u0440\u0435\u0434 \u0437\u0430\u043f\u0443\u0441\u043a\u043e\u043c \u0411\u041b", None))
        self.on_switch_rb.setText(QCoreApplication.translate("SettingsWindow", u"\u041f\u0440\u0438 \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0438/\u0432\u044b\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0438 \u043c\u043e\u0434\u0430", None))
        self.when_update_label.setText(QCoreApplication.translate("SettingsWindow", u"\u041a\u043e\u0433\u0434\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u044f\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u043c\u043e\u0434\u043e\u0432:", None))
        self.on_launch_update_rb.setText(QCoreApplication.translate("SettingsWindow", u"\u041f\u0440\u0438 \u0437\u0430\u043f\u0443\u0441\u043a\u0435 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440\u0430", None))
        self.on_button_click_rb.setText(QCoreApplication.translate("SettingsWindow", u"\u041f\u043e \u043d\u0430\u0436\u0430\u0442\u0438\u044e \u043a\u043d\u043e\u043f\u043a\u0438", None))
        self.path_label.setText(QCoreApplication.translate("SettingsWindow", u"\u041f\u0443\u0442\u0438 \u0434\u043b\u044f \u043f\u0430\u043f\u043e\u043a:", None))
        self.enabel_folder_label.setText(QCoreApplication.translate("SettingsWindow", u"\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043c\u043e\u0434\u043e\u0432:", None))
        self.browse_enabel_folder_button.setText(QCoreApplication.translate("SettingsWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.disabel_folder_label.setText(QCoreApplication.translate("SettingsWindow", u"\u041f\u0430\u043f\u043a\u0430 \u0434\u043b\u044f \u0432\u044b\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f: ", None))
        self.browse_disable_folder_button.setText(QCoreApplication.translate("SettingsWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
    # retranslateUi

