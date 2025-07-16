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

def extract_from_file(path):
    with open(path,"r") as file:
        return file.read()


def summarize_text(text):
    generator = pipeline("summarization", model="t5-small", framework="pt")
    return generator(text, max_length=100, min_length=30)

@click.command()
@click.option("--url", help="url to summarize")
@click.option("--path", help="file path to summarize")
def summarize(url, path):
    text=""
    if url:
        text = extract_from_url(url)
    elif path:
        text=extract_from_file(path)
    else:
        return
    result=summarize_text(text)
    click.echo("*"*20)
    click.echo(result[0]["summary_text"])

if __name__=="__main__":
    summarize()

