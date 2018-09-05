import json
import codecs
from urllib.parse import quote
import urllib
import requests
import re
import os
import itertools

ImagePath = "" #文件保存路径
oneperson = 600
str_table = {
    '_z2C$q': ':',
    '_z&e3B': '.',
    'AzdH3F': '/'
}

char_table = {
    'w': 'a',
    'k': 'b',
    'v': 'c',
    '1': 'd',
    'j': 'e',
    'u': 'f',
    '2': 'g',
    'i': 'h',
    't': 'i',
    '3': 'j',
    'h': 'k',
    's': 'l',
    '4': 'm',
    'g': 'n',
    '5': 'o',
    'r': 'p',
    'q': 'q',
    '6': 'r',
    'f': 's',
    'p': 't',
    '7': 'u',
    'e': 'v',
    'o': 'w',
    '8': '1',
    'd': '2',
    'n': '3',
    '9': '4',
    'c': '5',
    'm': '6',
    '0': '7',
    'b': '8',
    'l': '9',
    'a': '0'
}

# str 的translate方法需要用单个字符的十进制unicode编码作为key
# value 中的数字会被当成十进制unicode编码转换成字符
# 也可以直接用字符串作为value
char_table = {ord(key): ord(value) for key, value in char_table.items()}

# 解码图片URL
def decode(url):
# 先替换字符串
    for key, value in str_table.items():
        url = url.replace(key, value)

#再替换剩下的字符
    return url.translate(char_table)

#下载图片
def downImg(imgUrl, dirpath, imgName):
    filename = os.path.join(dirpath, imgName)
    try:
        res = requests.get(imgUrl, timeout=15)
        if str(res.status_code)[0] == "4":
            print(str(res.status_code), ":" , imgUrl)
            return False
    except Exception as e:
        print("抛出异常：", imgUrl)
        print(e)
        return False
    with open(filename, "wb") as f:
        f.write(res.content)
    return True

#解析json获取图片
def downloadpic(key,word):
    name=word
#关键词转换
    word = quote(key+word)
#建立图片目录
    dirname = ImagePath + "/" + name.replace("\n", "")
    is_direxist = os.path.exists(dirname)
    if not is_direxist:
        print("新建一个目录%s" %name)
        os.mkdir(dirname)

# 生成多页url
    url = r"http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&st=-1&ic=0&word={word}&face=0&istype=2nc=1&pn={pn}&rn=60"
    urls = []  # (url.format(word=word, pn=x) for x in itertools.count(start=0, step=60))
    i=0
    index = 0
    while True:
        url = r"http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&st=-1&ic=0&word={word}&face=0&istype=2nc=1&pn={pn}&rn=60"
        url1=url.format(word=word, pn=i * 60)
        i+=1
        try:
            print('正在请求URL：',url1)
            #get HTML
            response = requests.get(url1, timeout=10)
        except Exception as e:
            print(e)
            continue
        if response:
            try:
                html = response.content.decode('UTF-8')
            except Exception as e:
                print(e)
                continue
        try:
            imgurls = [decode(x) for x in re.compile(r'"objURL":"(.*?)"').findall(html)]
            if len(imgurls) == 0:
                print('没有图片%s' % name)
                return
        except Exception as e:
            print(e)
            continue
        try:
            for url in imgurls:
                if downImg(url,dirname,str(index)+".jpg"):
                    index += 1
                    print("%s已下载%s张照片"%(name, str(index)))
                if index >oneperson:
                    return
            if index >oneperson:
                return

        except Exception as e:
            print(e)
            print(name)
        if index > oneperson:
            return

if __name__ == '__main__':
    file = open('hhh.txt')
    for line in file:
        print("正在爬取%s的照片" % line)
        line.replace("\n","")
        downloadpic("",line)