# -*- coding:utf-8 -*-
import urllib.request as request
import re
from bs4 import BeautifulSoup


def baidubaike_boss(url):
    response = request.urlopen(url)
    html = response.read()
    print('hhhhh')
    data = html.decode('UTF-8')
    soup = BeautifulSoup(data,"html.parser")
#    print(soup.prettify())
    file = open('kaiguoshaojiang.txt','w')
    for list in soup.find_all('a',href=re.compile(r'/item/[0-9a-zA-Z%]+')):
        print(list.string)
        file.write(list.string + "\n")
    file.close()

def spider_table(url):
    response = request.urlopen(url)
    html = response.read()
    print('reading...')
    data = html.decode('UTF-8')
    #soup = BeautifulSoup(data,"html.parser")
    #for list in soup.find('div',class_='para').find(''):
    #   print(list.string)
    reg = re.compile(r'<td width="72" height="16" align="left" valign="bottom"><div class="para" label-module="para">.*?<//a><//div>',re.S)
    items = re.findall(reg,data)
    for i in items:
        pattern = re.compile()

def unique(filename):
    file = open(filename)
    u = []
    n = []
    for line in file:
        u.append(line)
    for i in range (len(u)):
        f = 0
        for j in range (len(n)):
            if(u[i] == n[j]):
                f=1
                break
        if(f == 0 ):
            n.append(u[i])
    file = open('name1.txt', 'w')
    for m in n:
        print(m)
        file.write(m)
    file.close()





if __name__ == '__main__' :
    #baidubaike_boss(url)
    unique('name.txt')