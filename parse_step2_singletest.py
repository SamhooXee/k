
import os
import sys

TOIDX = 9999

def fileParse(filename):
	datalist = []
	cnt = 0
	with open(filename) as f:
		for each in f:
			try:
				result = each.split(',')
				datamap = {}
				datamap['Date'] = result[0]
				datamap['Open'] = float(result[1])
				datamap['High'] = float(result[2])
				datamap['Low'] = float(result[3])
				datamap['Close'] = float(result[4])
				datalist.append(datamap)
			except:
				cnt += 1
				# print "Fisrt line: %s?" % (filename)
	if cnt>1:
		print "%s - more than once: %d" % (filename, cnt)
	return datalist

def dataCheck_stop(datalist):
	m = datalist[0]
	m2 = datalist[1]
	if (m['High'] == m['Open'] and m['High'] == m['Low'] and m['High'] == m['Close']):
		if(m['High'] > m2['Close']): return (True, 'UP')
		elif(m['High'] < m2['Close']): return (True, 'DOWN')
		else: return (True, 'ERR')
	return (False, 'None')

def dataCheck_hammer(datalist):
	m = datalist[0]
	d_h2l = m['High'] - m['Low']
	d_instance = abs(m['Open'] - m['Close'])
	if (m['High'] == m['Open'] and d_h2l >= d_instance*2):
		if (d_instance!=0): return (True, (d_h2l/d_instance))
		else: return (True, 0)
	if (m['High'] == m['Close'] and d_h2l >= d_instance*2):
                if (d_instance!=0): return (True, (d_h2l/d_instance))
                else: return (True, 0)
	return (False, 0)

def singletest(file):
	print file
	datalist = fileParse(file)
	statusStop, type = dataCheck_stop(datalist)
	statusHammer, data = dataCheck_hammer(datalist)
	if (statusStop):
		print "%s,stop,%s" % (file, type)
	elif (statusHammer):
		print "%s,hammer,%f" % (file, data)

print sys.argv[0]
print sys.argv[1]
singletest(sys.argv[1])

print 'done!!!'
