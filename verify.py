

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
        if 'BOTOM' in each or 'BOTTOM' in each:
            if strInLine(strList, each) :
                currentfile = fileNameTransform(each)
                try:
                    result = re.search('TOM,(.*?),', each)
                    if result:
                        lastClose = result.group(1)
                        # print lastClose
                    v_lastClose = float(lastClose)

                    with open(currentfile) as f:
                        datalist = []
                        lineParse(f.readline(), datalist)
                        current = datalist[0]
                        v_percent = 100.0*(current['Close'] - v_lastClose) / v_lastClose
                        # print '%s - %s,%f,%f' % (currentfile, datalist[0]['color'], datalist[0]['Close'], v_percent)
                        print '%s,%f,%f,%f,%s' % (current['color'], current['Close'], v_lastClose, v_percent, each.rstrip())
                except Exception, e:
                    print '%s:' % (currentfile)
                    print e

print 'done!!!'