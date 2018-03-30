import urllib2


connection = urllib2.urlopen("http://www.wdylike.appspot.com?q=shit")
code = connection.getcode()
print(code)
info = connection.info()
print(info)
url = connection.geturl()
print(url)
print(type(connection))
