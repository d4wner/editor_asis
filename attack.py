#!/usr/bin/env python
#coding=utf-8
import re
import sys
import urllib2
import urllib
import os
sys.path.append("plugin/")
import color_pr
global site
def start():
	fold_list_tmp=[]
	fold_list_tmp=os.listdir(".")
	#print fold_list_tmp
	for dicname in fold_list_tmp:
		if not os.path.isfile(dicname) and dicname !=".git" and dicname != "plugin":
			print dicname
			#sys.path.append(dicname+"/")
			#print dicname+"/"
			pack = dicname+"/crack.py"
			os.system("python "+pack+" "+site)
			for filename in os.listdir(dicname):
				print color_pr.green(filename)
				#pack = dicname+"/crack.py"
				#print pack
				#os.popen('python '+pack)
				#site = "!!!!"
				#os.system("python "+pack+" "+site)




if __name__ == "__main__":
	print ("""       ===================================
       +-----------DemonSpider-----------+
       +--My dream,my morning sunshine.--+
       +--------Editor-Assasin-V1.0------+
       +--------demon@dawner.info--------+
       +--Exp:url-->http://www.baidu.com-+
       ===================================
                    =     =
                   ==     ==
                  ===<-|->===
                   =========
                    =======
                     =====
                      ===
                       +\nPlease input the url or input "x" to use the default dic:\n<-|->""")
	site = raw_input()
	start()

        


