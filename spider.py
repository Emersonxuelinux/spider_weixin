# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def spider(url):
    r = requests.get(url)
    page = r.text
    soup = BeautifulSoup(page, 'html.parser')
    value = soup.find_all(id='gz_gszzl')
    value = value[0].get_text()
    return value
