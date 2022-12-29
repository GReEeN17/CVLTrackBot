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


    def setTeamHomepage(self, team_homepage):
        self.team_homepage = team_homepage
        self.setGames()
        self.setLeague()


    def setLeaguePage(self, league_page):
        self.league_page = league_page


    def setGames(self):
        response = requests.get(self.team_homepage)
        bs = BeautifulSoup(response.text, "lxml")
        opponents = bs.find_all("td")
        self.league_games = 0
        self.cup_games = 0
        i = self.index_start
        while "Расписание" not in opponents[i].text:
            self.league_games += 1
            i += self.gap_league_games
        i += 9
        while "История" not in opponents[i].text:
            self.cup_games += 1
            i += self.gap_cup_games


    def setLeague(self):
        response = requests.get(self.team_homepage)
        bs = BeautifulSoup(response.text, "lxml")
        info_league = bs.find_all('div')[90].text.strip().split(",")
        self.group = info_league[0][1:]
        self.league = info_league[1][:len(info_league[1]) - 1]



    def getLeagueTimetable(self):
        response = requests.get(self.team_homepage)
        bs = BeautifulSoup(response.text, "lxml")
        opponents = bs.find_all("td")
        full_info_opponents = []
        for i in range(self.index_start, self.index_start + self.league_games * self.gap_league_games, self.gap_league_games):
            info_ab_op = []
            for j in range(self.gap_league_games - 1):
                stripped_info = opponents[i + j].text.strip()
                if stripped_info == '':
                    break
                info_ab_op.append(stripped_info)
            full_info_opponents.append(info_ab_op)
        print(full_info_opponents)


    def getCupTimetable(self):
        response = requests.get(self.team_homepage)
        bs = BeautifulSoup(response.text, "lxml")
        opponents = bs.find_all("td")
        full_info_opponents = []
        start = self.index_start + self.league_games * self.gap_league_games + self.gap_cup_games + 1
        end = start + self.gap_cup_games * self.cup_games
        for i in range(start, end, self.gap_cup_games):
            info_ab_op = []
            for j in range(self.gap_cup_games - 1):
                stripped_info = opponents[i + j].text.strip()
                if stripped_info == '':
                    break
                info_ab_op.append(stripped_info)
            full_info_opponents.append(info_ab_op)
        print(full_info_opponents)


def testing():
    parser = CVlParser()
    parser.setTeamHomepage("https://v-open.spb.ru/component/volleychamp/?view=players&tid=200")
    #parser.getLeagueTimetable()
    parser.getCupTimetable()
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

#со 110 индекса a начинаются команды лиги
#со 133 индекса a начинаются команды кубка
#90 индекс div лига наша
#с 23 индекса td начинаются соперники - разрыв в 7 между играми
#с 109 индекса td начингаются соперники кубка разрыв - 8
#для переодического вызова функций - https://ru.stackoverflow.com/questions/951177/Как-написать-периодически-выполняемую-функцию-для-бота