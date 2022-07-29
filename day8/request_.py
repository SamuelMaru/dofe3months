import requests
import re
import bs4
import time
homepage = requests.get("https://firetechcamp.com/")

def findele(url, elename):
    title_info = requests.get(url).text
    return (title_info.split("<" + elename + ">"))[1].split("</" + elename + ">")[0]


def findele_reg(url, elename):
    title_info = requests.get(url).text
    data = re.search(("<" + elename + ">(.*)</" + elename + ">"), title_info)
    return data[1]


def findele_html(url, elename):
    title_info = requests.get(url).text
    html = bs4.BeautifulSoup(requests, features="html.parser")
    return html.title

