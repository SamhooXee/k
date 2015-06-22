# -*- coding: utf-8 -*
__author__ = 'abc'

import codecs
import re
import urllib2
import time

# original http://quote.eastmoney.com/stocklist.html

historyIdMap = {
    "sh": "ss",
    "sz": "sz"
}

print "#!/bin/bash"

# s = u'            <li><a target="_blank" href='.encode('utf-8')
# print type(s)
# print s
cnt = 0
idlist = []
with codecs.open("stocklist_utf8.html", "r", "utf-8") as fin:
    for each in fin:
        # print type(each)
        # s = '(\d\d\d\d\d\d).*</a>"&gt;</span>(.*)\((.*)\)<span'
        s = '(..)(\d\d\d\d\d\d).*span>(.*)\((.*)\)<span'
        # s = u'            <li><a target="_blank" href='.encode('utf8')
        # s = u'            <li><a target="_blank" href='
        # s = '            <li><a target="_blank" href='.encode('utf8')
        # s = '            <li><a target="_blank" href='
        result = re.search(s, each.encode('utf8'))
        if result:
            if result.group(4) == result.group(2):
                # print '%s - %s - %s' % (result.group(1), result.group(2), result.group(3))
                # idlist.append(result.group(1))
                idmap = {}
                idmap['id'] = result.group(1)+result.group(2)
                idmap['name'] = result.group(3)
                idmap['tableid'] = result.group(2) + '.' + historyIdMap[result.group(1)]
                idlist.append(idmap)
            else:
                print '# ERR - %s - %s - %s' % (result.group(1), result.group(2), result.group(3))
            # print type(result.group(1))
            # print type(result.group(2))
            # print len(result.group(2))
            # print each
            cnt += 1

def getCurrentValue(idlist, max):
    cnt = 0
    for idmap in idlist:
        cnt += 1
        # print 'http://hq.sinajs.cn/list=%s' % (idmap['id'])
        url = 'http://hq.sinajs.cn/list=%s' % (idmap['id'])
        try:
            response = urllib2.urlopen(url)
            page = response.read()
            result = page.split(',')
            print "%s,%s,%s" % (idmap['name'], idmap['id'], result[3])
            # print page.split(',')
        except:
            print "%d - %s" % (cnt, url)
        time.sleep(0.1)
        if cnt > max:
            break

def getCurrentGif(idlist, max, filter):
    cnt = 0
    for idmap in idlist:
        cnt += 1
        if filter in idmap['id']:
            print 'http://image.sinajs.cn/newchart/daily/n/%s.gif' % (idmap['id'])
        if cnt > max:
            break
			
def getHistory(idlist, fromIdx, toIdx):
    cnt = 0
    for idmap in idlist:
        cnt += 1
	if cnt > fromIdx:
	        cmd = 'curl -o %04d_%s.csv http://table.finance.yahoo.com/table.csv?s=%s &' % (cnt, idmap['tableid'], idmap['tableid'])
		print 'echo %d:' % cnt
		print 'touch %04d_%s.csv' % (cnt, idmap['tableid'])
        	print cmd
		print 'sleep 1'
        # time.sleep(0.1)
        if cnt > toIdx:
            break

# getCurrentValue(idlist, 9999)
# getCurrentValue(idlist, 2)
getCurrentGif(idlist, 9999, 'sz300')
# getHistory(idlist, 1304, 1304+10)
# getHistory(idlist, 0, 9999)

print "# done!!! - %d" % (cnt)
