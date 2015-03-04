#encoding=utf-8
__author__ = 'penghu2'

import os
from xtestSuit import XTestSuit


from unittest.loader import TestLoader
from unittest.suite import TestSuite
import unittest.case as case
import unittest.suite as suite


T_FILEPATH = 1
T_TESTCASE = 2
T_DIRPATH = 3

class XTestLoader(TestLoader):
    suiteClass = XTestSuit

    def loadTestsFromTestCase(self, testCaseClass):
        """Return a suite of all tests cases contained in testCaseClass"""
        if issubclass(testCaseClass, suite.TestSuite):
            raise TypeError("Test cases should not be derived from TestSuite." \
                                " Maybe you meant to derive from TestCase?")
        testCaseNames = self.getTestCaseNames(testCaseClass)
        if not testCaseNames and hasattr(testCaseClass, 'runTest'):
            testCaseNames = ['runTest']
        loaded_suite = self.suiteClass(map(testCaseClass, testCaseNames))
        loaded_suite.type = T_TESTCASE
        loaded_suite.desc = testCaseClass.__name__
        return loaded_suite

    def loadTestsFromModule(self, module, use_load_tests=True):
        """Return a suite of all tests cases contained in the given module"""
        tests = []
        for name in dir(module):
            obj = getattr(module, name)
            if isinstance(obj, type) and issubclass(obj, case.TestCase):
                tests.append(self.loadTestsFromTestCase(obj))

        if len(tests) == 0:
            return None

        load_tests = getattr(module, 'load_tests', None)
        tests = self.suiteClass(tests)
        if use_load_tests and load_tests is not None:
            try:
                return load_tests(self, tests, None)
            except Exception, e:
                return _make_failed_load_tests(module.__name__, e,
                                               self.suiteClass)
        return tests



    def loadTestFromPath(self, path, profix=None):
        """
        :param dirname: the dir, such as /home/test/myproject/testdir
        :return: a TestSuit class
        """
        tests=[]
        if not os.path.isdir(path):
            raise

        import sys
        sys.path.append(path)

        basedir = path
        fllelist = os.listdir(path)
        for f in fllelist:
            f_path = os.path.join(basedir,f)
            if os.path.isfile(f_path):
                if f.endswith("py"):
                    if (profix is not None) and (not f.startswith(profix)):
                        continue
                    if f=='init.py':
                        continue

                    parts = f.split('.')
                    try:
                        module = __import__(parts[0])
                        moduleSuit = self.loadTestsFromModule(module)
                        if moduleSuit is not None:
                            moduleSuit.type = T_FILEPATH
                            moduleSuit.desc = f_path
                            tests.append(moduleSuit)
                    except ImportError:
                        continue
            elif os.path.isdir(f_path):
                test = self.loadTestFromPath(f_path)
                if test is not None:
                    tests.append(test)
            else:
                continue
        sys.path.remove(path)

        if len(tests)==0:
            return None
        dirSuit =  self.suiteClass(tests)
        dirSuit.type = T_DIRPATH
        dirSuit.desc = path
        return dirSuit


def printSuit(xsuit):
    t = '-'*10
    print t+'\n', xsuit.type
    print xsuit.desc+'\n',t
    for s in xsuit:
        if isinstance(s, XTestSuit):
            printSuit(s)
        if isinstance(s, case.TestCase):
            print s.id()

if __name__ == '__main__':
    testloader = XTestLoader()
    suits =  testloader.loadTestFromPath("E:/temp/test")
    printSuit(suits)