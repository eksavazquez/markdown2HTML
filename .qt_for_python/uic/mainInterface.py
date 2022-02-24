# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainInterface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ImageViewerWindow(object):
    def setupUi(self, ImageViewerWindow):
        if not ImageViewerWindow.objectName():
            ImageViewerWindow.setObjectName(u"ImageViewerWindow")
        ImageViewerWindow.resize(1080, 800)
        self.centralwidget = QWidget(ImageViewerWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u"../icons/Save-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton)

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        icon1 = QIcon()
        icon1.addFile(u"../icons/md-to-html.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveButton.setIcon(icon1)
        self.saveButton.setIconSize(QSize(50, 25))

        self.horizontalLayout.addWidget(self.saveButton)

        self.currentFile = QLabel(self.centralwidget)
        self.currentFile.setObjectName(u"currentFile")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentFile.sizePolicy().hasHeightForWidth())
        self.currentFile.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.currentFile)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_2.addWidget(self.textEdit)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout_2.addWidget(self.graphicsView)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        ImageViewerWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ImageViewerWindow)
        self.statusbar.setObjectName(u"statusbar")
        ImageViewerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ImageViewerWindow)

        QMetaObject.connectSlotsByName(ImageViewerWindow)
    # setupUi

    def retranslateUi(self, ImageViewerWindow):
        ImageViewerWindow.setWindowTitle(QCoreApplication.translate("ImageViewerWindow", u"Example Image Viewer", None))
        self.pushButton.setText("")
        self.saveButton.setText("")
        self.currentFile.setText(QCoreApplication.translate("ImageViewerWindow", u"No file selected", None))
    # retranslateUi

