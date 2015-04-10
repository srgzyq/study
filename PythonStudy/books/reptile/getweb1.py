#encoding:UTF-8
import urllib.request

url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
print(data)

data = urllib.request.urlopen(url)

print(type(data))
print(data.geturl())
print(data.info())
print(data.getcode())
