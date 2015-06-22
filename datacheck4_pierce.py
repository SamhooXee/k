
def dataCheck_pierce(datalist):
    m = datalist[0]
    m1 = datalist[1]
    m2 = datalist[2]
    m3 = datalist[3]
    if m['color']=='red' and m1['color']=='green':
        if m['Close']<m1['Open'] and m['Open']<m1['Close']:
            if m1['instance_low'] < m2['instance_low'] and m2['instance_low'] < m3['instance_low']:
            	if m1['Close'] + m1['d_instance'] / 2 < m['Close']:
                	return (True, 'BOTTOM,%f,%s,%s' % (m['Close'], m['d_instance'], m1['d_instance']))
    return (False, 'NULL')