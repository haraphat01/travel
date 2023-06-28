import re
import requests
from pprint import pprint
from bs4 import BeautifulSoup

dictionaryFrom = {
    "соединённые штаты америки": "сша",
    "чехия": "чешская-республика",
    "объединенные арабские эмираты": "оаэ",
    "россия": "рф",
    "российская федерация": "рф",
    "юар": "южная-африка",
    "белоруссия": "беларусь",
    "конго": "дем-респ-конго",
    "шриланка": "шри-ланка",
    "палестина": "гос-палестина",

}
dictionaryTo = {
    "сша": "соединённые штаты америки",
    "чешская-республика": "чехия",
    "оаэ": "объединенные арабские эмираты",
    "рф": "российская федерация",
    "россия": "российская федерация",
    "южная-африка": "юар",
    "беларусь": "белоруссия",
    "дем-респ-конго": "конго",
    "шри-ланка": "шриланка",
    "гос-палестина": "палестина"
}


def visaAdvisory(destination: str, citizenship: str, lang: str):
    passport = citizenship.lower()
    to = destination.lower()
    if passport == to:
        return "You are already here"
    if dictionaryTo.get(destination):
        to = dictionaryTo.get(destination)
    if dictionaryFrom.get(citizenship):
        passport = dictionaryFrom.get(citizenship)



    passport_link_eng = f"https://visaindex.com/country/{passport}-passport-ranking/"
    passport_link_ru = f"https://visaindex.com/ru/страна/{passport}-рейтинг-паспорта/"

    url = {
        'ru': passport_link_ru,
        'eng': passport_link_eng
    }

    dict = {}

    response = requests.get(url[f'{lang}'])
    soup = BeautifulSoup(response.text, 'lxml')

    data = soup.find_all("div", class_="col-title text-secondary font-weight-bold display-8")
    data2 = soup.find_all("div", class_="list-group borderLight bg-white")

    for i in range(len(data)):
        element = re.sub('[\t\r\n]', '', data[i].text)
        countries = data2[i].find_all("span", class_="country-name")
        for e in countries:
            country_element = re.sub('[\t\r\n]', '', e.text).lower()
            dict.setdefault(element, [])
            dict[element].append(country_element)

    for key in dict:
        for v in dict[key]:
            if v == to or dictionaryFrom.get(to) == v or dictionaryTo.get(to) == v or dictionaryTo.get(v)== to or dictionaryFrom.get(v) == to:
                return key
