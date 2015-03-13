#encoding=utf-8
__author__ = 'penghu2'

from unittest.runner import TextTestRunner,TextTestResult


class _WriteBrDecorator(object):
    """Used to decorate file-like objects with a handy 'writeln' method"""
    def __init__(self,stream):
        self.stream = stream

    def __getattr__(self, attr):
        if attr in ('stream', '__getstate__'):
            raise AttributeError(attr)
        return getattr(self.stream,attr)

    def writeln(self, arg=None):
        if arg:
            self.write(arg)
        self.write('<br/>') # text-mode streams translate to \r\n if needed

class xTestRunner(TextTestRunner):
    """
    xTestRunner, control the test procedures, and send message to the System
    """
    resultclass = TextTestResult

    def __init__(self, stream, descriptions=True, verbosity=1,
                 failfast=False, buffer=False, resultclass=None):
        super(xTestRunner, self).__init__(stream, descriptions, verbosity,
                 failfast, buffer, resultclass)

        self.stream = _WriteBrDecorator(stream)

