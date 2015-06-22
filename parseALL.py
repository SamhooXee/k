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

def getCurrentValue(idlist, fromIdx, max):
    cnt = 0
    for idmap in idlist:
        cnt += 1
        if cnt > fromIdx:
            # print 'http://hq.sinajs.cn/list=%s' % (idmap['id'])
            url = 'http://hq.sinajs.cn/list=%s' % (idmap['id'])
            try:
                response = urllib2.urlopen(url)
                page = response.read()
                result = page.split(',')
                vOpen = (result[1])
                vClose = (result[3])
                vHigh = (result[4])
                vLow = (result[5])
                vVolume = (result[8])
                # print "%s,%s,%s" % (idmap['name'], idmap['id'], result[3])
                with open('usefulCurrent/%s.csv' % (idmap['id']), 'w') as f:
                    # print "# %s" % (idmap['id'])
                    # print "today,%s,%s,%s,%s,%s,0" % (vOpen, vClose, vHigh, vLow, vVolume)
                    f.write("today,%s,%s,%s,%s,%s,0" % (vOpen, vHigh, vLow, vClose, vVolume))
            except:
                print "# %d - %s" % (cnt, url)
            time.sleep(0.1)
        if cnt % 100 == 0:
            print "# %d done - current !" % cnt
        if cnt > max:
            break

def getHistory(idlist, fromIdx, toIdx, outputfile):
    cnt = 0
    with open(outputfile, 'w') as f:
        f.write("#!/bin/bash\n")
        for idmap in idlist:
            cnt += 1
            if cnt > fromIdx:
                cmd = 'curl -o %04d_%s.csv http://table.finance.yahoo.com/table.csv?s=%s &' % (cnt, idmap['tableid'], idmap['tableid'])
                # print 'echo %d:' % cnt
                # print 'touch %04d_%s.csv' % (cnt, idmap['tableid'])
                # print cmd
                # print 'sleep 0.5'
                f.write('echo %d:\n' % cnt) 
                f.write('touch %04d_%s.csv\n' % (cnt, idmap['tableid']))
                f.write(cmd+"\n")
                f.write('sleep 0.5\n')
            # time.sleep(0.1)
            if cnt > toIdx:
                break

if __name__ == '__main__':
    # print "#!/bin/bash"

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

    # getCurrentValue(idlist, 288, 288+10)
    # getHistory(idlist, 1304, 1304+10)

    # sz start from 1302
    getCurrentValue(idlist, 0, 9999)
    getHistory(idlist, 0, 9999, "gethistory.sh")

    print "# done!!! - %d" % (cnt)
