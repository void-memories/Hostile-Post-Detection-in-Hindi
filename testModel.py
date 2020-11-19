import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("dataset.csv")
data2 = pd.read_csv("validation.csv")

sss=open('stopWords.txt')
stopWords=[]
for i in sss:
    stopWords.append(i[:len(i)-2])
# print(stopWords)

posts=list(data['Post'])
label=list(data['Labels Set'])
posts2=list(data2['Post'])
label2=list(data2['Labels Set'])

labelMaster={'hate':[],'offensive':[],'non-hostile':[],'defamation':[],'fake':[]}

#TRAINING
for index in range(len(posts)):
    ar=list(label[index].split(','))
    for i in ar:
        tokens=list(posts[index].split())
        for j in tokens:
            if j not in stopWords:
                labelMaster[i].append(j)
print('done')




total=0
correct=0
wrong=0

#VALIDATING
for index in range(len(posts2)):
    ar=list(label2[index].split(','))
    tokens=list(posts2[index].split())
    measure={'hate':0,'offensive':0,'non-hostile':0,'defamation':0,'fake':0}
    for j in tokens:
        for k in labelMaster:
            if j in k:
                measure[k]+=1
    total+=1

    X=list(measure.keys())
    Y=list(measure.values())
    [x for _,x in sorted(zip(Y,X))]

    
    if X[-1] in ar:
        correct+=1
    else:
        wrong+=1
            
print(str((correct/total)*100)[:5]+'%')
print(correct,wrong)
            
            