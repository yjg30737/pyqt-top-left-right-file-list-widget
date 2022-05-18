import codecs
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='pyqt-top-left-right-file-list-widget',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_top_left_right_file_list_widget.ico': ['add.svg', 'clear.svg', 'delete.svg']},
    description='Simple PyQt Widget which contains QListWidget and add, delete QPushButton '
                'to add and delete file in the list',
    url='https://github.com/yjg30737/pyqt-top-left-right-file-list-widget.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'PyQt5>=5.8',
        'simplePyQt5>=0.0.1',
        'pyqt-file-list-widget>=0.0.1',
        'pyqt-svg-button>=0.0.1'
    ]
)