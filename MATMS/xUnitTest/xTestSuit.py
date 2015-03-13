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