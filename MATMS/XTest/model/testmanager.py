#encoding=utf-8
__author__ = 'penghu2'
import StringIO
import xTestProgram
import xTestLoader

class TestManager(object):
    bufferStream = {}
    position = {}
    suitsList = {}
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(TestManager, cls).__new__(cls, *args)
        return cls.__instance

    def getSuit(self, key):
        if not self.suitsList.has_key(key):
            self.suitsList[key]=self.loadsuit(key)
        return self.suitsList[key]

    def loadsuit(self, key):
        xloder = xTestLoader.XTestLoader()
        testsuit = xloder.loadTestFromPath('F:/python/TestPro/')
        return testsuit

    def addSuit(self, key, suit):
        if not self.suitsList.has_key(key):
            self.suitsList[key]=suit

    def getBuffStream(self, key):
        if not self.bufferStream.has_key(key):
            self.bufferStream[key] = StringIO.StringIO()
        return self.bufferStream[key]

    def runSuit(self, suit, key):
        testDriver = xTestProgram.xTestProgram(stream=self.getBuffStream(key))
        return testDriver.runTestSuit(suit, ifHtml=True)

    def readBuffer(self, key):
        if self.bufferStream[key] is not None:
            if not self.position.has_key(key):
                self.position[key]=0
            self.bufferStream[key].seek(self.position[key])
            str = self.bufferStream[key].read()
            self.position[key]=self.bufferStream[key].tell()
            return str
        return None

    def closeBuffer(self, key):
        self.bufferStream[key].close()
        self.bufferStream.pop(key)
        self.position.pop(key)
