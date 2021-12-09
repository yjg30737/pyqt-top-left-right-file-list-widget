from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QFileDialog, QCheckBox, QApplication

from simplePyQt5.styleApplier import StyleApplier

from pyqt_top_left_right_file_list_widget.fileListWidget import FileListWidget
from simplePyQt5.topLabelBottomWidget import TopLabelBottomWidget


class TopLeftRightFileListWidget(QWidget):
    fileAdded = pyqtSignal(list)
    fileRemoved = pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ext_lst = ''
        self.__initUi()

    def __initUi(self):
        self.__addBtn = QPushButton()
        self.__delBtn = QPushButton()
        self.__clearBtn = QPushButton()

        self.__addBtn.clicked.connect(self.__add)
        self.__delBtn.clicked.connect(self.__delete)
        self.__clearBtn.clicked.connect(self.__clear)

        applier = StyleApplier()
        btns = [self.__addBtn, self.__delBtn, self.__clearBtn]
        applier.setCssFile('../style/button.css', btns)
        applier.setIconAutomatically(['add', 'delete', 'clear'], btns)
        applier.setToolTip(['Add', 'Delete', 'Clear'], btns)

        self.__fileListWidget = FileListWidget()
        self.__fileListWidget.currentItemChanged.connect(self.__currentItemChanged)

        self.__onlyFileNameChkBox = QCheckBox('Show file name only')
        self.__onlyFileNameChkBox.stateChanged.connect(self.__fileListWidget.setOnlyFileName)

        self.__mainWidget = TopLabelBottomWidget()
        self.__mainWidget.setLabel('List of files')
        self.__mainWidget.setLeftWidgets([self.__onlyFileNameChkBox])
        self.__mainWidget.setRightWidgets(btns)
        self.__mainWidget.addBottomWidget(self.__fileListWidget)

        lay = self.__mainWidget.layout()
        lay.setContentsMargins(5, 5, 5, 5)
        self.setLayout(lay)

        self.__btnToggled()

    def __currentItemChanged(self, i1, i2):
        self.__btnToggled()

    def __btnToggled(self):
        f1 = self.__fileListWidget.count() > 0
        f2 = True if self.__fileListWidget.currentItem() else False
        self.__delBtn.setEnabled(f1 and f2)
        self.__clearBtn.setEnabled(f1)
        
    def setLabel(self, text):
        self.__mainWidget.setLabel(text)

    def setStrExtFilesToOpen(self, ext_lst):
        self.__ext_lst = ext_lst

    def __add(self):
        ext_lst = self.__ext_lst if self.__ext_lst else 'All Files (*.*)'
        filenames = QFileDialog.getOpenFileNames(self, 'Open Files', '', ext_lst)
        if filenames[0]:
            filenames = filenames[0]
            self.__fileListWidget.setDatas(filenames)
            self.fileAdded.emit(filenames)
            self.__btnToggled()

    def __delete(self):
        filenames = self.__fileListWidget.getSelectedFileNames()
        self.__fileListWidget.removeSelectedRows()
        self.__btnToggled()

        self.fileRemoved.emit(filenames)

    def __clear(self):
        self.__fileListWidget.clear()
        self.__btnToggled()


