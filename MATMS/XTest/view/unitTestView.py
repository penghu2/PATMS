__author__ = 'penghu2'

from rest_framework.views import APIView
from rest_framework.response import Response

import unittest.case as case
from  xTestSuit import  XTestSuit
from XTest.model.testmanager import TestManager
import json
import pprint
import copy

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

    def getSuitFromJson(self, pk, data):
        res = json.loads(data['checkTree'])
        res_tree = None
        for item in res:
            if item.has_key(u'type') and item[u'type']==1:
                res_tree =  item
                break

        suit = self.manager.getSuit(pk)
        if res_tree is None:
            return None

        suits = None
        if res_tree[u'name'] == suit.name and res_tree[u'type'] == suit.type:
            testlist = self.testSuitFilter(suit, res_tree)
            print testlist
            suits = XTestSuit(testlist)

        return suits

    # def testSuitFilter(self, testSuit, selectTree):
    #     for j in testSuit:
    #         do_have = False
    #         for i in selectTree[u'children']:
    #             if hasattr(j, 'type') and i.has_key(u'type'):
    #                 if j.type == i[u'type']:
    #                     if j.name == i[u'name'] and i[u'checked']==True:
    #                         do_have = True
    #                         continue
    #             else:
    #                 # here means this is the testcase class
    #                 if j.id().split('.')[-1]+'()' == i[u'name'] and i[u'checked']==True:
    #                     do_have=True
    #                     continue
    #
    #         # if not do_have:
    #         #     testSuit.removeTest(j)
    #         #     continue
    #
    #         if i[u'isParent'] is True:
    #             self.testSuitFilter(j,i)

    def testSuitFilter(self, testSuit, selectTree):
        testlist=[]
        for j in testSuit:
            for i in selectTree[u'children']:
                if hasattr(j, 'type') and i.has_key(u'type'):
                    if j.type == i[u'type']:
                        if j.name == i[u'name'] and i[u'checked']==True:
                            testlist += (self.testSuitFilter(j,i))
                            continue
                else:
                    # here means this is the testcase class
                    if j.id().split('.')[-1]+'()' == i[u'name'] and i[u'checked']==True:
                        testlist.append(j)
                        continue

        return testlist

    def post(self, request, pk, format=None):
        data = request.data
        suit = self.getSuitFromJson(pk, data)
        result = self.manager.runSuit(suit, pk)
        print result
        str = self.manager.readBuffer(pk)
        #self.manager.closeBuffer(pk)
        resp={}
        if result.wasSuccessful():
            resp['status']='0000'
            resp['data']=str
            return Response(resp)

        else:
            resp['status']='1001'
            resp['data']=str
            return Response(resp)

# def getTestDetail(request, pk):
#     xLoder = XTestLoader()
#     testsuit = xLoder.loadTestFromPath('C:/Users/penghu2/PycharmProjects/TestUnit/BVT_Test')
#     data=jsonpickle.encode(testsuit)
#     return JSONResponse(data)