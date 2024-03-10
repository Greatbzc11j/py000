import requests
from bs4 import BeautifulSoup


def get_per(code):
    url = "https://finance.naver.com/item/main.naver?code="+ code
    html = requests.get(url).text

    soup = BeautifulSoup(html,"html5lib")
    tags = soup.select("#_cns_per")
    tag = tags[0]
    return float(tag.text)

def get_dividend(code):
    url = "https://finance.naver.com/item/main.naver?code=" + code
    html = requests.get(url).text
    soup = BeautifulSoup(html,"html5lib")
    tags = soup.select("#_dvr")
    tag=tags[0]
    return float(tag.text)

print(get_per("000660"))
#print(get_dividend("000660"))
