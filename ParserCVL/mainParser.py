from bs4 import BeautifulSoup
import requests


class CVlParser:
    def __init__(self):
        self.index_start = 23
        self.gap_league_games = 7
        self.gap_cup_games = 8
        self.team_homepage = None
        self.league_page = None
        self.league_games = 0
        self.cup_games = 0
        self.group = None
        self.league = None
        self.ind_cup_games = 0
        self.ind_league_games = 0
        self.url_leagues = ['https://v-open.spb.ru/hard-liga-v.html', 'https://v-open.spb.ru/rezult-hard-liga.html',
                            'https://v-open.spb.ru/rezul-tsuper-liga.html',
                            'https://v-open.spb.ru/result-medium-liga-sever.html']

    def set_team_homepage(self, team_homepage):
        self.team_homepage = team_homepage
        self.set_indexes_tables()
        self.set_games()

    def set_league_page(self, league_page):
        self.league_page = league_page

    def set_indexes_tables(self):
        response = requests.get(self.team_homepage)
        bs = BeautifulSoup(response.text, "lxml")
        opponents = bs.find_all("td")
        ind_cup_games = 0
        ind_league_games = 0
        for i, inf in enumerate(opponents):
            if "Расписание" in inf.text and "Сезон" in inf.text:
                if "Кубок" in inf.text:
                    ind_cup_games = i
                if "Кубок" not in inf.text:
                    ind_league_games = i
        self.ind_cup_games = ind_cup_games
        self.ind_league_games = ind_league_games

    def set_games(self):
        response = requests.get(self.team_homepage)
        bs = BeautifulSoup(response.text, "lxml")
        opponents = bs.find_all("td")
        gap_btw_games = self.gap_league_games if self.ind_league_games < self.ind_cup_games else self.gap_cup_games
        frc = self.ind_cup_games if self.ind_cup_games < self.ind_league_games else self.ind_league_games
        frc += gap_btw_games + 1
        while "История" not in opponents[frc].text:
            if "Расписание" in opponents[frc].text:
                gap_btw_games = self.gap_league_games if gap_btw_games == self.gap_cup_games else self.gap_cup_games
                frc += gap_btw_games + 1
            self.league_games += 1 if gap_btw_games == self.gap_league_games else 0
            self.cup_games += 1 if gap_btw_games == self.gap_cup_games else 0
            frc += gap_btw_games

    def set_league(self):
        response = requests.get(self.team_homepage)
        bs = BeautifulSoup(response.text, "lxml")
        info_league = bs.find_all('div')[90].text.strip().split(",")
        self.group = info_league[0][1:]
        self.league = info_league[1][:len(info_league[1]) - 1]

    def get_league_timetable(self):
        response = requests.get(self.team_homepage)
        bs = BeautifulSoup(response.text, "lxml")
        opponents = bs.find_all("td")
        full_info_opponents = []
        start = self.ind_league_games + self.gap_league_games + 1
        for i in range(start, start + self.league_games * self.gap_league_games, self.gap_league_games):
            info_ab_op = []
            for j in range(self.gap_league_games - 1):
                stripped_info = opponents[i + j].text.strip()
                if stripped_info == '':
                    break
                info_ab_op.append(stripped_info)
            full_info_opponents.append(info_ab_op)
        return full_info_opponents

    def get_cup_timetable(self):
        response = requests.get(self.team_homepage)
        bs = BeautifulSoup(response.text, "lxml")
        opponents = bs.find_all("td")
        full_info_opponents = []
        start = self.ind_cup_games + self.gap_cup_games + 1
        end = start + self.gap_cup_games * self.cup_games
        for i in range(start, end, self.gap_cup_games):
            info_ab_op = []
            for j in range(self.gap_cup_games - 1):
                stripped_info = opponents[i + j].text.strip()
                if stripped_info == '':
                    break
                info_ab_op.append(stripped_info)
            full_info_opponents.append(info_ab_op)
        return full_info_opponents

    def get_current_position(self):
        for league in self.url_leagues:
            response = requests.get(league)
            bs = BeautifulSoup(response.text, "lxml")
            find_sky_steps = bs.find_all("tbody")
            for i in find_sky_steps:
                stripped_text = i.text.split()
                if stripped_text[1] == 'SkyStepS':
                    return [stripped_text[0], stripped_text[1], stripped_text[-5], stripped_text[-3], stripped_text[-4]]


parser = CVlParser()
parser.set_team_homepage("https://v-open.spb.ru/component/volleychamp/?view=players&tid=200")



def testing():
    '''parser = CVlParser()
    parser.set_team_homepage("https://v-open.spb.ru/component/volleychamp/?view=players&tid=200")
    parser.get_league_timetable()
    parser.get_cup_timetable()'''

    '''url = "https://v-open.spb.ru/component/volleychamp/?view=players&tid=200"
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    info_league = bs.find_all('div')[90].text.strip().split(",")
    group = info_league[0][1:]
    league = info_league[1][:len(info_league[1]) - 1]
    print(group, league)
    results = bs.find_all("td")
    for i in range(23, 100, 7):
        print(results[i].text)
    print(results[108].text)'''

# со 110 индекса a начинаются команды лиги со 133 индекса a начинаются команды кубка 90 индекс div лига наша с 23
# индекса td начинаются соперники - разрыв в 7 между играми с 109 индекса td начингаются соперники кубка разрыв - 8
# для переодического вызова функций -
# https://ru.stackoverflow.com/questions/951177/Как-написать-периодически-выполняемую-функцию-для-бота
