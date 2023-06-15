import re
import requests
from bs4 import BeautifulSoup
from pprint import pprint


def visaAdvisory(citizenship: str, destination: str ):
    passport = citizenship.lower()
    to = destination.lower()

    passport_link = f"https://visaindex.com/country/{passport}-passport-ranking/"

    dict = {}

    response = requests.get(passport_link)
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
            if v == to:
                return key
