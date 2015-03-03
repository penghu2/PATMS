#encoding=utf-8
__author__ = 'penghu2'

from unittest.loader import TestLoader
from unittest.suite import TestSuite

class XTestLoader(TestLoader):

    def loadTestFromDir(self, dirname):
        """
        :param dirname: the dir, such as /home/test/myproject/testdir
        :return: a TestSuit class
        """

    pass
