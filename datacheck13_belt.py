
def dataCheck_belt(datalist):
    m = datalist[0]
    m1 = datalist[1]
    m2 = datalist[2]
    m3 = datalist[3]

    if m['Low'] == m['Open'] and m['color'] == 'red':
        if m['instance_low'] < m1['instance_low'] and m1['instance_low'] < m2['instance_low']:
            return (True, 'BOTTOM,%f,%f' % (m['Close'], m['d_high2low']/m['d_instance']))
    elif m['High'] == m['Open'] and m['color'] == 'green':
        if m['instance_High'] < m1['instance_High'] and m1['instance_High'] < m2['instance_High']:
            return (True, 'TOP,%f,%f' % (m['Close'], m['d_high2low']/m['d_instance']))

    return (False, 'NULL')

