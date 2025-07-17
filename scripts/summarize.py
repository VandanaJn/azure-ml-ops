import requests
from bs4 import BeautifulSoup
from transformers import pipeline
import click
# mute tensorflow complaints
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = "3"

def extract_from_file(path):
    with open(path,"r") as file:
        return file.read()

def summarize_text(text):
    generator = pipeline("summarization", model="t5-small", framework="pt")
    return generator(text, max_length=100, min_length=30)

@click.command  
@click.argument("inputpath", type=click.Path(exists=True, dir_okay=False, file_okay=True))  
@click.argument("outputpath",type=click.Path())
def summarize(inputpath, outputpath):
    '''
    INPUTPATH with raw text to summarize\n
    writes summary to OUTPUTPATH 
    '''
    text=extract_from_file(inputpath)
    result=summarize_text(text)
    result=result[0]["summary_text"]
    with open(outputpath,"+w") as file:
        file.write(result)


if __name__=="__main__":
    summarize()


