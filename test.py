import requests
from bs4 import BeautifulSoup


def getToLink(link):
    result = requests.get(link)
    if result.status_code != 200:
        print("Bad request, try later")
        return None
    return result

def parser(result):
    soup = BeautifulSoup(result.content, 'html.parser')
    parsedData = soup.find_all("a",attrs={"class":"hll"})
    print("Getting all the titles...")
    return parsedData

def saveFile(data):
    print("Saving to data.txt ...")
    with open("data.txt","w",encoding='utf-8') as f:
        for line in data:
            f.write((line.text)+'\n')
    print("Data saved.")

if __name__ == "__main__":
    link = "https://www.newsnow.co.uk/h/"
    result = getToLink(link)
    parsedData = parser(result)
    saveFile(parsedData)