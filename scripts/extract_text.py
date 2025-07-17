import requests
from bs4 import BeautifulSoup
from transformers import pipeline
import click
# mute tensorflow complaints
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "3"

def extract_from_url(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    text=""
    for p in soup.find_all("p"):
        text+=p.get_text()
    return text


@click.command()
@click.argument("url")
@click.argument("outputpath")
def extract_text(url,  outputpath):
    '''
    URL to get text from
    writes text to OUTPUTPATH 
    '''
    text=extract_from_url(url)
    with open(outputpath,"+w") as file:
        file.write(text)

if __name__=="__main__":
    extract_text()


