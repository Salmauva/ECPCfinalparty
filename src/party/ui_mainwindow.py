# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QHBoxLayout,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(883, 649)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plot_widget = PlotWidget(self.centralwidget)
        self.plot_widget.setObjectName(u"plot_widget")

        self.verticalLayout.addWidget(self.plot_widget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.clear_button = QPushButton(self.centralwidget)
        self.clear_button.setObjectName(u"clear_button")

        self.horizontalLayout_2.addWidget(self.clear_button)

        self.save_data = QPushButton(self.centralwidget)
        self.save_data.setObjectName(u"save_data")

        self.horizontalLayout_2.addWidget(self.save_data)

        self.device_button = QComboBox(self.centralwidget)
        self.device_button.setObjectName(u"device_button")

        self.horizontalLayout_2.addWidget(self.device_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_min_button = QDoubleSpinBox(self.centralwidget)
        self.add_min_button.setObjectName(u"add_min_button")
        self.add_min_button.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.add_min_button.setMaximum(3.300000000000000)
        self.add_min_button.setSingleStep(0.010000000000000)

        self.horizontalLayout.addWidget(self.add_min_button)

        self.add_max_button = QDoubleSpinBox(self.centralwidget)
        self.add_max_button.setObjectName(u"add_max_button")
        self.add_max_button.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.add_max_button.setMaximum(3.300000000000000)
        self.add_max_button.setSingleStep(0.010000000000000)
        self.add_max_button.setValue(3.300000000000000)

        self.horizontalLayout.addWidget(self.add_max_button)

        self.add_numpoints_button = QSpinBox(self.centralwidget)
        self.add_numpoints_button.setObjectName(u"add_numpoints_button")
        self.add_numpoints_button.setValue(2)

        self.horizontalLayout.addWidget(self.add_numpoints_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 883, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.save_data.setText(QCoreApplication.translate("MainWindow", u"Save data", None))
        self.add_min_button.setPrefix(QCoreApplication.translate("MainWindow", u"Start value [V]: ", None))
        self.add_max_button.setPrefix(QCoreApplication.translate("MainWindow", u"Stop value [V]: ", None))
        self.add_numpoints_button.setPrefix(QCoreApplication.translate("MainWindow", u"Measurments: ", None))
    # retranslateUi

