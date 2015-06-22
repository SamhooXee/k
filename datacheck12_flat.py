
def dataCheck_flat(datalist):
    m = datalist[0]
    # m1 = datalist[1]
    # m2 = datalist[2]
    # m3 = datalist[3]
    # m4 = datalist[4]
    
    for i in range(1, 5):
        if m['High'] + 0.01 < datalist[i]['High']:
            return (False, 'NULL')
        elif abs(m['High'] - datalist[i]['High'])<0.01:
            return (True, 'TOP,%f,%d' % (m['Close'], i))
    
    for i in range(1, 5):
        if m['Low'] + 0.01 > datalist[i]['Low']:
            return (False, 'NULL')
        elif abs(m['Low'] - datalist[i]['Low'])<0.01:
            return (True, 'BOTTOM,%f,%d' % (m['Close'], i))

    return (False, 'NULL')

# for i in range(1, 5):
#   print i
