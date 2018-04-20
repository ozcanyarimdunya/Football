import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

from football.core import TournamentScraper, LeagueScraper
from gui.forms import MainWindow


class Form(QMainWindow, MainWindow):
    tournaments_list = []

    def __init__(self):
        super(__class__, self).__init__()
        self.setup_ui(self)
        self.resize(650, 650)
        self.move(300, 0)
        self.setWindowTitle("Football")
        self.show()

        self.start()

    def start(self):
        self.tournaments_to_list()
        self.listWidget.itemClicked.connect(lambda item: self.tournaments_list_item_clicked(item))

    def tournaments_to_list(self):
        self.label_loading.setText("Loading Tournaments ..")
        url = 'http://www.goal.com/tr/ligler'
        ts = TournamentScraper()
        ts.open_from_url(url=url)
        self.tournaments_list = ts.get_popular_tournaments()

        for tournament in self.tournaments_list:
            self.listWidget.addItem(tournament.name)

        self.label_loading.setText("Click any tournaments to see detail")

    def tournaments_list_item_clicked(self, item):
        for tournament in self.tournaments_list:
            if tournament.name == item.text():
                """Fill Table Widget | it could throw exception"""
                self.setWindowTitle(tournament.name)
                self.leagues_to_table_widget(link=tournament.link)
                break

    def leagues_to_table_widget(self, link):
        try:
            self.main_layout.setCurrentIndex(0)
            self.label_loading.setText("Loading League ..")

            ls = LeagueScraper()
            ls.open_from_url(url=link)
            team_list = ls.get_teams()

            # Prepare table
            self.main_table.clear()

            # Poz.  Takım OM G B M +/- P
            self.main_table.setColumnCount(8)
            self.main_table.setRowCount(team_list.__len__())
            for order, team in enumerate(team_list):
                self.main_table.setItem(order, 0, QTableWidgetItem(team.pos))
                self.main_table.setItem(order, 1, QTableWidgetItem(team.name))
                self.main_table.setItem(order, 2, QTableWidgetItem(team.om))
                self.main_table.setItem(order, 3, QTableWidgetItem(team.g))
                self.main_table.setItem(order, 4, QTableWidgetItem(team.b))
                self.main_table.setItem(order, 5, QTableWidgetItem(team.m))
                self.main_table.setItem(order, 6, QTableWidgetItem(team.a))
                self.main_table.setItem(order, 7, QTableWidgetItem(team.p))

            self.main_table.setHorizontalHeaderLabels(['Poz.', 'Takım', 'OM', 'G', 'B', 'M', '+/-', 'P'])
            self.main_table.resizeColumnsToContents()
            self.main_table.verticalHeader().hide()
            self.main_layout.setCurrentIndex(1)
        except Exception as e:
            self.label_loading.setText("An error occur!\n" + str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    sys.exit(app.exec_())
