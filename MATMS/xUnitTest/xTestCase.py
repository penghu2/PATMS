#encoding=utf-8
__author__ = 'penghu2'

from unittest import case
import chardet
import datetime

class ITestCase(case.TestCase):
    stream=None
    ifc=None

    @classmethod
    def _print(cls, msg):
        if cls.stream is not None and hasattr(cls.stream, 'writeln'):
            cls.stream.writeln(msg)
        else:
            print(msg)

    def setup(self):
        pass

    def tearDown(self):
        pass

    def setIfcInstance(self, ifc):
        self.ifc = ifc

    @property
    def stream(self):
        return self.__class__.stream

    @stream.setter
    def stream(self, value):
        self.__class__.stream = value

    def invoke(self, methodName, req):
        return self.ifc(method=methodName, req=req)

    def assertEqualUtf8(self, first, second, msg=None):
        first = str(first)
        second = str(second)
        if (((first is None) and (second is None)) or
            ((first is None) and (second=="")) or
            ((first is "") and (second==""))):
            return

        if not isinstance(first, unicode):
            #first = first.decode(chardet.detect(first)['encoding'])
            first = first.decode('utf-8')
        if not isinstance(second, unicode):
            #second = second.decode(chardet.detect(second)['encoding'])
            second = second.decode('utf-8')
        # print first,second
        assertion_func = self._getAssertEqualityFunc(first, second)
        assertion_func(first, second, msg=msg)

    def getdateTime(self, strDate):

        if isinstance(strDate, unicode):
            strDate = strDate.encode('utf8')
        return datetime.datetime.strptime(strDate,"%Y-%m-%d %H:%M:%S")
