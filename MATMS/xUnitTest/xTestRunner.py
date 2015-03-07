#encoding=utf-8
__author__ = 'penghu2'

from unittest.runner import TextTestRunner,TextTestResult


class xTestRunner(TextTestRunner):
    """
    xTestRunner, control the test procedures, and send message to the System
    """
    resultclass = TextTestResult
