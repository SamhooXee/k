

import sys
import re
from parseALL import *
from parse_step2 import *

print sys.argv[1]

strList = [
'hammer',
'embrace',
'pirece',
'morning star',
'belt',
'flat'
]

def strInLine(thelist, line):
    for each in thelist:
        if each in line:
            return True
    return False

inputfile = sys.argv[1]

with open(inputfile) as f:
    for each in f:
        if 'BOTTOM' in each and 'green' not in each:
            if strInLine(strList, each) :
                theid = fileNameTransformSimple(each)
                print "http://image.sinajs.cn/newchart/daily/n/%s.gif" % (theid)

print 'done!!!'