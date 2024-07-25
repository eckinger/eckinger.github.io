import requests
from termcolor import colored
from bs4 import BeautifulSoup

def download_pdfs():
    URL = "https://www.bp.com/en/global/corporate/investors/results-reporting-and-presentations/archive.html"
    page = requests.get(URL,headers={"User-Agent":"Mozilla/5.0"})
    soup = BeautifulSoup(page.text, "html.parser")
    
    for link in soup.select("a[href$='.pdf']"):
        if ('.pdf' in link.get('href',[])):
            filename = link.get('href')[link.get('href').rfind('/'):]
            filename = filename[1:]
            print(colored("Downloading: " + filename, 'green'))
            try:
                response = requests.get('https://www.bp.com' +
                                        link.get('href'))
            except requests.exceptions.ConnectionError as e0:
                continue
            except requests.exceptions.MissingSchema as e1:
                print(colored('E> URL is not complete.', 'red'))
                continue
            with open("BP/pdfs/" + filename, 'wb') as f:
                f.write(response.content)

download_pdfs()