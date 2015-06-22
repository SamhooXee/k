

import sys
import re
from parseALL import *
from parse_step2 import *

print sys.argv[1]

inputfile = sys.argv[1]

with open(inputfile) as f:
    for each in f:
        if 'percent 10' in each and 'UP' in each:
            theid = fileNameTransformSimple(each)
            print "http://image.sinajs.cn/newchart/daily/n/%s.gif" % (theid)

print 'done!!!'