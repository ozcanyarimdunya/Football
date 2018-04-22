from bs4 import BeautifulSoup
import requests

from football.core.models import Tournament, Team


class TournamentScraper:
    """
    Scraper class
    """
    __html = str()
    __tournaments = list()

    def __init__(self):
        """
        init function
        """

    def open_from_file(self, path):
        """
        open file and get html
        """
        self.__html = open(path).read()

    def open_from_url(self, url):
        """
        open url and get html
        """
        self.__html = requests.get(url).text

    def __scrap(self):
        """
        scrap website and get tournament list
        """
        self.__tournaments = list()

        soup = BeautifulSoup(self.__html, 'lxml')
        popular = soup.find('div', attrs={'class': 'widget-competitions-popular'})
        for each in popular.find_all('a'):
            link = each['href']
            name = each.find('span').text
            t = Tournament(name=name, link=link)
            self.__tournaments.append(t)

    def get_popular_tournaments(self):
        """
        return list of popular tournaments
        """
        self.__scrap()

        return self.__tournaments


class LeagueScraper:
    """
    Scraper class
    """
    __html = str()
    __teams = list()

    def __init__(self):
        """
        init function
        """

    def open_from_file(self, path):
        """
        open file and get html
        """
        self.__html = open(path).read()

    def open_from_url(self, url):
        """
        open url and get html
        """
        self.__html = requests.get(url).text

    def __scrap(self):
        """
        scrap website and get team list
        """
        self.__teams = list()

        soup = BeautifulSoup(self.__html, 'lxml')
        popular = soup.find('div', attrs={'class': 'table__body'})
        for each in popular.find_all('div', attrs={'class': 'table__row'}):
            base = each.find_all('div', attrs={'class': 'table__cell'})
            pos = base[0].text
            logo = base[1].find('img')['src']
            name = base[2].find('a').text
            om = base[3].text
            g = base[4].text
            b = base[5].text
            m = base[6].text
            a = base[7].text
            p = base[8].text

            t = Team(pos=pos, logo=logo, name=name, om=om, g=g, b=b, m=m, a=a, p=p)
            self.__teams.append(t)

    def get_teams(self):
        """
        return list of popular tournaments
        """
        self.__scrap()

        return self.__teams
