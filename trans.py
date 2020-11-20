# from googletrans import Translator
# t = Translator()
# s="वह अपने कमरे में रो रही थी।"
# print(s)
# gg=(t.translate(s))
# print(gg.text)

# importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from googletrans import Translator

#load data

data = pd.read_csv("dataset.csv")
#removing urls & hashtags from the string

data['cleanPost'] = data['Post'].str.replace('http\S+|www.\S+|#\S+|@\S+', '', case=False)

columns_titles = ["cleanPost","Labels Set","Post"]
data=data.reindex(columns=columns_titles)

data=data.drop(data.columns[[2]], axis=1)

#Removing emojis and non-hindi characters for the translation

translationInput=[]
for i in data['cleanPost']:
    post=""
    for j in i:
        if (u'\u0900' <= j <= u'\u097f' or j==' '):
            if len(post)!=0 and post[-1]==' ' and j==' ':
                do='nothing'
            else:
                post+=j
    translationInput.append(post)


#Translating hindi to english using "googletrans" API
from googletrans import Translator
import time
errorCounter=0
cnt=0
eng=[]
f = open("res.txt", "a")
f.write("Now the file has more content!")
for i in range(5728):
    t=Translator()
    cnt+=1
    time.sleep(5)
    
    print(cnt,errorCounter)
    # if i%5==0:
    #     time.sleep(1)
    try:
        f.write(t.translate(translationInput[i]).text)
        f.write('\n')
    except:
        errorCounter+=1
print("Total Loss = " + str(errorCounter))