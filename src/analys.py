import os
import re

def listdir(path=".", name=None, dirlist=[]):
    files = os.listdir(path.decode('utf-8'))
    for i in files:
        if not re.match("mall_trans_statistics_*",i):
            print "not match:"+i
            continue
        file_path = path+os.sep+i
        if not os.path.isdir(file_path):
            dirlist.append(file_path)
            
    return dirlist

def parse_trans(trans, transMap={}):
    content = open(trans)
    for line in content:
        fields = line.strip().split(",")
        name = fields[2]
        if transMap.has_key(name):
            transMap[name].append(fields[1])
        else:            
            transMap[name]=[fields[1]]
    content.close()
    return transMap

def analyse(transMap={}):
    statisticFlie = open("statistic.txt",'w')
    for key in transMap:
        usetimes=transMap[key]
        result=0
        for time in usetimes:
            result+=int(time)
        avg=result/len(usetimes)
        statisticFlie.write(key+","+str(avg)+"\n")
    statisticFlie.close();

if __name__ == '__main__':
    print "starting..."
    list=[]
    transMap={}
    files =listdir("C:\\doc\\pywork\\trans\\malllog",None,list)
    for log in files:
        parse_trans(log, transMap)
    analyse(transMap)
    
