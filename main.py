#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
import pickle
import numpy as np
import sys
sys.stdout = open('output_normal.csv','w')
#sys.stdout = open('output_poisson.csv','w')

day = 1
nowTime = []
floorNow = []
floorGo = []
count = 0
Kt=3 #한층 이동하는데 걸리는 시간 상수
Ke=1 #한층 이동하는데 소비하는 전력 상수
OpenCloseTime=10 #엘레베이터 문 두번 열고닫히는 시간

mini = 100000 #최소 대기시간
mini_t = 0 #최소 대기시간을 만들어주는 시간t
mini_f = 0 #최소 대기시간을 만들어주는 층f
t_move = 150 
f_move = 150

t = [6,8,17,20,24]
upP = [60,4,45,70,75]
downP = [30,96,45,28,23]
inter = [1800,300,600,450,900]

def probablistic_move(upP, downP):
    p = random.randrange(1,101)
    if(p <= upP): up()
    elif(p <= upP + downP): down()
    else: move()
def up():
    floorNow.append(0)
    floorGo.append(random.randrange(1,10))
def down():
    floorNow.append(random.randrange(1,10))
    floorGo.append(0)
def move():
    f= random.randrange(1,10)
    ff =random.randrange(1,10)
    if f == ff: move()
    else:
        floorNow.append(f)
        floorGo.append(ff)

def time_add(nTime, ran):
    nowTime.append(nTime)
    return abs(round(np.random.normal(ran/2,100)))
   # return abs(np.random.poisson(ran/2))

def waiting(count):
    waitingTime = 0
    for ii in range(count-1):
        if nowTime[ii+1] - (nowTime[ii] + Kt * abs( floorGo[ii] - f_move ) + Kt * abs( f_move - floorNow[ii+1]) ) > t_move:
            waitingTime += Kt * abs( f_move - floorNow[ii+1] ) + OpenCloseTime
            #print("if")
        else:
            #print(nowTime[ii+1],nowTime[ii],Kt * abs( floorGo[ii] - f_move ),Kt * abs( f_move - floorNow[ii+1]))
            waitingTime += Kt * abs( floorGo[ii] - floorNow[ii+1] )
    return waitingTime

def power(count): 
    powerUse = 0
    for jj in range(count -1):
        powerUse += Ke*( abs(floorGo[jj-1] - floorNow[j])+ abs(floorNow[jj] - floorGo[jj]) )
    return powerUse
for d in range(day):
    time =random.randrange(0,600) ##초기시간 설정
    for j in range(5):
        for i in range(1000):
            if time>=t[j]*3600:
                time= t[j]*3600+ random.randrange(0,300)
                break
            probablistic_move(upP[j], downP[j])
            time+= time_add(time, inter[j])
            count+=1
            
    print(count)        
    for k in range(count):
        print(nowTime[k],floorNow[k],floorGo[k], sep=' ')
        
for t in range(30,6001):
    for f in range(0,10):
        t_move = t
        f_move = f
        Time_wait = waiting( count )
        print(t,f,"T = ", Time_wait)
        if Time_wait < mini:
            mini = Time_wait
            mini_f = f
            mini_t = t
print(mini_t,mini_f)

   
with open('nowtime.pickle', 'wb') as time:
    pickle.dump(nowTime, time)
with open('nowtime.pickle', 'wb') as floorN:
    pickle.dump(floorNow, floorN)
with open('nowtime.pickle', 'wb') as floorG:
    pickle.dump(floorGo, floorG)


# In[6]:





# In[ ]:




