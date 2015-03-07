#encoding=utf-8
__author__ = 'penghu2'
import os,sys
from unittest.main import TestProgram
import xTestLoader
import xTestRunner
import types

class xTestProgram(object):
    def __init__(self, path=None, testRunner = xTestRunner.xTestRunner,
                 testLoader=xTestLoader.XTestLoader(),verbosity=2, failfast=None, buffer=None,
                 exit=None):

        self.path = path
        if path is None:
            self.path = os.getcwd()

        self.testRunner = testRunner
        self.testLoader = testLoader

        self.tests=[]
        self.verbosity=verbosity
        self.failfast=failfast
        self.buffer=buffer
        self.exit=exit
        self.creaTest()
        self.runTest()

    def creaTest(self):
        self.tests = self.testLoader.loadTestFromPath(self.path)

    def runTest(self):
        if isinstance(self.testRunner, (type, types.ClassType)):
            try:
                testRunner = self.testRunner(verbosity=self.verbosity,
                                             failfast=self.failfast,
                                             buffer=self.buffer)
            except TypeError:
                # didn't accept the verbosity, buffer or failfast arguments
                testRunner = self.testRunner()
        else:
            # it is assumed to be a TestRunner instance
            testRunner = self.testRunner
        self.result = testRunner.run(self.tests)
        if self.exit:
            sys.exit(not self.result.wasSuccessful())
        pass