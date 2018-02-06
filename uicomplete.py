# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ytgui.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ytcode import Youtube
import pytube

class Ui_YtGUI(object):
    def __init__(self):
        self.combobox_list = [{'id': '0', 'res': '<Select One>'}]
    def setupUi(self, YtGUI):
        YtGUI.setObjectName("YtGUI")
        YtGUI.resize(672, 336)
        YtGUI.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(238, 238, 236);")
        self.centralWidget = QtWidgets.QWidget(YtGUI)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(238, 238, 236);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame)

        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        # Download location
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)

        self.fetch_button = QtWidgets.QPushButton(self.frame)
        self.fetch_button.setObjectName('fetch_button')
        self.verticalLayout_2.addWidget(self.fetch_button)
        self.fetch_button.clicked.connect(self.fetch_data)

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        # Download link
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        #self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)

        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")


        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setBaseSize(QtCore.QSize(200, 100))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton.clicked.connect(self.download)

        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 50))
        self.comboBox.setObjectName("comboBox")
        for data in self.combobox_list:
            self.comboBox.addItem(data['res'], data['id'])

        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)

        YtGUI.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(YtGUI)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 672, 22))
        self.menuBar.setObjectName("menuBar")
        YtGUI.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(YtGUI)
        self.statusBar.setObjectName("statusBar")
        self.progressBar = QtWidgets.QProgressBar(self.statusBar)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.statusBar.addWidget(self.progressBar)
        self.progressBar.hide()
        YtGUI.setStatusBar(self.statusBar)

        self.retranslateUi(YtGUI)
        QtCore.QMetaObject.connectSlotsByName(YtGUI)

    def retranslateUi(self, YtGUI):
        _translate = QtCore.QCoreApplication.translate
        YtGUI.setWindowTitle(_translate("YtGUI", "YouTube Downloader"))
        self.label_2.setText(_translate("YtGUI", "<html><head/><body><p>Destination Path(Optional): </p></body></html>"))
        self.label.setText(_translate("YtGUI", "Youtube url link : "))
        self.pushButton.setText(_translate("YtGUI", "Download"))
        self.fetch_button.setText(_translate("YtGUI", "Fetch"))
        self.label_3.setText(_translate("YtGUI", "Select a Category: "))

    def fetch_data(self):
        _translate = QtCore.QCoreApplication.translate
        link = self.textEdit.toPlainText()
        print(str(link))
        self.yt_ins = pytube.YouTube(link)
        self.pralay = Youtube(self.yt_ins)
        self.comboBox.clear()
        for data in self.pralay.category:
            self.comboBox.addItem(data['res'], data['id'])
        self.pushButton.setText(_translate("YtGUI", "Download"))

    def download(self):
        _translate = QtCore.QCoreApplication.translate
        # link = self.textEdit.text()
        # self.yt_ins = pytube.YouTube(link)
        # self.pralay = Youtube(self.yt_ins)
        self.download_loc = self.lineEdit.text()
        itag = self.comboBox.currentText().split()[0]
        self.comboBox.clear()
        self.lineEdit.clear()
        self.textEdit.clear()

        print(str(itag))
        if str(self.download_loc) == "":
            try:
                # self.progressBar.show()
                # self.pralay.get_instance().register_on_progress_callback(self.setProgress)
                self.pralay.get_instance().streams.get_by_itag(int(itag)).download()
            except:
                self.label_2.setText(_translate("YtGUI", "Something went wrong"))
        else:
            try:
                # self.pralay.streams.download(self.download_loc)
                # self.pralay.on_progress(self.setProgress)
                # self.pralay.get_instance().register_on_progress_callback(self.setProgress)
                # self.pralay.get_instance().register_on_complete_callback(self.on_complete)
                # self.progressBar.show()
                self.pralay.get_instance().streams.get_by_itag(int(itag)).download(self.download_loc)
            except:
                self.label_2.setText(_translate("YtGUI", "Missing Destination"))

    def setProgress(self, stream, chunk, file_handle, bytes_remaining):
        rem_byte = bytes_remaining
        size = stream.filesize()
        complete = size-rem_byte
        complete = complete * 100 / size
        # while complete < 100:
        self.progressBar.setProperty("value", complete)


    def on_complete(self, stream, file_handle):
        self.progressBar.hide()
