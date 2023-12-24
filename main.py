import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
import random
import copy
import config
import threading
import schedule
import time


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

        self.start_button = QPushButton('Next Picture', self)
        self.start_learn_button = QPushButton('Switch to Learn mode', self)
        self.start_test_button = QPushButton('Switch to Test mode', self)

        self.label = QLabel(self)
        self.label.resize(300, 200)

        self.start_button.setGeometry(600, 400, 200, 200)

        self.start_button.show()

        self.start_button.clicked.connect(self.update_button_click)
        self.start_learn_button.clicked.connect(self.start_learn_thread)
        self.start_test_button.clicked.connect(self.start_test_thread)

        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.start_learn_button)
        self.layout.addWidget(self.start_test_button)

        self.picture_list = get_all_picture_names()

        self.picture_list_backup = copy.deepcopy(self.picture_list)

        self.test_task = schedule.every().second.do(self.update_button_click)

        self.test_time_interval = config.test_time_interval

        self.is_test_continuous = True

    def update_button_click(self):
        if len(self.picture_list) == 0:
            self.picture_list = copy.deepcopy(self.picture_list_backup)

        random_number = random.randint(0, len(self.picture_list) - 1)

        path = self.picture_list[random_number]

        del self.picture_list[random_number]

        pix = QPixmap(path)

        self.label.setPixmap(pix)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

    def start_learn_thread(self):
        self.start_button.setEnabled(True)
        self.is_test_continuous = False

    def start_test_thread(self):
        self.test_task = schedule.every().second.do(self.update_button_click)
        self.start_button.setEnabled(False)
        self.is_test_continuous = True
        thread = threading.Thread(target=self.show_pictures_continuously)
        thread.start()

    def show_pictures_continuously(self):
        while self.is_test_continuous:
            schedule.run_pending()
            time.sleep(self.test_time_interval)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWidget = CubeCFOPTestGame()
    mainWidget.show()
    sys.exit(app.exec_())
