import numpy as np
import os
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

class GUI(basicgui.Ui_GUI, QtCore.QObject):

    sigPredict = QtCore.pyqtSignal(str,str)

    def __init__(self, app):
        QtCore.QObject.__init__(self)
        self.app = app
        self.mainwindow = QtWidgets.QMainWindow()
        self.qdir = QtCore.QDir()
        self.setupUi(self.mainwindow)

        # do stuff
        # chooseBurnsModel = CheckableDirModel()
        # self.burnTree.setModel(chooseBurnsModel)
        # self.burnTree.setRootIndex(chooseBurnsModel.index(self.qdir.absoluteFilePath('/home/n_crews/Documents/thesis/mlthesis/data/')))
        # self.burnTree.setRootIndex(chooseBurnsModel.index(QtGui.QDir.currentPath()));
        self.getFires()

        self.modelBrowseButton.clicked.connect(self.browseModels)
        self.predictButton.clicked.connect(self.predict)

        img = np.random.random((200,600))*255
        self.showImage(img,self.display)

        self.predictions = {}

        self.mainwindow.show()

    def getFires(self):
        burnFolder = 'data/'
        burns = util.listdir_nohidden(burnFolder)
        model = QtGui.QStandardItemModel()
        for name in burns:
            item = QtGui.QStandardItem(name)
            item.setCheckable(True)
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            # check = Qt.Unchecked
            # item.setCheckState(check)
            item.setCheckable(True)
            model.appendRow(item)

        self.datasetList.setModel(model)
        self.datasetList.clicked.connect(self.datasetClicked)

    def datasetClicked(self, item):
        print('clicked', item)

    def browseModels(self):
        # print('browsing!')
        fname = QtWidgets.QFileDialog.getExistingDirectory(directory='models/', options=QtWidgets.QFileDialog.ShowDirsOnly)
        if fname == '':
            return
        self.modelLineEdit.setText(fname)
        self.model = model.load(fname)
        img = viz.renderModel(self.model)
        self.showImage(self.modelDisplay, img)


    def predict(self):
        selectedBurns = []
        mod = self.datasetList.model()
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
