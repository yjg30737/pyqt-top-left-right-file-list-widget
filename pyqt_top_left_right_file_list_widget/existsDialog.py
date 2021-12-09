from PyQt5.QtWidgets import QDialog, QLabel, QListWidgetItem, \
    QCheckBox
from PyQt5.QtCore import Qt, pyqtSignal

from simplePyQt5.okCancelWidget import OkCancelWidget
from simplePyQt5.leftRightWidget import LeftRightWidget
from simplePyQt5.topLeftRightWidget import TopLeftRightWidget

import pyqt_top_left_right_file_list_widget


class ExistsDialog(QDialog):
    dontAskAgainChecked = pyqtSignal(bool)
    
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle('Notice')
        self.setFixedSize(self.sizeHint())
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.__listWidget = pyqt_top_left_right_file_list_widget.fileListWidget.FileListWidget()
        self.__listWidget.setAcceptDrops(False)
        self.__listWidget.setFixedHeight(300)
        
        self.__exists_text = '{0} of files already exists.'
        self.__existsLbl = QLabel(self.__exists_text.format(''))
        self.__onlyFileNameChkBox = QCheckBox('Show file name only')
        self.__onlyFileNameChkBox.stateChanged.connect(self.__listWidget.setOnlyFileName)

        topWidget = LeftRightWidget()
        topWidget.setLeftWidgets([self.__existsLbl])
        topWidget.setRightWidgets([self.__onlyFileNameChkBox])

        self.__dontAskAgainChkBox = QCheckBox("Don't ask again")
        self.__dontAskAgainChkBox.stateChanged.connect(self.__sendDontAskAgainSignal)

        okCancelWidget = OkCancelWidget(self)
        okBtn, cancelBtn = okCancelWidget.getOkCancelBtn()

        okBtn.clicked.connect(self.accept)
        cancelBtn.clicked.connect(self.close)

        bottomWidget = LeftRightWidget()
        bottomWidget.setLeftWidgets([self.__dontAskAgainChkBox])
        bottomWidget.setRightWidgets([okCancelWidget])

        mainWidget = TopLeftRightWidget()
        mainWidget.addBottomWidget(topWidget)
        mainWidget.addBottomWidget(self.__listWidget)
        mainWidget.addBottomWidget(QLabel('Apply except for files above.'))
        mainWidget.addSeparator()
        mainWidget.addBottomWidget(bottomWidget)
        lay = mainWidget.layout()
        lay.setContentsMargins(5, 5, 5, 5)

        self.setLayout(lay)
        
    def setDontAskAgainChecked(self, f: bool):
        self.__dontAskAgainChkBox.setChecked(f)

    def setExistFiles(self, files):
        self.__existsLbl.setText(self.__exists_text.format(len(files)))
        self.__setList(files)

    def __setList(self, files):
        for file in files:
            item = ''
            if isinstance(file, str):
                item = QListWidgetItem(file)
            elif isinstance(file, QListWidgetItem):
                item = QListWidgetItem(file.text())
            self.__listWidget.addItem(item)

    def setOnlyFilename(self, state):
        self.__onlyFileNameChkBox.setChecked(state == Qt.Checked)
        
    def __sendDontAskAgainSignal(self, state):
        self.dontAskAgainChecked.emit(state == Qt.Checked)