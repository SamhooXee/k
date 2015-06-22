

def dataCheck_window_index(datalist):
    for i in range(0, 10):
        if datalist[i]['Low'] > datalist[i+1]['High']:
            return (True, i, 'BOTTOM', '%d,%f,%f,%f,<-percent' % (i, datalist[i]['Low'], datalist[i+1]['High'],\
                                    100.0*(datalist[i]['Low'] - datalist[i+1]['High'])/datalist[i+1]['High']))
        elif datalist[i]['High'] < datalist[i+1]['Low']:
            return (True, i, 'TOP', '%d,%f,%f,%f,<-percent' % (i, datalist[i]['High'], datalist[i+1]['Low'],\
                                    100.0*(datalist[i]['High'] - datalist[i+1]['Low'])/datalist[i+1]['Low']))
    return (False, 0, 'NULL', 'NULL')

def dataCheck_window(datalist):
    status, index, data1, data2 = dataCheck_window_index(datalist)
    return (status, data1+','+data2)
