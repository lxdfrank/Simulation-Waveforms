import numpy as np
import matplotlib.pyplot as plt


## 方波

VV = []
tau = 0.25
tspan = np.arange(0,100.25,tau)
T1=tspan[-1]/10
n = 0
for t in tspan:
    # print(T1)
    if (t > T1+10*n) & (t < T1 + 5+10*n):
        I = -36
    elif(t >  T1 + 5+10*n) & (t < T1 + 10+10*n):
        I = 36
    else:
        I=0
    # if t > T1 +10+10*n:
    #     if n < 5:
    #         n = n + 1
    VV.append(I)
plt.figure(3)
plt.subplot(251)
plt.plot(tspan,VV)
plt.ylim(-36,36)
plt.xlabel("time/ms")
plt.ylabel("Voltage/V")
# plt.xticks([])
# plt.yticks([])

################################
## (A) tonic spiking
a=0.02
b=0.2
c=-65
d=6
V=-70
u=b * V
tau = 0.25
tspan = np.arange(0,100.25,tau)
T1=tspan[-1]/10
VV = []
uu = []
for t in tspan:
    if t > T1:
        I = 14
    else:
        # print(V)
        I = 0
    # print(type(V))
    V = V + tau * (0.04 * V ** 2 + 5 * V + 140 - u + I)
    u = u + tau * a * (b * V - u)
    if V > 30:
        VV.append(30)
        V = c
        u = u + d
    else:
        VV.append(V)
    uu.append(u)
# plt.figure(1)
plt.subplot(253)
plt.plot(tspan,VV)
plt.xticks([])
plt.yticks([])

#################################
a=0.03
b=0.25
c=-52
d=0
V=-64
u=b*V
VV=[]
uu=[]
tau = 0.2
tspan = np.arange(0,200.25,tau)
T1=tspan[-1]/10

##  rebound burst (N)
for t in tspan:
    if (t > T1) & (t < T1 + 5):
        I = -15
    else:
        I=0
    V = V + tau * (0.04 * V ** 2 + 5 * V + 140 - u + I)
    u = u + tau * a * (b * V - u)
    if V > 30:
        VV.append(30)
        V = c
        u = u + d
    else:
        VV.append(V)
    uu.append(u)
# plt.figure(2)
plt.subplot(252)
plt.plot(tspan,VV)
plt.xticks([])
plt.yticks([])
##################################
VV = []
tau = 0.25
tspan = np.arange(0,100.25,tau)
T1=tspan[-1]/10
n = 3
for t in tspan:
    # print(T1)
    if (t > T1+10*n) & (t < T1 + 5+10*n):
        I = -15
    elif(t >  T1 + 10+10*n) & (t < T1 + 15+10*n):
        I = 15
    else:
        I=0
    # if t > T1 +10+10*n:
    #     if n < 5:
    #         n = n + 1
    VV.append(I)
# plt.figure(4)
plt.subplot(254)
plt.plot(tspan,VV)
plt.xticks([])
plt.yticks([])
##########################################
###  P
a=0.1
b=0.26
c=-60
d=0
V=-61
u=b*V
VV=[]
uu=[]
tau = 0.25
tspan = np.arange(0,300.25,tau)
T1=300/8
T2 = 216
for t in tspan:
    if ((t>T1) & (t < T1+5)) | ((t>T2) & (t < T2+5)):
        I=1.24
    else:
        I=0.24
    V = V + tau*(0.04*V ** 2+5*V+140-u+I)
    u = u + tau*a*(b*V-u)
    if V > 30:
        VV.append(30)
        V = c;
        u = u + d;
    else:
        VV.append(V)
    uu.append(u)
# plt.figure(5)
plt.subplot(255)
plt.plot(tspan,VV)
plt.xticks([])
plt.yticks([])

######################################
## Figure 6
VV = []
tau = 0.25
tspan = np.arange(0,200.25,tau)
for t in tspan:

    if (t >20) & (t < 30):
        I = -30
    elif (t >= 30):
        I = 600.0/t
        # I = np.round(100.0/tspan,2)
    else:
        I = 0
    VV.append(I)
# VV = np.concatenate(VV,axis=0)
# plt.figure(6)
plt.subplot(256)
plt.plot(tspan,VV)
plt.xticks([])
plt.yticks([])


############################
## Figure 7
VV = []
tau = 0.25
tspan = np.arange(0,200.25,tau)
for t in tspan:
    if (t >5) & (t < 100):
        I = 1.03 ** t
    else:
        I = 0
    VV.append(I)
# VV = np.concatenate(VV,axis=0)
# plt.figure(7)
plt.subplot(257)
plt.plot(tspan,VV)
plt.xticks([])
plt.yticks([])

## Figure 8
VV = []
tau = 0.25
tspan = np.arange(0,200.25,tau)
for t in tspan:
    if (t >5) & (t < 150):
        I =  0.2*(t+30)
    else:
        I = 0
    VV.append(I)
# VV = np.concatenate(VV,axis=0)
# plt.figure(8)
plt.subplot(258)
plt.plot(tspan,VV)
plt.xticks([])
plt.yticks([])

## Figure 9
VV = []
tau = 0.25
tspan = np.arange(0,200.25,tau)
for t in tspan:
    if (t >20) & (t < 100):
        I =  0.2*(t-20)
    elif (t >=100) & (t < 180):
        I = -0.2 * (t-100 )+0.2*(80)
    else:
        I = 0
    VV.append(I)
# VV = np.concatenate(VV,axis=0)
# plt.figure(9)
plt.subplot(259)
plt.plot(tspan,VV)
plt.xticks([])
plt.yticks([])

## Figure 6
VV = []
tau = 0.25
tspan = np.arange(0,200.25,tau)
for t in tspan:
    if (t >20) & (t < 100):
        I=30
        if ((t > 37) &(t < 43))|((t > 57) &(t < 63))|((t > 77) &(t < 83)) :
            I=0
    else:
        I = 0
    VV.append(I)
# plt.figure(10)
plt.subplot(2,5,10)
plt.plot(tspan,VV)

plt.xticks([])
plt.yticks([])
plt.show()