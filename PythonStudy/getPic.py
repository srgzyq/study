from urllib2 import urlopen

#kittens = urlopen('http://placekitten.com/200/300')
kittens = urlopen('http://www.baidu.com/img/270_05c4d4f94af4827d5a75120a7f65798d.gif')

f = open('kittens.jpg', 'wb')
f.write(kittens.read())
f.close()
