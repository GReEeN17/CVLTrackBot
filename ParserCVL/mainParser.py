from bs4 import BeautifulSoup
import requests

def testing():
    url = "https://v-open.spb.ru/component/volleychamp/?view=players&tid=200"
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    opponents = bs.find_all("a")
    for i in range(110, 131, 2):
        print(opponents[i].text)
    for i in range(133, 136, 2):
        print(opponents[i].text)
    infoAboutLeague = bs.find("div", "contentheading")
    print(infoAboutLeague.text)
    league = bs.find_all('div')
    print(league[90].text)
    results = bs.find_all("td")
    print(results[23].text)

#со 110 индекса a начинаются команды лиги
#со 133 индекса a начинаются команды кубка
#90 индекс div лига наша
#с 23 индекса td начинаются соперники - разрыв в 7 между играми