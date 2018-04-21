##!/usr/bin/python
## coding=UTF-8

import os
from os import listdir
from os.path import isfile, join

path = "/Users/money/Downloads/0413_三國志_Android"

pcapFiles = [f for f in listdir(path) if isfile(join(path, f))]
os.system('mkdir ip')

filter = "'ip.src >= 192.168.137.2 && ip.src <= 192.168.137.255 && ip.dst != 192.168.137.1 && not icmp.type == 3'"

for file in pcapFiles:
    os.system('tshark -r ' + path + '/' + file 
              + ' -Y ' + filter 
              + ' -T fields -e ip.src -e ip.dst'
              + ' | sort -u'
              + ' > ./ip/' + file + '.txt')
    print "outputting file: " + file
    
path = './ip'
ipFiles = [f for f in listdir(path) if isfile(join(path, f))]
for file in ipFiles:
    with open(path + '/' + file, "r") as categoryFile:
        allIps = categoryFile.read()
        print 'file: ' + file + '\n' + allIps
    for lineIp in allIps.split('\n'):
        with open('category_ip', "a") as fCategory_ip:
            if(len(lineIp) > 0):
                fCategory_ip.write(file.split('.')[0] + '\t' + lineIp.split('\t')[1] + '\n')
                
