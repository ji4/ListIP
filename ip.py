##!/usr/bin/python
## coding=UTF-8
import os
from os import listdir
from os.path import isfile, join
from myDict import *

path = "/Users/money/Downloads/0413_三國志_Android"
filter = "'ip.src >= 192.168.137.2 && ip.src <= 192.168.137.255 && not ((ip.dst >= 192.168.0.0 && ip.dst <= 192.168.255.255) || (ip.dst >= 224.0.0.0 && ip.dst <= 239.255.255.255)) && not icmp.type == 3'"
fileNames = ['FbLogin', 'GoogleLogin', 'GuestLogin',
             'FbPersonal', 'GooglePersonal', 'GuestPersonal',
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
        print "outputting file: " + file + ".txt"

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
def sortByCategory():
    with open('category_ip_unsorted', 'r') as fOldCategory_ip, open('category_ip_sorted', 'a+') as fNewCategory_ip:
        categoryIps = fOldCategory_ip.read()
        categoryIpSet = set()
        for fileName in fileNames:
            for line in categoryIps.strip().split('\n'):
                ip = line.split('\t')[dstIpIndex]
                appendLine = fileName + '\t' + ip
                if line.startswith(fileName) and appendLine not in categoryIpSet:
                    isp, country = searchISP_Country(ip)
                    if not isp.startswith('MICROSOFT-CORP'):
                        if isp != '#N/A':
                            fNewCategory_ip.write(appendLine + '\t' + isp + '\t' + allcn[country] +'('+ country + ')\n')
                        categoryIpSet.add(appendLine)
                    else: print 'Filtered an IP from MS. IP: '+ip
    os.system('rm category_ip_unsorted')

def searchISP_Country(ip):
    cmd = "whois -h whois.cymru.com \" -v %s\"" % ip
    res = os.popen(cmd).read()
    if(len(res) > 0):
        res = res.split("\n")[1]
        data = res.split('|')
        cn = data[3].strip()
        isp = data[6].strip()

        if "," in isp: #filter NA
            print "%s\t%s\t%s(%s)" % (ip, isp.split(',')[0], allcn[cn], cn)
        if cn in allcn.keys():
            return (isp.split(',')[0], cn)
    
    saveToLog(ip)
    return ('#N/A','#N/A') 

def saveToLog(ip):
    print "Found unidentified ip: " + ip + ", saved to unidentified.txt"
    with open('unidentified', 'a+') as fLog:
        fLog.write(ip + "\n")

if __name__ == "__main__":
    pcapToTxt()
    listAllIps()
    sortByCategory()
