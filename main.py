import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
import random
import copy
import config


def get_all_picture_names():
    picture_list = list()

    folder_path = os.path.abspath(config.pictures_path)

    files_in_folder = os.listdir(folder_path)

    for file_name in files_in_folder:
        file_name = os.path.join(folder_path, file_name)
        picture_list.append(file_name)

    return picture_list


class CubeCFOPTestGame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(600, 400, 600, 400)
        self.setWindowTitle("Cube CFOP Test")
        self.layout = QVBoxLayout(self)

        self.start_button = QPushButton('Update', self)

        self.label = QLabel(self)
        self.label.resize(300, 200)

        self.start_button.setGeometry(600, 400, 200, 200)

        self.start_button.show()

        self.start_button.clicked.connect(self.button_click)

        self.layout.addWidget(self.start_button)

        self.picture_list = get_all_picture_names()

        self.picture_list_backup = copy.deepcopy(self.picture_list)

    def button_click(self):
        if len(self.picture_list) == 0:
            self.picture_list = copy.deepcopy(self.picture_list_backup)

        random_number = random.randint(0, len(self.picture_list) - 1)

        path = self.picture_list[random_number]

        del self.picture_list[random_number]

        pix = QPixmap(path)

        self.label.setPixmap(pix)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWidget = CubeCFOPTestGame()
    mainWidget.show()
    sys.exit(app.exec_())
