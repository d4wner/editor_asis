from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2
import re


register_openers()


datagen, headers = multipart_encode({"NewFile": open("1.jpg", "rb")})


request = urllib2.Request("http://localhost/editor/filemanager/browser/default/browser.html?Type=all&Connector=connectors/php/connector.php", datagen, headers)

resp= urllib2.urlopen(request).read()
print resp
#xx= re.findall(r'\(.*jpg',resp)
##print xx[0]
#print xx[0][1:].split(',"')[0]
#print xx[0][1:].split(',"')[1]

