# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basicgui.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GUI(object):
    def setupUi(self, GUI):
        GUI.setObjectName("GUI")
        GUI.setEnabled(True)
        GUI.resize(588, 666)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GUI.sizePolicy().hasHeightForWidth())
        GUI.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(GUI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.datasetTab = QtWidgets.QWidget()
        self.datasetTab.setObjectName("datasetTab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.datasetTab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.dividerLine = QtWidgets.QFrame(self.datasetTab)
        self.dividerLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.dividerLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.dividerLine.setObjectName("dividerLine")
        self.verticalLayout.addWidget(self.dividerLine)
        self.inputLabel = QtWidgets.QLabel(self.datasetTab)
        self.inputLabel.setObjectName("inputLabel")
        self.verticalLayout.addWidget(self.inputLabel)
        self.frame = QtWidgets.QFrame(self.datasetTab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.burnTree = QtWidgets.QTreeView(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.burnTree.sizePolicy().hasHeightForWidth())
        self.burnTree.setSizePolicy(sizePolicy)
        self.burnTree.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.burnTree.setIndentation(20)
        self.burnTree.setSortingEnabled(True)
        self.burnTree.setObjectName("burnTree")
        self.burnTree.header().setVisible(False)
        self.burnTree.header().setStretchLastSection(False)
        self.horizontalLayout_3.addWidget(self.burnTree)
        self.burnDisplay = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.burnDisplay.sizePolicy().hasHeightForWidth())
        self.burnDisplay.setSizePolicy(sizePolicy)
        self.burnDisplay.setObjectName("burnDisplay")
        self.horizontalLayout_3.addWidget(self.burnDisplay)
        self.verticalLayout.addWidget(self.frame)
        self.display = QtWidgets.QLabel(self.datasetTab)
        self.display.setMinimumSize(QtCore.QSize(0, 300))
        self.display.setObjectName("display")
        self.verticalLayout.addWidget(self.display)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.datasetTab, "")
        self.modelTab = QtWidgets.QWidget()
        self.modelTab.setObjectName("modelTab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.modelTab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.modelLabel = QtWidgets.QLabel(self.modelTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modelLabel.sizePolicy().hasHeightForWidth())
        self.modelLabel.setSizePolicy(sizePolicy)
        self.modelLabel.setObjectName("modelLabel")
        self.horizontalLayout_2.addWidget(self.modelLabel)
        self.modelLineEdit = QtWidgets.QLineEdit(self.modelTab)
        self.modelLineEdit.setObjectName("modelLineEdit")
        self.horizontalLayout_2.addWidget(self.modelLineEdit)
        self.modelBrowseButton = QtWidgets.QPushButton(self.modelTab)
        self.modelBrowseButton.setObjectName("modelBrowseButton")
        self.horizontalLayout_2.addWidget(self.modelBrowseButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.modelDisplay = QtWidgets.QLabel(self.modelTab)
        self.modelDisplay.setObjectName("modelDisplay")
        self.verticalLayout_3.addWidget(self.modelDisplay)
        self.verticalLayout_8.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.modelTab, "")
        self.trainTab = QtWidgets.QWidget()
        self.trainTab.setObjectName("trainTab")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.trainTab)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.tabWidget.addTab(self.trainTab, "")
        self.predictTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.predictTab.sizePolicy().hasHeightForWidth())
        self.predictTab.setSizePolicy(sizePolicy)
        self.predictTab.setObjectName("predictTab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.predictTab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.predictButton = QtWidgets.QPushButton(self.predictTab)
        self.predictButton.setObjectName("predictButton")
        self.verticalLayout_4.addWidget(self.predictButton)
        self.predictDisplay = QtWidgets.QLabel(self.predictTab)
        self.predictDisplay.setObjectName("predictDisplay")
        self.verticalLayout_4.addWidget(self.predictDisplay)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.predictTab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        GUI.setCentralWidget(self.centralwidget)
        self.actionN = QtWidgets.QAction(GUI)
        self.actionN.setCheckable(True)
        self.actionN.setChecked(True)
        self.actionN.setObjectName("actionN")
        self.actionKg = QtWidgets.QAction(GUI)
        self.actionKg.setCheckable(True)
        self.actionKg.setObjectName("actionKg")
        self.actionLbs = QtWidgets.QAction(GUI)
        self.actionLbs.setCheckable(True)
        self.actionLbs.setObjectName("actionLbs")
        self.actionOpenCal = QtWidgets.QAction(GUI)
        self.actionOpenCal.setShortcut("")
        self.actionOpenCal.setObjectName("actionOpenCal")
        self.actionSaveCal = QtWidgets.QAction(GUI)
        self.actionSaveCal.setObjectName("actionSaveCal")
        self.actionSaveCalAs = QtWidgets.QAction(GUI)
        self.actionSaveCalAs.setObjectName("actionSaveCalAs")
        self.actionSave_2 = QtWidgets.QAction(GUI)
        self.actionSave_2.setObjectName("actionSave_2")
        self.actionOpenRec = QtWidgets.QAction(GUI)
        self.actionOpenRec.setObjectName("actionOpenRec")
        self.actionSaveRec = QtWidgets.QAction(GUI)
        self.actionSaveRec.setObjectName("actionSaveRec")
        self.actionSaveRecAs = QtWidgets.QAction(GUI)
        self.actionSaveRecAs.setObjectName("actionSaveRecAs")
        self.actionExportSnippet = QtWidgets.QAction(GUI)
        self.actionExportSnippet.setObjectName("actionExportSnippet")
        self.actionNew_Dataset = QtWidgets.QAction(GUI)
        self.actionNew_Dataset.setObjectName("actionNew_Dataset")
        self.modelLabel.setBuddy(self.modelBrowseButton)

        self.retranslateUi(GUI)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GUI)

    def retranslateUi(self, GUI):
        _translate = QtCore.QCoreApplication.translate
        GUI.setWindowTitle(_translate("GUI", "Hot Topic"))
        self.inputLabel.setText(_translate("GUI", "Burns and Dates:"))
        self.burnDisplay.setText(_translate("GUI", "TextLabel"))
        self.display.setText(_translate("GUI", "Display"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.datasetTab), _translate("GUI", "Dataset"))
        self.modelLabel.setText(_translate("GUI", "Model:"))
        self.modelLineEdit.setText(_translate("GUI", "None set..."))
        self.modelBrowseButton.setText(_translate("GUI", "Browse..."))
        self.modelDisplay.setText(_translate("GUI", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.modelTab), _translate("GUI", "Model"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.trainTab), _translate("GUI", "Train"))
        self.predictButton.setText(_translate("GUI", "Predict!"))
        self.predictDisplay.setText(_translate("GUI", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.predictTab), _translate("GUI", "Predict"))
        self.actionN.setText(_translate("GUI", "N"))
        self.actionKg.setText(_translate("GUI", "kg"))
        self.actionLbs.setText(_translate("GUI", "lbs"))
        self.actionOpenCal.setText(_translate("GUI", "Open..."))
        self.actionSaveCal.setText(_translate("GUI", "Save"))
        self.actionSaveCalAs.setText(_translate("GUI", "Save As..."))
        self.actionSave_2.setText(_translate("GUI", "Save"))
        self.actionOpenRec.setText(_translate("GUI", "Open..."))
        self.actionSaveRec.setText(_translate("GUI", "Save"))
        self.actionSaveRecAs.setText(_translate("GUI", "Save As..."))
        self.actionExportSnippet.setText(_translate("GUI", "Export Snippet..."))
        self.actionNew_Dataset.setText(_translate("GUI", "New Dataset..."))

