
def dataCheck_stop(datalist):
    m = datalist[0]
    m2 = datalist[1]
    if (m['High'] == m['Open'] and m['High'] == m['Low'] and m['High'] == m['Close']):
        if(m['High'] > m2['Close']): return (True, 'UP')
        elif(m['High'] < m2['Close']): return (True, 'DOWN')
        else: return (True, 'ERR')
    return (False, 'None')
