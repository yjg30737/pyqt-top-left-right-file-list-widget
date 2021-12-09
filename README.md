# pyqt-top-left-right-file-list-widget
Simple PyQt widget which contains QListWidget and add, delete QPushButton to add and delete file in the list

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-top-left-right-file-list-widget.git --upgrade```

## Included module
* <a href="https://github.com/yjg30737/simplePyQt5.git">simplePyQt5</a>

## Feature
* Being able to add files to list, select multiple files on the list to delete, clear list.
* Being able to drop the files to the list
* Being able to define the specific extensions to add with ```setExtList(ext_lst: list)```.
* Check the duplicated files' name
* Option to show files' name as absname/basename 

## Example
Code Example
```python
from PyQt5.QtWidgets import QApplication
from pyqt_top_left_right_file_list_widget.topLeftRightFileListWidget import TopLeftRightFileListWidget


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    topLeftRightFileListWidget = TopLeftRightFileListWidget()
    topLeftRightFileListWidget.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/145379025-1c7c075f-fbab-45c4-bcc3-d5ebc5ab00b5.png)

Show file name only

![image](https://user-images.githubusercontent.com/55078043/145379084-3e6dfc8e-4c8f-4c0c-848f-73816ae5a651.png)

You can select multiple files on the list. If at least one file is selected, delete button(red dash icon) will be clickable.

![image](https://user-images.githubusercontent.com/55078043/145379667-e3a7d67e-a7b5-4cb5-9d08-c002d2398fc7.png)

Click it and selected ones will be removed from the list.

![image](https://user-images.githubusercontent.com/55078043/145379940-11289218-2b1a-406b-98d8-f4a9ec31fc97.png)

If some of files you want to add already exist in the list, Notice dialog will pop up to show you which files exist in the list. If you click OK, it will add files which are not duplicated. Otherwise none of files you want to add will be on the list.

![image](https://user-images.githubusercontent.com/55078043/145380501-1907ec13-31f8-483d-9fa7-5cb6d2ed440a.png)

## Note

I'm currently working with "Don't ask again" feature. Hope you don't mind. 

Well, One more thing. Duplicated files notice dialog's "show file name only" is not properly connected with main file list widget. I'm currently working with this too.

