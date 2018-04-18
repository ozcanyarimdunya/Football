from bs4 import BeautifulSoup
from football.core.models import Tournament, Team
import requests


class TournamentScraper:
    """
    Scraper class
    """
    __url = str()
    __html = str()
    __tournaments = list()

    def __init__(self, url=None):
        """
        init function
        """
        self.__url = url

    def open_from_file(self):
        """
        open file and get html
        """
        self.__html = open(self.__url).read()

    def open_from_url(self):
        """
        open url and get html
        """
        self.__html = requests.get(self.__url).text

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
    __url = str()
    __html = str()
    __teams = list()

    def __init__(self, url=None):
        """
        init function
        """
        self.__url = url

    def open_from_file(self):
        """
        open file and get html
        """
        self.__html = open(self.__url).read()

    def open_from_url(self):
        """
        open url and get html
        """
        self.__html = requests.get(self.__url).text

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
