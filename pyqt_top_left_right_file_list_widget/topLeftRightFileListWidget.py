from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QFileDialog, QCheckBox

from pyqt_file_list_widget.fileListWidget import FileListWidget
from pyqt_svg_icon_pushbutton import SvgIconPushButton
from simplePyQt5.topLabelBottomWidget import TopLabelBottomWidget


class TopLeftRightFileListWidget(QWidget):
    fileAdded = pyqtSignal(list)
    fileRemoved = pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__extensions = ''
        self.__initUi()

    def __initUi(self):
        self.__addBtn = SvgIconPushButton()
        self.__delBtn = SvgIconPushButton()
        self.__clearBtn = SvgIconPushButton()

        self.__addBtn.setIcon('ico/add.svg')
        self.__delBtn.setIcon('ico/delete.svg')
        self.__clearBtn.setIcon('ico/clear.svg')

        self.__addBtn.clicked.connect(self.__add)
        self.__delBtn.clicked.connect(self.__delete)
        self.__clearBtn.clicked.connect(self.__clear)

        btns = [self.__addBtn, self.__delBtn, self.__clearBtn]

        self.__addBtn.setToolTip('Add')
        self.__delBtn.setToolTip('Delete')
        self.__clearBtn.setToolTip('Clear')

        self.__fileListWidget = FileListWidget()
        self.__fileListWidget.currentItemChanged.connect(self.__currentItemChanged)

        self.__onlyFileNameChkBox = QCheckBox('Show file name only')
        self.__onlyFileNameChkBox.stateChanged.connect(self.__fileListWidget.setFilenameOnly)

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

    def setExtensions(self, extensions: list):
        self.__extensions = extensions

    def __add(self):
        ext_lst = self.__extensions if self.__extensions else 'All Files (*.*)'
        filenames = QFileDialog.getOpenFileNames(self, 'Open Files', '', ext_lst)
        if filenames[0]:
            filenames = filenames[0]
            self.__fileListWidget.addFilenames(filenames)
            self.fileAdded.emit(filenames)
            self.__btnToggled()

    def __delete(self):
        filenames = self.__fileListWidget.getSelectedFilenames()
        self.__fileListWidget.removeSelectedRows()
        self.__btnToggled()

        self.fileRemoved.emit(filenames)

    def __clear(self):
        self.__fileListWidget.clear()
        self.__btnToggled()


