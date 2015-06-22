
import os

def fileCheck(filename):
    with open(filename) as f:
        cmd = ''
        if 'Date,Open' not in f.readline():
            cmd = 'mv %s nouse/' % (filename)
        else:
            cmd = 'mv %s useful/' % (filename)
        print cmd

def fileParse(filename):
    datalist = []
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
                print "# Fisrt line: $s?" % (filename)
    return datalist

print "#!/bin/bash"

for file in os.listdir('.'):
    if '.csv' in file:
        #print file
        fileCheck(file)

print '# done!!!'
