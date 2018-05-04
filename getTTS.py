#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-04 17:47:46
# @Author  : ShadowHu (shadow_hu1441@163.com)
# @GitHub  : https://github.com/ShadowHu

import requests
import os


def reqmp3(url, lan, text, mp3dir, dirname):
    url = url + "lan=" + lan + "&text=" + text + "&spd=3&source=web"
    req = requests.get(url)
    if not os.path.exists(os.path.join(mp3dir, dirname)):
        os.mkdir(os.path.join(mp3dir, dirname))
    with open(os.path.join(mp3dir, dirname, text + '.mp3'), 'wb') as file:
        file.write(req.content)


url = "http://fanyi.baidu.com/gettts?"
cwd = os.getcwd()
mp3dir = os.path.join(cwd, 'Mp3files')

if not os.path.exists(mp3dir):
    os.mkdir(mp3dir)

lannum = input("Which language? (1.English; 2.Japanese)\n")
text = input("Input your text:(If you have a text file just click 'Enter') \n")


if lannum == '1':
    lan = 'en'
elif lannum == '2':
    lan = 'jp'

if text:
    reqmp3(url, lan, text, mp3dir, 'SingleText')
else:
    textfile = input("Or drag your text file below.\n")
    with open(textfile) as tfile:
        for text in tfile:
            reqmp3(url, lan, text.rstrip(), mp3dir, os.path.split(textfile)[-1][:-4])

