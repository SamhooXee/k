
from datacheck21_window import *

def dataCheck_window_parallelRedGreen(datalist):
    status, index, data1, data2 = dataCheck_window_index(datalist)
    if status and index==1 and \
            datalist[0]['instance_high'] > datalist[1]['instance_Low'] and \
            datalist[1]['instance_high'] > datalist[0]['instance_Low']:
        if data1 == 'BOTTOM':
            if datalist[0]['Low'] > datalist[2]['High'] and datalist[1]['Low'] > datalist[2]['High']:
                return (True, "BOTTOM,%f,%f,%f" % (datalist[0]['Low'], datalist[1]['Low'], datalist[2]['High']))
        elif data1 == 'TOP':
            if datalist[0]['High'] < datalist[2]['Low'] and datalist[1]['High'] < datalist[2]['Low']:
                return (True, "TOP,%f,%f,%f" % (datalist[0]['High'], datalist[1]['High'], datalist[2]['Low']))
    return (False, "NULL")