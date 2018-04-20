from football.utils import convert_link


class Tournament:
    __name = None
    __link = None

    def __init__(self, name=None, link=None):
        self.__name = name
        self.__link = link

    @property
    def name(self):
        return self.__name

    @property
    def link(self):
        """
        Link converted because of additional url
        :return:
        """
        return convert_link(self.__link)

    def __str__(self):
        return f'<Tournaments(name={self.name}, link={self.link})>'


class Team:
    __pos = __logo = __name = __om = __g = __b = __m = __a = __p = None

    def __init__(self, pos=None, logo=None, name=None, om=None, g=None, b=None, m=None, a=None, p=None):
        self.__pos = pos
        self.__logo = logo
        self.__name = name
        self.__om = om
        self.__g = g
        self.__b = b
        self.__m = m
        self.__a = a
        self.__p = p

    @property
    def pos(self):
        return self.__pos

    @property
    def logo(self):
        return self.__logo

    @property
    def name(self):
        return self.__name

    @property
    def om(self):
        return self.__om

    @property
    def g(self):
        return self.__g

    @property
    def b(self):
        return self.__b

    @property
    def m(self):
        return self.__m

    @property
    def a(self):
        return self.__a

    @property
    def p(self):
        return self.__p

    def __str__(self):
        return f'<Team(pos={self.pos}, name={self.name}, om={self.om}, g={self.g}, b={self.b}, m={self.m}, ' \
               f'a={self.a}, p={self.p})> '
