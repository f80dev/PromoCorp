import Corporate as corps
from html.parser import HTMLParser

class WebParser(HTMLParser):
    def __init__(self,desc_tags:dict,e):
        for p in e:
            print(p)