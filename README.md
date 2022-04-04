# pyqt-top-left-right-file-list-widget
Simple PyQt widget which contains QListWidget and add, delete QPushButton to add and delete file in the list

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-top-left-right-file-list-widget.git --upgrade```

## Included packages
* <a href="https://github.com/yjg30737/simplePyQt5.git">simplePyQt5</a>
* <a href="https://github.com/yjg30737/pyqt-file-list-widget.git">pyqt-file-list-widget</a>
* <a href="https://github.com/yjg30737/pyqt-svg-icon-pushbutton.git">pyqt-svg-icon-pushbutton</a>

## Detailed Description
* Being able to add files to list, select multiple files on the list to delete, clear list.
* Being able to drop the files to the list
* Check the duplicated files' name
* User can able to choose the option to show files' name as absolute name or base name with "Show file name only" checkbox. 
* `setLabel(text: str)` - Set the label at the left side.
* `setExtensions(ext_lst: list)` - Define the specific extensions to add. 

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

![image](https://user-images.githubusercontent.com/55078043/161471903-e036a628-85b9-4bf7-bb55-d73b41596cb8.png)

Show file name only

![image](https://user-images.githubusercontent.com/55078043/161471920-4e8dace5-00ea-46e9-8652-731a1dc488bf.png)

You can select multiple files on the list. If at least one file is selected, delete button(red dash icon) will be clickable.

![image](https://user-images.githubusercontent.com/55078043/161471941-077dc58a-6490-4148-82eb-5ece2d31e13a.png)

Click it and selected ones will be removed from the list.

![image](https://user-images.githubusercontent.com/55078043/161472073-794cdaca-2d91-4647-bb3a-3a4c74db3902.png)

If some of files you want to add already exist in the list, Notice dialog will pop up to show you which files exist in the list. If you click OK, it will add files which are not duplicated. Otherwise none of files you want to add will be on the list.

![image](https://user-images.githubusercontent.com/55078043/145380501-1907ec13-31f8-483d-9fa7-5cb6d2ed440a.png)

## Note

I'm currently working with "Don't ask again" feature. Hope you don't mind. 

Well, One more thing. Duplicated files notice dialog's "show file name only" is not properly connected with main file list widget. I'm currently working with this too.

