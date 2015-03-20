import urllib.request
import re


def gethref(url):
    html_content = urllib.request.urlopen(url).read()
    r = re.compile('href="(.*?)"')
    result = r.findall(html_content.decode('GBK'))
    return result

def find_links(website):
    html_content = urllib.request.urlopen(website).read()
    r = re.compile('href="(.*?)"')
    result = r.findall(html_content.decode('GBK'))
    return result

if __name__ == '__main__':
    print(find_links('http://www.sina.com/'))
    print(gethref('http://www.taobao.com'))