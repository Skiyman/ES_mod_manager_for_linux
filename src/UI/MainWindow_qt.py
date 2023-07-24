# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_Es_mod_namager_linux(object):
    def setupUi(self, Es_mod_namager_linux):
        if not Es_mod_namager_linux.objectName():
            Es_mod_namager_linux.setObjectName(u"Es_mod_namager_linux")
        Es_mod_namager_linux.resize(560, 615)
        self.mods_path_settings = QAction(Es_mod_namager_linux)
        self.mods_path_settings.setObjectName(u"mods_path_settings")
        self.abbout_guide = QAction(Es_mod_namager_linux)
        self.abbout_guide.setObjectName(u"abbout_guide")
        self.abbout_program = QAction(Es_mod_namager_linux)
        self.abbout_program.setObjectName(u"abbout_program")
        self.main_widget = QWidget(Es_mod_namager_linux)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setMinimumSize(QSize(560, 547))
        self.verticalLayout_2 = QVBoxLayout(self.main_widget)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 8)
        self.main_layout = QVBoxLayout()
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(-1, -1, -1, 0)
        self.list_view_layout = QGridLayout()
        self.list_view_layout.setObjectName(u"list_view_layout")
        self.list_view_layout.setContentsMargins(-1, -1, -1, 8)
        self.enabled_mods_label = QLabel(self.main_widget)
        self.enabled_mods_label.setObjectName(u"enabled_mods_label")
        font = QFont()
        font.setPointSize(12)
        self.enabled_mods_label.setFont(font)
        self.enabled_mods_label.setAlignment(Qt.AlignCenter)

        self.list_view_layout.addWidget(self.enabled_mods_label, 0, 0, 1, 1)

        self.disabled_mods_label = QLabel(self.main_widget)
        self.disabled_mods_label.setObjectName(u"disabled_mods_label")
        self.disabled_mods_label.setFont(font)
        self.disabled_mods_label.setAlignment(Qt.AlignCenter)

        self.list_view_layout.addWidget(self.disabled_mods_label, 0, 1, 1, 1)

        self.enabled_mods_list = QListWidget(self.main_widget)
        self.enabled_mods_list.setObjectName(u"enabled_mods_list")

        self.list_view_layout.addWidget(self.enabled_mods_list, 1, 0, 1, 1)

        self.disabled_mods_list = QListWidget(self.main_widget)
        self.disabled_mods_list.setObjectName(u"disabled_mods_list")

        self.list_view_layout.addWidget(self.disabled_mods_list, 1, 1, 1, 1)


        self.main_layout.addLayout(self.list_view_layout)

        self.btn_layout = QHBoxLayout()
        self.btn_layout.setObjectName(u"btn_layout")
        self.btn_layout.setContentsMargins(-1, 5, -1, -1)
        self.btn_enable_all = QPushButton(self.main_widget)
        self.btn_enable_all.setObjectName(u"btn_enable_all")

        self.btn_layout.addWidget(self.btn_enable_all)

        self.btn_disable_all = QPushButton(self.main_widget)
        self.btn_disable_all.setObjectName(u"btn_disable_all")

        self.btn_layout.addWidget(self.btn_disable_all)

        self.btn_update_mods_db = QPushButton(self.main_widget)
        self.btn_update_mods_db.setObjectName(u"btn_update_mods_db")
        self.btn_update_mods_db.setCheckable(False)

        self.btn_layout.addWidget(self.btn_update_mods_db)

        self.btn_Launch_es = QPushButton(self.main_widget)
        self.btn_Launch_es.setObjectName(u"btn_Launch_es")

        self.btn_layout.addWidget(self.btn_Launch_es)

        self.btn_layout.setStretch(0, 2)
        self.btn_layout.setStretch(1, 2)
        self.btn_layout.setStretch(3, 5)

        self.main_layout.addLayout(self.btn_layout)


        self.verticalLayout_2.addLayout(self.main_layout)

        Es_mod_namager_linux.setCentralWidget(self.main_widget)
        self.menubar = QMenuBar(Es_mod_namager_linux)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 560, 30))
        self.settings_menu = QMenu(self.menubar)
        self.settings_menu.setObjectName(u"settings_menu")
        self.abbout_menu = QMenu(self.menubar)
        self.abbout_menu.setObjectName(u"abbout_menu")
        Es_mod_namager_linux.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Es_mod_namager_linux)
        self.statusbar.setObjectName(u"statusbar")
        Es_mod_namager_linux.setStatusBar(self.statusbar)

        self.menubar.addAction(self.settings_menu.menuAction())
        self.menubar.addAction(self.abbout_menu.menuAction())
        self.settings_menu.addAction(self.mods_path_settings)
        self.abbout_menu.addAction(self.abbout_guide)
        self.abbout_menu.addAction(self.abbout_program)

        self.retranslateUi(Es_mod_namager_linux)

        QMetaObject.connectSlotsByName(Es_mod_namager_linux)
    # setupUi

    def retranslateUi(self, Es_mod_namager_linux):
        Es_mod_namager_linux.setWindowTitle(QCoreApplication.translate("Es_mod_namager_linux", u"ES mod manager for Linux", None))
        self.mods_path_settings.setText(QCoreApplication.translate("Es_mod_namager_linux", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438...", None))
        self.abbout_guide.setText(QCoreApplication.translate("Es_mod_namager_linux", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430 \u043f\u043e \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u044e", None))
        self.abbout_program.setText(QCoreApplication.translate("Es_mod_namager_linux", u"\u041e \u043c\u043d\u0435\u043d\u0434\u0436\u0435\u0440\u0435", None))
        self.enabled_mods_label.setText(QCoreApplication.translate("Es_mod_namager_linux", u"\u0412\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u044b\u0435 \u043c\u043e\u0434\u044b", None))
        self.disabled_mods_label.setText(QCoreApplication.translate("Es_mod_namager_linux", u"\u0412\u044b\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u044b\u0435 \u043c\u043e\u0434\u044b", None))
        self.btn_enable_all.setText(QCoreApplication.translate("Es_mod_namager_linux", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0432\u0441\u0435", None))
        self.btn_disable_all.setText(QCoreApplication.translate("Es_mod_namager_linux", u"\u0412\u044b\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0432\u0441\u0435", None))
        self.btn_update_mods_db.setText(QCoreApplication.translate("Es_mod_namager_linux", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c c\u043f\u0438\u0441\u043e\u043a \u043c\u043e\u0434\u043e\u0432", None))
        self.btn_Launch_es.setText(QCoreApplication.translate("Es_mod_namager_linux", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0411\u041b", None))
        self.settings_menu.setTitle(QCoreApplication.translate("Es_mod_namager_linux", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.abbout_menu.setTitle(QCoreApplication.translate("Es_mod_namager_linux", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi

