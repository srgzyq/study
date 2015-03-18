class Chain(object):
    
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self,path):
        return Chain('%s/%s' % (self._path,path))

    def user(self,name):
        return Chain('%s/%s' % (self._path,name))

    def __str__(self):
        return self._path

a = Chain()
#print a.status.user.timeline.list
print a.users.user('srgyzq').repos
