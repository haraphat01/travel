import re
import requests
from pprint import pprint



def visaAdvisory(citizenship: str, destination: str, lang: str):
    passport = destination.lower()
    to = citizenship.lower()

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


    pprint(dict)
    for key in dict:
        for v in dict[key]:
            if v == to:
                print(v, key)
                return key
