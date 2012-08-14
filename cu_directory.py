import urllib
import sys

from bs4 import BeautifulSoup

def parse_uni(uni):
    url = "https://directory.columbia.edu/people/uni?code=" + uni
    html =urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    mydict = {}
    try:
        for i, child in enumerate(soup.find_all('table')[3].tbody.children):
            temp = []
            for j, grandkid in enumerate(child):
                temp.extend(grandkid)
                if i == 0:
                    mydict[u'Name'] = temp[0]
                    temp = []
                elif j % 2:
                    if temp[0] == u'Email:':
                        temp[1] = temp[1].contents[0]
                    mydict[temp[0].rstrip(':')] = temp[1]
                    temp = []
                else:
                    continue
        return mydict
    except IndexError:
        print 'UNI does not exist'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: python cu_directory.py <CU UNI>'
    else:
        print parse_uni(sys.argv[1])