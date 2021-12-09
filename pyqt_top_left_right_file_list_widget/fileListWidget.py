from collections import defaultdict

from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QDialog, QAbstractItemView
from PyQt5.QtCore import Qt
import os, sys

from pyqt_top_left_right_file_list_widget.existsDialog import ExistsDialog


class FileListWidget(QListWidget):
    __ext_lst = []
    _basename_absname_dict = defaultdict(str)
    _only_filename_flag = False

    drag_and_drop_filename = ''

    def __init__(self):
        super().__init__()
        self.__existsDialogDontAskAgainChecked = False
        self._initUi()

    def _initUi(self):
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setAcceptDrops(True)

    def setExtList(self, ext_lst):
        self.__ext_lst = ext_lst

    def setData(self, filename):
        item = QListWidgetItem(filename)
        absname = item.text()
        basename = os.path.basename(absname)
        self._basename_absname_dict[basename] = absname
        if self._only_filename_flag:
            item.setText(basename)
        else:
            item.setText(absname)
        self.addItem(item)

    def setDatas(self, filenames):
        exists_file_lst = []
        not_exists_file_lst = []
        for filename in filenames:
            filename_to_find = os.path.basename(filename) if self._only_filename_flag else filename
            items = self.findItems(filename_to_find, Qt.MatchFixedString)
            if items:
                exists_file_lst.append(items[0])
            else:
                not_exists_file_lst.append(filename)
        if exists_file_lst:
            dialog = ExistsDialog()
            dialog.setDontAskAgainChecked(self.__existsDialogDontAskAgainChecked)
            dialog.setExistFiles(exists_file_lst)
            reply = dialog.exec()
            if reply == QDialog.Accepted:
                for filename in not_exists_file_lst:
                    self.setData(filename)
                return
            else:
                return
        else:
            for filename in not_exists_file_lst:
                self.setData(filename)

    def setOnlyFileName(self, flag: bool):
        self._only_filename_flag = flag
        self.setItemAsBaseName(flag)

    def setItem(self, item: QListWidgetItem):
        absname = item.text()
        basename = os.path.basename(absname)
        self._basename_absname_dict[basename] = absname
        if self._only_filename_flag:
            item.setText(basename)
        else:
            item.setText(absname)
        self.addItem(item)

    def remove(self, item: QListWidgetItem):
        filename = item.text()
        self.takeItem(self.row(item))
        self._basename_absname_dict.pop(os.path.basename(filename))

    def getSelectedFileNames(self):
        items = self.selectedItems()
        filenames = [item.text() for item in items]
        return filenames

    def removeSelectedRows(self):
        items = self.selectedItems()
        if items:
            items = reversed(items)
            for item in items:
                self.remove(item)

    def clear(self):
        for i in range(self.count()-1, -1, -1):
            self.remove(self.item(i))
        super().clear()

    def isOnlyFileName(self):
        return self._only_filename_flag

    def getAbsFileName(self, basename):
        return self._basename_absname_dict[basename]

    def __getExtFilteredFiles(self, lst):
        if len(self.__ext_lst) > 0:
            return list(map(lambda x: x if os.path.splitext(x)[-1] in self.__ext_lst else None, lst))
        else:
            return lst

    def __getFileNames(self, urls):
        return list(map(lambda x: x.path()[1:], urls))

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.accept()

    def dragMoveEvent(self, e):
        pass

    def dropEvent(self, e):
        filenames = [file for file in self.__getExtFilteredFiles(
                                      self.__getFileNames(e.mimeData().urls())) if file]
        self.setDatas(filenames)
        super().dropEvent(e)

    def setItemAsBaseName(self, flag: bool):
        self._only_filename_flag = flag
        items = [self.item(i) for i in range(self.count())]
        if flag:
            for item in items:
                absname = item.text()
                basename = os.path.basename(absname)
                item.setText(basename)
        else:
            for item in items:
                basename = item.text()
                absname = self._basename_absname_dict[basename]
                item.setText(absname)
