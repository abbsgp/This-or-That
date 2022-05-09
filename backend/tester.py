import time
import treeBasedDB

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import progressbar


nValues = []
getTime = []
searchTime = []
noiseReduce = 10000

db = treeBasedDB.dataBase(False)
bar = progressbar.ProgressBar(max_value=1000).start()
file = open("database2.csv", "r")
lines = file.readlines()
for i in range(5):
    kvpair = lines[i].split(",")
    db.insert(kvpair[0],int(kvpair[1]))
for i in range(5,1000):
    kvpair = lines[i].split(",")
    db.insert(kvpair[0],int(kvpair[1]))
    firsttime = 0
    secondtime = 0
    nValues.append(i)
    for j in range (noiseReduce):
        start = time.time_ns()
        tmp = db.getWords(5)
        gtime = time.time_ns()
        db.getMostPopular(tmp)
        etime = time.time_ns()
        firsttime += gtime-start
        secondtime += etime-gtime
    getTime.append(firsttime/noiseReduce)
    searchTime.append(secondtime/noiseReduce)
    bar.update(i)
    
plt.plot( nValues, getTime, "--", color="red", label="get random values" )
plt.plot( nValues, searchTime, color="blue", label="findmostpopular" )
plt.xlabel("n")
plt.ylabel("Time(ns)")
plt.legend()
plt.title("")
plt.show()
print("done")