# הארי רציונלי אבל לא נורא

# install if not exist "bs4" need for html parser

from bs4 import BeautifulSoup
import re
import os
import bs4

def change_name_Potter(directory=None):
    if directory == None:
        directory = os.path.join(os.getcwd(), 'resource', 'potter')

    # iterate over files in
    # that directory
    for filename in os.scandir(directory):
        if filename.is_file():
            new_name = get_name_from_Potter(filename.path)

            os.rename(filename.path, os.path.join(directory, new_name))


# get name from  of harry potter chapter from title
def get_name_from_Potter(path):
    potter_chapter = open(path, 'r', encoding="utf8").read()

    soup = BeautifulSoup(potter_chapter, 'html.parser')

    # title of chapter
    title = soup.find('title').get_text()

    # mach the chapter number and chapter name
    result = re.search(r"([0-9]*): *(.*)", title)

    # Hack replace :->.  ":" cant be in file name
    return (result.group(1).zfill(3) + " " + result.group(2) + ".html").replace(":", ".")


change_name_Potter()