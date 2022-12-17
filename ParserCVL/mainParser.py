from bs4 import BeautifulSoup
import requests

def testing():
    url = "https://v-open.spb.ru/result-medium-liga-sever.html"
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    attrs = {"title": "SkyStepS"}
    temp = bs.find("a", attrs)
    print(temp.text)