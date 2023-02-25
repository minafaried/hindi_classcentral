import bs4
from englisttohindi.englisttohindi import EngtoHindi
import os


def translate(data):

    if not data:
        return
    for tag in data:

        if tag.name=="script" or tag.name=="style":
            continue
        if str(tag)=='\n'or str(tag)==' ' or not str(tag) or str(tag)=='html':
            continue
        if not isinstance(tag, bs4.element.Tag):
            hindi=EngtoHindi(str(tag)).convert
            if hindi:
                tag.string.replace_with(hindi)
            continue

        translate(tag)


def translateHTMLFile(file):
    with open(file, "r", encoding='utf-8') as f:
        data = f.read()
        f.close()
    soup = bs4.BeautifulSoup(data, 'html.parser')
    for element in soup(text=lambda text: isinstance(text, bs4.Comment)):
        element.extract()
    translate(soup)
    print("translated successfully")
    with open(file, "w+", encoding='utf-8') as f:
        f.write(str(soup))
        f.close()

directory = 'hindi'

# iterate over files in
# that directory
def getFiles(directory):
    print( "*********************directory:"+directory)
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        filename, file_extension = os.path.splitext(f)
        if os.path.isfile(f):
            if file_extension=='.html':
                print("translate :"+f)
                translateHTMLFile(f)
        else:
            getFiles(f)

getFiles(directory)