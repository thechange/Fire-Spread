import os
import numpy as np
import cv2
import multiprocessing
from PyQt5 import QtCore, QtGui, QtWidgets, uic

# dynamically generate the gui skeleton file from the ui file
with open('basicgui.py', 'w') as pyfile:
    uic.compileUi('basicgui.ui', pyfile)
import basicgui

from lib import rawdata
from lib import dataset
from lib import util
from lib import model
from lib import viz

class GUI(basicgui.Ui_GUI, QtCore.QObject):

    sigPredict = QtCore.pyqtSignal(str,str)

    def __init__(self, app):
        QtCore.QObject.__init__(self)
        self.app = app
        self.mainwindow = QtWidgets.QMainWindow()
        self.setupUi(self.mainwindow)

        self.data = rawdata.load()
        self.model = None
        self.dataset = None

        # do stuff
        self.initBurnTree()

        self.modelBrowseButton.clicked.connect(self.browseModels)
        self.loadDatasetButton.clicked.connect(self.browseDatasets)
        self.predictButton.clicked.connect(self.predict)

        # img = np.random.random((200,600))*255
        # self.showImage(img,self.display)
        # self.predictions = {}

        self.mainwindow.show()

    def initBurnTree(self):
        model = QtGui.QStandardItemModel()
        self.burnTree.setModel(model)
        burns = sorted(self.data.burns.keys())
        for name in burns:
            burnItem = QtGui.QStandardItem(name)
            burnItem.setSelectable(True)
            model.appendRow(burnItem)
            dates = sorted(self.data.burns[name].days.keys())
            for d in dates:
                dateItem = QtGui.QStandardItem(d)
                # dateItem.setCheckable(True)
                # dateItem.setCheckState(QtCore.Qt.Unchecked)
                dateItem.setSelectable(True)
                burnItem.appendRow(dateItem)
        self.burnTree.setColumnWidth(0, 300)
        self.burnTree.expandAll()
        self.burnTree.selectionModel().selectionChanged.connect(self.burnDataSelected)

    def burnDataSelected(self, selected, deselected):
        idx = selected.indexes()[0]
        item = self.burnTree.model().itemFromIndex(idx)
        p = item.parent()
        if p is None:
            # must have selected a burn, not a date
            self.displayBurn(item.text())
        else:
            # selected a date
            self.displayDay(p.text(), item.text())

    def displayBurn(self, burnName):
        burn = self.data.burns[burnName]
        dem = viz.renderBurn(burn)
        SIZE = (400,300)
        resized = cv2.resize(dem, SIZE)
        self.showImage(resized, self.burnDisplay)

    def displayDay(self, burnName, date):
        day = self.data.burns[burnName].days[date]
        img = viz.renderDay(day)
        SIZE = (400,300)
        resized = cv2.resize(img, SIZE)
        self.showImage(resized, self.burnDisplay)
        # print('displaying day:', day)

    def browseModels(self):
        # print('browsing!')
        fname = QtWidgets.QFileDialog.getExistingDirectory(directory='models/', options=QtWidgets.QFileDialog.ShowDirsOnly)
        try:
            self.model = model.load(fname)
            self.modelLineEdit.setText(fname)
            self.predictModelLineEdit.setText(fname)
            self.trainModelLineEdit.setText(fname)
        except:
            print('could not open that model')
        # img = viz.renderModel(self.model)
        # self.showImage(self.modelDisplay, img)

    def browseDatasets(self):
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(directory='datasets/', filter="numpy archives (*.npz)")
        try:
            self.dataset = dataset.load(fname)
            self.datasetDatasetLineEdit.setText(fname)
            self.trainDatasetLineEdit.setText(fname)
            self.predictDatasetLineEdit.setText(fname)
        except Exception as e:
            print('Could not open that dataset:', e)


    def predict(self):
        selectedBurns = []
        mod = self.burnTree.model()
        for index in range(mod.rowCount()):
            i = mod.item(index)
            # print(i.checkState())
            if i.checkState() == QtCore.Qt.Checked:
                selectedBurns.append(i.text())
        print('opening the data for the burns,', selectedBurns)
        data = rawdata.RawData.load(burnNames=selectedBurns, dates='all')
        ds = dataset.Dataset(data, dataset.Dataset.vulnerablePixels)

        from lib import model
        modelFileName = self.modelLineEdit.text()
        print('loading model', modelFileName)
        mod = model.load(modelFileName)
        print(mod)
        # predictions = mod.predict(ds)
        # self.predictions.update(predictions)
        # print('opening modelFileName!')
        # todo: load keras model
        # self.sigPredict.emit(modelFileName, burnName)

    def donePredicting():
        pass

    @staticmethod
    def showImage(img, label):
        if img.dtype.kind == 'f':
            # convert from float to uint8
            img = (img*255).astype(np.uint8)
        assert img.dtype == np.uint8
        if len(img.shape) > 2:
            # color images
            h, w, bytesPerComponent = img.shape
            bytesPerLine = bytesPerComponent * w;
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            QI=QtGui.QImage(img.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
        else:
            # black and white images
            h,w = img.shape[:2]
            QI=QtGui.QImage(img, w, h, QtGui.QImage.Format_Indexed8)
        # QI.setColorTable(COLORTABLE)
        label.setPixmap(QtGui.QPixmap.fromImage(QI))

class CheckableDirModel(QtWidgets.QDirModel):
    def __init__(self, parent=None):
        QtGui.QDirModel.__init__(self, None)
        self.checks = {}

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.CheckStateRole:
            return QtGui.QDirModel.data(self, index, role)
        else:
            if index.column() == 0:
                return self.checkState(index)

    def flags(self, index):
        return QtGui.QDirModel.flags(self, index) | QtCore.Qt.ItemIsUserCheckable

    def checkState(self, index):
        if index in self.checks:
            return self.checks[index]
        else:
            return QtCore.Qt.Unchecked

    def setData(self, index, value, role):
        if (role == QtCore.Qt.CheckStateRole and index.column() == 0):
            self.checks[index] = value
            self.emit(QtCore.SIGNAL("dataChanged(QModelIndex,QModelIndex)"), index, index)
            return True

        return QtGui.QDirModel.setData(self, index, value, role)

def async(func, args, callback):
    pass

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    gui = GUI(app)

    app.exec_()
