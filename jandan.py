# Last modified: Yang Kai (kai.yang@bugua.com)
__author__ = 'yang'

import os

from lxml import html
import requests


if not os.path.exists('imgs'):
    os.makedirs('imgs')
next_page = requests.get('http://jandan.net/ooxx')
i = 1
while True:
    tree = html.fromstring(next_page.text)
    imgs = tree.xpath('//p//img[@*]')
    for img in imgs:
        url = img.attrib.values()[0] if len(img.attrib.values()) == 1 else img.attrib.values()[1]
    if not os.path.exists('imgs/' + url.split('/')[-1]):
        r = requests.get(url)
        with open('imgs/' + url.split('/')[-1], 'w') as f:
            f.write(r.content)
    next_page = requests.get(tree.xpath("//a[@class='previous-comment-page']")[0].attrib['href'])
    print('page %s downloaded' % i)
    i += 1