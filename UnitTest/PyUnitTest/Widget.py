class Widget:
    def __init__(self, name = "Widget",size = (50,50)):
        self._size = size
        self._name = name
    def getSize(self):
        return self._size
    def resize(self, width, height):
        if width < 0 or height < 0:
            raise ValueError, "illegal size"
        self._size = (width, height)
    def dispose(self):
        pass
