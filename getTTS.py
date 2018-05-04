#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-04 17:47:46
# @Author  : ShadowHu (shadow_hu1441@163.com)
# @GitHub  : https://github.com/ShadowHu

import requests
import os

url = "http://fanyi.baidu.com/gettts?"
cwd = os.getcwd()
mp3dir = os.path.join(cwd, 'Mp3files')

if not os.path.exists(mp3dir):
    os.mkdir(mp3dir)

lannum = input("Which language? (1.English; 2.Japanese)\n")
text = input("Input your text: \n")

if lannum == '1':
    lan = 'en'
elif lannum == '2':
    lan = 'jp'

url = url + "lan=" + lan + "&text=" + text + "&spd=3&source=web"

req = requests.get(url)
with open(os.path.join(mp3dir, text + '.mp3'), 'wb') as file:
    file.write(req.content)
