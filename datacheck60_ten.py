
def dataCheck_ten(datalist):
    m = datalist[0]
    m1 = datalist[1]

    if m['Close'] > m1['Close'] and (m['Close'] - m1['Close'])/m1['Close'] > 0.095:
        return (True, 'UP,%f,%f,%f' % (m['Close'], m1['Close'], (m['Close'] - m1['Close'])/m1['Close']))
    elif m['Close'] < m1['Close'] and (m['Close'] - m1['Close'])/m1['Close'] < -0.095:
        return (True, 'Down,%f,%f,%f' % (m['Close'], m1['Close'], (m['Close'] - m1['Close'])/m1['Close']))

    return (False, 'NULL')

