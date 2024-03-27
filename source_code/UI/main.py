import sys
import os
from PyQt5.QtWidgets import QApplication
from mainwindow import MainWindow

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from sudu.gdb.other import print_test

if __name__ == "__main__":
    # print_test()
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())