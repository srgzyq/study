import urllib 
from sgmllib import SGMLParser

class URLLister(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.urls = []


    def start_a(self, attrs):
        href = [v for k, v in attrs if k=='href']
        if href:
            self.urls.append(href) 

class BaseHTMLProcessor(SGMLParser):
    def reset(self):
        self.pieces = []
        SGMLParser.reset(self)

    def unknow_starttag(self, tag, attrs):
        strattrs = "".join([' %s="%s"' % (key, value) for key, value in attrs ])
        self.pieces.append("<%(tag)s%(strattrs)s>" % locals())

    def unknow_endtag(self,tag):
        self.pieces.append("</%(tag)s/>" % locals())

    def handle_charref(self,ref):
        self.pieces.append("&#%(ref)s;" % locals())

    def handle_entityred(self, ref):
        self.pieces.append("&%(ref)s" % locals())
        if htmlentitydefs.entitydefs.has_key(ref):
            self.pieces.append(";")

    def handle_data(self,text):
        self.pieces.append(text)

    def handle_comment(self,text):
        self.pieces.append("<!--%(text)s-->" % locals())

    def handle_pi(self, text):
        self.pieces.append("<?%(text)s>" % locals())

    def handle_decl(self,text):
        self.pieces.append("<!%(text)s>" % locals())

    def output(self):
        """Return processed HTML as a single string"""
        return "".join(self.pieces)

if __name__ == "__main__":
    usock = urllib.urlopen("http://www.baidu.com")
    parser = URLLister()
    parser.feed(usock.read())
    usock.close()
    parser.close()
    for url in parser.urls:
        print url

