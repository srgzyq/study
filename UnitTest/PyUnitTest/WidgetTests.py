import unittest
#import Widget

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

"""class SimpleWidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget("The widget")
    # If setUp succeeded, the tearDown method will be run regardless of
    # whether or not runTest succeeded
    def tearDown(self):
        self.widget.dispose()
        self.widget = None

class DefaultWidgetSizeTestCase(SimpleWidgetTestCase):
    def runTest(self):
        assert widget.getSize() == (50,50), "incorrect default size"

class WidgetResizeTestCase(SimpleWidgetTestCase):
    def runTest(self):
        self.widget.resize(100,150)
        assert self.widget.getSize() == (100,150), 'wrong size after resize'
"""

# TestCase classses with several test methods
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget("The widget")
    def tearDown(self):
        self.widget.dispose()
        self.widget = None
    def testDefaultSize(self):
        assert self.widget.getSize() == (50,50), "incorrect default size"
    def testResize(self):
        self.widget.resize(100,150)
        assert self.widget.getSize() == (100,150), 'wrong size after resize'

# TestSuite
#widgetTestSuite = unittest.TestSuite() 
#widgetTestSuite.addTest(WidgetTestCase("testDefaultSize"))
#widgetTestSuite.addTest(WidgetTestCase("testResize"))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testDefaultSize"))
    suite.addTest(WidgetTestCase("testResize"))
    return suite

# suite = unittest.makeSuite(WidgetTestCase,'test')

#runner = unittest.TextTestRunner()
#widgetTestSuite = suite()
#runner.run(widgetTestSuite)

if __name__ == "__main__":
    unittest.main()


