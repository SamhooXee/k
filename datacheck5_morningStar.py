
def dataCheck_morningStar(datalist):
    m = datalist[0]
    m1 = datalist[1]
    m2 = datalist[2]
    m3 = datalist[3]
    m4 = datalist[4]
    # if m['color']=='red' and m1['color']=='green' and m2['color']=='green':
    if m2['instance_low'] > m1['instance_high'] and m2['instance_low'] < m['instance_high']:
        if m['instance_low'] > m1['instance_high']:
            if m2['instance_low'] < m3['instance_low'] and m['color'] == 'red':
                if m3['instance_low'] < m4['instance_low']:
                    return (True, 'BOTTOM,%f,' % (m['Close']))
    return (False, 'NULL')