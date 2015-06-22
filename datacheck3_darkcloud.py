

def dataCheck_darkcloud(datalist):
    m = datalist[0]
    m1 = datalist[1]
    m2 = datalist[2]
    m3 = datalist[3]
    if m['color']=='green' and m1['color']=='red':
        if m['Open']>m1['Close'] and m['Close']>m1['Open']:
            # if m1['Close'] > m2['Close'] and m2['Close'] > m3['Close']:
                if m1['Open'] + m1['d_instance'] / 2 > m['Close']:
                    return (True, 'TOP,%f,%f,%f' % (m['Close'], m['d_instance'], m1['d_instance']))
    return (False, 'NULL')