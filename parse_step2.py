
import os
import sys
import re
from datetime import *

# section 0
from datacheck0_stop import *
from datacheck1_hammer import *
from datacheck2_embrace import *
from datacheck3_darkcloud import *
from datacheck4_pierce import *
from datacheck5_morningStar import *
from datacheck12_flat import *
from datacheck13_belt import *
from datacheck21_window import *
from datacheck22_window_parallelRedGreen import *

from datacheck60_ten import *

TOIDX = 9999

idMap = {
    "ss": "sh",
    "sz": "sz"
}

def fileNameTransformSimple(input):
    result = re.search('(\d\d\d\d\d\d)\.(..).csv', input)
    if result:
        # print "./usefulCurrent/%s%s.csv" % (idMap[result.group(2)], result.group(1))
        return "%s%s" % (idMap[result.group(2)], result.group(1))
    return "NOTEXISTFILE"

# ./useful/0151_600000.ss.csv -> ./usefulCurrent/sh600000.csv
def fileNameTransform(input):
    result = re.search('(\d\d\d\d\d\d)\.(..).csv', input)
    if result:
        # print "./usefulCurrent/%s%s.csv" % (idMap[result.group(2)], result.group(1))
        return "./usefulCurrent/%s%s.csv" % (idMap[result.group(2)], result.group(1))
    return "NOTEXISTFILE"

def lineParse(line, datalist):
    result = line.split(',')
    datamap = {}
    datamap['Date'] = result[0]
    datamap['Open'] = float(result[1])
    datamap['High'] = float(result[2])
    datamap['Low'] = float(result[3])
    datamap['Close'] = float(result[4])
    datamap['Volume'] = float(result[5])
    if (datamap['Open'] > datamap['Close']):
        datamap['instance_high'] = datamap['Open']
        datamap['instance_low'] = datamap['Close']
    else:
        datamap['instance_high'] = datamap['Close']
        datamap['instance_low'] = datamap['Open'] 
    datamap['d_instance'] = abs(datamap['Open'] - datamap['Close'])
    datamap['d_high2low'] = datamap['High'] - datamap['Low']
    datamap['color'] = 'green'
    if (datamap['Close'] >= datamap['Open']): datamap['color'] = 'red'
    datalist.append(datamap)

def fileParse(filename, max):
    datalist = []
    errcnt = 0
    cnt = 0

    # current date
    try:
        with open(fileNameTransform(filename)) as f:
            for each in f:
                    lineParse(each, datalist)
                    cnt += 1
    except:
        print "%s not exist?" % (fileNameTransform(filename))
        errcnt += 1

    # history date
    with open(filename) as f:
        for each in f:
            try:
                lineParse(each, datalist)
                cnt += 1
            except:
                errcnt += 1
                # print "Fisrt line: %s?" % (filename)
            if cnt > max or errcnt > max:
                break
    if errcnt>1:
        print "%s - more than once: %d" % (filename, errcnt)
    
    # debug:
    # print "%s, %s" % (datalist[0]['Date'], datalist[1]['Date'])

    return datalist

def executeAll():
    cnt = 0

    # section 1
    stoplist = []
    stoplistERR = []
    hammerlist = []
    embracelist = []
    darkcloudlist = []
    piercelist = []
    morningStarlist = []
    flatlist = []
    beltlist = []
    windowlist = []
    windowParallellist = []
    tenlist = []

    for file in sorted(filelist):
        cnt += 1
        if cnt > TOIDX:
            break

        try:
            datalist = fileParse(file, 10)

            lastDateStr = datalist[1]['Date'].split('-')
            # print lastDateStr
            lastDate = date(int(lastDateStr[0]),int(lastDateStr[1]),int(lastDateStr[2]))
            # print lastDate
            currentDate = date.today()
            # print currentDate
            delta = currentDate - lastDate
            # print type(delta)
            # print type(delta.days)
            # print delta
            # print delta.days
            if delta.days > 4:
                continue
            if int(datalist[0]['Volume']) == 0:
                continue

            # section 2
            statusStop, dataStop = dataCheck_stop(datalist)
            statusHammer, dataHammer = dataCheck_hammer(datalist)
            statusEmbrace, dataEmbrace = dataCheck_embrace(datalist)
            statusDarkcloud, dataDarkcloud = dataCheck_darkcloud(datalist)
            statusPierce, dataPierce = dataCheck_pierce(datalist)
            statusMorningStar, dataMorningStar = dataCheck_morningStar(datalist)
            statusFlat, dataFlat = dataCheck_flat(datalist)
            statusWindow, dataWindow = dataCheck_window(datalist)
            statusWindowParallel, dataWindowParallel = dataCheck_window_parallelRedGreen(datalist)
            statusBelt, dataBelt = dataCheck_belt(datalist)
            statusTen, dataTen = dataCheck_ten(datalist)

            # section 3 - each 3 place to modify
            if (statusStop):
                if (dataStop!='ERR'):
                    print "%d,%s,0.stop,%s" % (cnt, file, dataStop)
                    stoplist.append(file)
                else:
                    stoplistERR.append(file)
            elif (statusHammer):
                print "%d,%s,01.hammer,%s" % (cnt, file, dataHammer)
                hammerlist.append(file)

            if (statusEmbrace):
                print "%d,%s,02.embrace,%s" % (cnt, file, dataEmbrace)
                embracelist.append(file)

            if (statusDarkcloud):
                print "%d,%s,03.darkcloud,%s" % (cnt, file, dataDarkcloud)
                darkcloudlist.append(file)

            if (statusPierce):
                print "%d,%s,04.pirece,%s" % (cnt, file, dataPierce)
                piercelist.append(file)

            if (statusMorningStar):
                print "%d,%s,05.morning star,%s" % (cnt, file, dataMorningStar)
                morningStarlist.append(file)

            if (statusFlat):
                print "%d,%s,12.flat,%s" % (cnt, file, dataFlat)
                flatlist.append(file)

            if (statusBelt):
                print "%d,%s,13.belt,%s" % (cnt, file, dataBelt)
                beltlist.append(file)

            if (statusWindow):
                print "%d,%s,21.window,%s" % (cnt, file, dataWindow)
                windowlist.append(file)

            if (statusWindowParallel):
                print "%d,%s,22.window parallel,%s" % (cnt, file, dataWindowParallel)
                windowParallellist.append(file)

            if (statusTen):
                print "%d,%s,60.percent 10,%s" % (cnt, file, dataTen)
                tenlist.append(file)

        except Exception, e:
            print "ERR %s" % (file)
            print e

    # section 4
    print '0.stop total %d' % (len(stoplist))
    print '0.1stop ERR total %d' % (len(stoplistERR))

    with open('list_stopERR.csv', 'w') as f:
        for each in stoplistERR:
            f.write(each + '\n')

    print '1.hammer total %d' % (len(hammerlist))
    print '2.embrace total %d' % (len(embracelist))
    print '3.darkcloud total %d' % (len(darkcloudlist))
    print '4.pierce total %d' % (len(piercelist))
    print '5.morning star total %d' % (len(morningStarlist))
    
    print '12.flat total %d' % (len(flatlist))
    print '13.belt total %d' % (len(flatlist))

    print '21.window total %d' % (len(windowlist))
    print '22.windowParallel total %d' % (len(windowParallellist))

    print '60.percent 10 total %d' % (len(tenlist))

if __name__ == '__main__':
    filelist = []
    for file in os.listdir('./useful'):
        if '.csv' in file:
            filelist.append("./useful/" + file)

    print 'total %d files' % (len(filelist))
    
    # fileNameTransform("./useful/0151_600000.ss.csv")
    # fileParse("./useful/0161_600010.ss.csv", 5)

    executeAll()

    print 'done!!!'
