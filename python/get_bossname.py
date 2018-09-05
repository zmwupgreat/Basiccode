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
    #中央政治局
    #url='https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%85%B1%E4%BA%A7%E5%85%9A%E4%B8%AD%E5%A4%AE%E6%94%BF%E6%B2%BB%E5%B1%80%E5%A7%94%E5%91%98/10622019?fr=aladdin&fromid=12574682&fromtitle=%E4%B8%AD%E5%A4%AE%E6%94%BF%E6%B2%BB%E5%B1%80%E5%A7%94%E5%91%98'
    #100感动中国人物
    #url='https://baike.baidu.com/item/100%E4%BD%8D%E6%96%B0%E4%B8%AD%E5%9B%BD%E6%88%90%E7%AB%8B%E4%BB%A5%E6%9D%A5%E6%84%9F%E5%8A%A8%E4%B8%AD%E5%9B%BD%E4%BA%BA%E7%89%A9/6182590'
    #奥运会冠军
    #url='https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%A5%A5%E8%BF%90%E5%86%A0%E5%86%9B/863861?fr=aladdin'
    #中将
    #url='https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E4%BA%BA%E6%B0%91%E8%A7%A3%E6%94%BE%E5%86%9B%E4%B8%AD%E5%B0%86/13870885'
    #少将
    #url='https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E4%BA%BA%E6%B0%91%E8%A7%A3%E6%94%BE%E5%86%9B%E5%B0%91%E5%B0%86'
    #上将
    #url='https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E4%BA%BA%E6%B0%91%E8%A7%A3%E6%94%BE%E5%86%9B%E4%B8%8A%E5%B0%86'
    #主持人
    #url='https://baike.baidu.com/item/%E5%A4%AE%E8%A7%86%E5%8D%81%E4%BD%B3%E4%B8%BB%E6%8C%81%E4%BA%BA/7667355'
    #print('aaaaaa')
    #baidubaike_boss(url)
    #url = 'https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E9%99%A2%E9%99%A2%E5%A3%AB/327194?fr=aladdin'
    #url='https://baike.baidu.com/item/%E5%BC%80%E5%9B%BD%E5%B0%91%E5%B0%86'
    #baidubaike_boss(url)
    unique('name.txt')