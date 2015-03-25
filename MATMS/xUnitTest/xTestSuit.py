__author__ = 'penghu2'

from unittest.suite import TestSuite

class XTestSuit(TestSuite):
    def __init__(self, tests=()):
        """
        :param tests:  testcases
        :param __type: 1. file path  2. testcase class 3. dir path
        :param __desc:  correspond with type parameters
        :return:
        """
        super(XTestSuit, self).__init__(tests)
        self.__type=None
        self.__desc=None
        self.__name=None
        self.__stream = None

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def desc(self):
        return self.__desc

    @desc.setter
    def desc(self, value):
        self.__desc = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def stream(self):
        return self.__stream

    @stream.setter
    def stream(self, value):
        self.__stream=value

    def run(self, result, debug=False):
        topLevel = False
        if getattr(result, '_testRunEntered', False) is False:
            result._testRunEntered = topLevel = True

        for test in self:
            if result.shouldStop:
                break

            if self._isnotsuite(test):
                if hasattr(test, 'stream'):
                    test.stream = self.stream

                self._tearDownPreviousClass(test, result)
                self._handleModuleFixture(test, result)
                self._handleClassSetUp(test, result)
                result._previousTestClass = test.__class__

                if (getattr(test.__class__, '_classSetupFailed', False) or
                    getattr(result, '_moduleSetUpFailed', False)):
                    continue

            if not debug:
                if hasattr(test, 'stream'):
                    test.stream = self.stream
                test(result)
            else:
                test.debug()

        if topLevel:
            self._tearDownPreviousClass(None, result)
            self._handleModuleTearDown(result)
            result._testRunEntered = False
        return result

    def removeTest(self, test):
        self._tests.remove(test)

    def _isnotsuite(self,test):
        "A crude way to tell apart testcases and suites with duck-typing"
        try:
            iter(test)
        except TypeError:
            return True
        return False