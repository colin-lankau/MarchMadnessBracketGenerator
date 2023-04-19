'''
Utility module for scraping web data
'''
import requests
from bs4 import BeautifulSoup

def get_html(target):
    API_KEY = '7e1efe7a-27c0-4ddf-b835-df8728425dcb'
    response = requests.get(
        url='https://proxy.scrapeops.io/v1/',
        params={
            'api_key': API_KEY,
            'url': target, 
        },
    )
    return response

def write_data(response):
    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.findAll('table')
    with open('data.txt', 'w') as file:
        for row in rows:
            file.write(row.text)