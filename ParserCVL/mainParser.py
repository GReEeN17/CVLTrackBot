from bs4 import BeautifulSoup
import requests

class CVlParser:
    def __init__(self):
        self.team_homepage = None
        self.league_page = None


    def setTeamHomepage(self, team_homepage):
        self.team_homepage = team_homepage


    def setLeaguePage(self, league_page):
        self.league_page = league_page


    def getLeagueTimetable(self):
        response = requests.get(self.team_homepage)
        bs = BeautifulSoup(response.text, "lxml")
        info_league = bs.find_all('div')[90].text.strip().split(",")
        group = info_league[0][1:]
        league = info_league[1][:len(info_league[1]) - 1]

def testing():
    url = "https://v-open.spb.ru/component/volleychamp/?view=players&tid=200"
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    info_league = bs.find_all('div')[90].text.strip().split(",")
    group = info_league[0][1:]
    league = info_league[1][:len(info_league[1]) - 1]
    print(group, league)
    results = bs.find_all("td")
    for i in range(23, 102, 7):
        print(results[i].text)
    print(results[109].text)

#со 110 индекса a начинаются команды лиги
#со 133 индекса a начинаются команды кубка
#90 индекс div лига наша
#с 23 индекса td начинаются соперники - разрыв в 7 между играми
#с 109 индекса td начингаются соперники кубка разрыв - 8
#для переодического вызова функций - https://ru.stackoverflow.com/questions/951177/Как-написать-периодически-выполняемую-функцию-для-бота