#!/usr/bin/python

# dataset.csv
###-----------------------
#user,A,B,C,D,E,F,G,H,I,L
#user1,5,10,7,2,2,2,2,4,7,7
#user2,1,1,1,0,0,0,0,0,0,0
#user3,8,9,6,1,0,3,0,5,2,2
#user4,8,7,3,3,3,1,2,4,4,3
#user5,7,5,1,0,0,0,0,4,1,1
#user6,5,2,1,1,1,8,0,7,8,4
###-----------------------

import pandas as pd
import numpy as np
import itertools as it
from itertools import combinations

from scipy import spatial

df = pd.read_csv('dataset.csv',header=None,skiprows=1)
df_list = map(list, df.values)

res = {}

#for (ds1,ds2) in it.combinations(df_list, r=2) :
for (ds1,ds2) in it.product(df_list, repeat=2) :
    if ds1[0] != ds2[0] : # or add any other constraint
        result = 1 - spatial.distance.cosine(ds1[1:],ds2[1:])
        res[ds1[0]] = res.get(ds1[0],[])
        res[ds1[0]].append((ds2[0],result))

busy = set()
for user1,v in res.items():
    i = 0
    userlist = sorted(v,key=lambda x: x[1],reverse=True)
    user2 = userlist[i][0]
    while (i < len(userlist) -1 ) :
        if (user1 not in busy) and (user2 not in busy) :
            print "%s <-> %s" % (user1,user2)
            busy.add(user1)
            busy.add(user2)
            continue
        i += 1
        user2 = userlist[i][0]

