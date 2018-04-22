import sys

from PyQt5.QtWidgets import QApplication

from football.gui import MainForm

app = QApplication(sys.argv)
form = MainForm()
sys.exit(app.exec_())