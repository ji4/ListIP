##!/usr/bin/python
## coding=UTF-8

import os
from os import listdir
from os.path import isfile, join

path = "/Users/money/Downloads/0413_三國志_Android"
filter = "'ip.src >= 192.168.137.2 && ip.src <= 192.168.137.255 && ip.dst != 192.168.137.1 && not icmp.type == 3'"
fileNames = ['FbLogin', 'FbPersonal',
            'GoogleLogin','GooglePersonal',
            'GuestLogin', 'GuestPersonal',
            'Gaming',
            'Money']
fileNameIndex = 0
dstIpIndex = 1

def pcapToTxt():
    pcapFiles = [f for f in listdir(path) if isfile(join(path, f))]
    os.system('mkdir ip')
    for file in pcapFiles:
        os.system('tshark -r ' + path + '/' + file 
                  + ' -Y ' + filter 
                  + ' -T fields -e ip.src -e ip.dst'
                  + ' | sort -u'
                  + ' > ./ip/' + file + '.txt')
        print "outputting file: " + file
        
def listAllIps():    
    path = './ip'
    ipFiles = [f for f in listdir(path) if isfile(join(path, f))]
    for file in ipFiles:
        with open(path + '/' + file, "r") as categoryFile:
            categoryIps = categoryFile.read()
            print 'file: ' + file + '\n' + categoryIps
        for lineIp in categoryIps.split('\n'):
            with open('category_ip_unsorted', "a") as fCategory_ip:
                if(len(lineIp) > 0):
                    fCategory_ip.write(file.split('.')[fileNameIndex] + '\t' + lineIp.split('\t')[dstIpIndex] + '\n')
def sortAllData():
    with open('category_ip_unsorted', 'r') as fOldCategory_ip, open('category_sorted', 'a+') as fNewCategory_ip:
        categoryIps = fOldCategory_ip.read()
        content = set()
        for fileName in fileNames:
            for line in categoryIps.strip().split('\n'):
                appendedline = fileName + '\t' + line.split('\t')[dstIpIndex]
                if line.startswith(fileName) and appendedline not in content:
                    fNewCategory_ip.write(appendedline + '\n')
                    content.add(appendedline)
            
if __name__ == "__main__":
    pcapToTxt()
    listAllIps()
    sortAllData()