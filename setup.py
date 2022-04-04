from setuptools import setup, find_packages

setup(
    name='pyqt-top-left-right-file-list-widget',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_top_left_right_file_list_widget.style': ['button.css'],
                  'pyqt_top_left_right_file_list_widget.ico': ['add.svg', 'clear.svg', 'remove.svg']},
    description='Simple PyQt Widget which contains QListWidget and add, delete QPushButton '
                'to add and delete file in the list',
    url='https://github.com/yjg30737/pyqt-top-left-right-file-list-widget.git',
    install_requires=[
        'PyQt5>=5.8',
        'simplePyQt5 @ git+https://git@github.com/yjg30737/simplePyQt5.git@master',
        'pyqt-file-list-widget @ git+https://git@github.com/yjg30737/pyqt-file-list-widget.git@main',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main'
    ]
)