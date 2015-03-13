__author__ = 'penghu2'

from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
import xTestLoader
# from XTest.commons import JSONResponse
# import jsonpickle
import unittest.case as case
from  xTestSuit import  XTestSuit
from XTest.model.testmanager import TestManager

class UnitTestList(APIView):
    """
    unitTestView
    """
    def get(self, request, format=None):
        data={}
        return Response(data)

    def post(self, request, format=None):
        pass

class UnitTestDetial(APIView):
    """
    unittest detial, list the testcases set
    """
    def __init__(self, *kwargs):
        super(UnitTestDetial, self).__init__(*kwargs)
        self.manager = TestManager()

    def get(self, request, pk, format=None):
        pk = pk.encode('utf8')
        data=self.getJsonFromSuit(self.manager.getSuit(pk))
        return Response(data)

    def getJsonFromSuit(self, suit):
        res = {}
        if suit is None:
            return res

        res['name']=suit.name
        res['open']='true'
        res['type']=suit.type
        res['desc']=suit.desc
        childlist = []
        for s in suit:
            child={}
            if isinstance(s, XTestSuit):
                childlist.append(self.getJsonFromSuit(s))
            if isinstance(s, case.TestCase):
                child['name'] = s.id().split('.')[-1]+'()'
                childlist.append(child)
        res['children'] = childlist
        return res

    def getSuitFromJson(self, pk, jsonstr):
        s=[]
        return self.manager.getSuit(pk)

    def post(self, request, pk, format=None):
        data = request.data
        suit = self.getSuitFromJson(pk, data)
        result = self.manager.runSuit(suit, pk)
        str = self.manager.readBuffer(pk)

        resp={}
        if result.wasSuccessful():
            resp['status']='0000'
            resp['data']=str
            return Response(resp)

        else:
            resp['status']='1001'
            return Response(resp)

# def getTestDetail(request, pk):
#     xLoder = XTestLoader()
#     testsuit = xLoder.loadTestFromPath('C:/Users/penghu2/PycharmProjects/TestUnit/BVT_Test')
#     data=jsonpickle.encode(testsuit)
#     return JSONResponse(data)