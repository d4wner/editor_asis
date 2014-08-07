#!/usr/bin/env python
#coding=utf-8
import re
import sys
import urllib2
import urllib
import os
import threading
sys.path.append("plugin/")
#import color_pr
global editor_types
types=["fckeditor","ewebeditor","kindeditor"]


class timer(threading.Thread): #The timer class is derived from the class threading.Thread  
    def __init__(self, cmd):  
        threading.Thread.__init__(self)  
        self.cmd = cmd  
    def run(self): #Overwrite run() method, put what you want the thread do here  
        try:
	    os.system(self.cmd)
        except Exception,e:
	    print e
	    #break

def scan_run(dicname):
    pack = dicname+"/crack.py"
    for site in open('dic/url.txt','r'):
        cmd="python "+pack+" "+site
            #print cmd
    try:
        tscan=timer(cmd)
        tscan.start()
    except Exception,e:
        print e

def choose_scan_start(editor_types):
#types=[]
    if "," in editor_types and editor_types != "":
        for item in editor_types.strip().split(","):
            if item in types:
                scan_run(item)
    elif editor_types != "":
        if item in types:
            scan_run(editor_types)
    else:
        multi_scan_start()


def multi_scan_start():
    fold_list_tmp=[]
    fold_list_tmp=os.listdir(".")
    #print fold_list_tmp
    for dicname in fold_list_tmp:
        if not os.path.isfile(dicname) and dicname !=".git" and dicname != "plugin" and dicname != "dic":
            scan_run(dicname)


if __name__ == "__main__":
    print ("""       ===================================
       +-----------DemonSpider-----------+
       +--------Editor-Assasin-V2.0------+
       +--------demon@dawner.info--------+
       +url.txt:http://www.baidu.com/fck/+
       ===================================
                    =     =
                   ==     ==
                  ===<-|->===
                   =========
                    =======
                     =====
                      ===
                       +\nPlease check the default dics and you can input the editor type to start:\n<-|->""")
    editor_types = raw_input()
    choose_scan_start(editor_types)

        


