#!/home/l50/Library/anaconda3/bin/python3.6
import sys

from PyQt5.QtWidgets import QApplication
from football.gui import MainForm


def execute_from_command_line():
    app = QApplication(sys.argv)
    form = MainForm()
    sys.exit(app.exec_())