
def dataCheck_hammer(datalist):
    m = datalist[0]
    m1 = datalist[1]
    m2 = datalist[2]
    # m3 = datalist[3]
    # d_h2l = m['d_high2low']
    d_instance = m['d_instance']
    if (10*(m['High'] - m['instance_high']) < (m['instance_low'] - m['Low']) and (m['instance_low'] - m['Low']) >= d_instance*2):
        status = 'UNKNOWN'
        percent = 0
        if m['instance_low'] <= m1['instance_low'] and m1['instance_low'] <= m2['instance_low']:
            status = 'BOTTOM'
            percent = 100.0* (m['Close'] - m1['Close']) / m1['Close']
        if m['instance_high'] >= m1['instance_high'] and m1['instance_high'] >= m2['instance_high']:
            status = 'TOP'
            percent = 100.0* (m['Close'] - m1['Close']) / m1['Close']
        if (d_instance!=0):
            return (True, "%s,%f,%f,%s,%f,\
                        %f,%f,%f,%f,%f,%f" % (status, m['Close'], ((m['instance_low'] - m['Low'])/d_instance), m['color'], percent, \
                                            m['instance_low'], m1['instance_low'], m2['instance_low'], \
                                            m['instance_high'], m1['instance_high'], m2['instance_high']))
        else: 
            return (True, "%s,0,%s,%f" % (status, m['color'], percent))
    return (False, "0")
