from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2

register_openers()


datagen, headers = multipart_encode({"userfile": open("1.jpg", "rb")})


request = urllib2.Request("http://localhost/testphp.php", datagen, headers)

print urllib2.urlopen(request).read()


