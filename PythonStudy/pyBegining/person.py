__metaclass__ = type

class Person:
    
    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print "Hello, world! I'm %s." % self.name

if __name__== "__main__":
    foo = Person()
    bar = Person()
    foo.setName('wangxuan')
    bar.setName('srgzyq')
    foo.greet()
    bar.greet()

