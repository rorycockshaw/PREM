rad0 = np.arange(0,1221.5,1)
rad1 = np.arange(1221.5,3480,1)
rad2 = np.arange(3480,5701,1)
rad3 = np.arange(5701,5771,1)
rad4 = np.arange(5771,5971,1)
rad5 = np.arange(5971,6151,1)
rad6 = np.arange(6151,6346.6,1)
rad7 = np.arange(6346.6,6356,1)
rad8 = np.arange(6356,6368,1)
rad9 = np.arange(6368,6371,1)

#0-1221.5
def rho0(i): 
    y0 = 13.0885 - 8.8381 * i ** 2
    return y0

#1221.5-3480
def rho1(i):  
    y1 = 12.5815 - 1.2638 * i - 3.6426 * i ** 2 - 5.5281 * i ** 2
    return y1

#3480-5701
def rho2(i): 
    y2 = 7.9565 - 6.4761 * i + 5.5283 * i ** 2 - 3.0807 * i ** 3
    return y2

#5701-5771
def rho3(i): 
    y3 = 5.3197 - 1.4836 * i
    return y3

#5771-5971
def rho4(i):  
    y4 = 11.2494 - 8.0298 * i
    return y4

#5971-6151
def rho5(i):
    y5 = 7.1089 - 3.8045 * i 
    return y5

#6151-6346.6
def rho6(i):
    y6 = 2.6910 + 0.6924 * i
    return y6

#6346.6-6356
def rho7(i):
    y7 = 2.9000
    return y7

#6356-6368
def rho8(i): 
    y8 = 2.6000
    return y8

#6368-6371
def rho9(i):
    y9 = 1.020
    return y9


rho0arr = np.array([])
rho1arr = np.array([])
rho2arr = np.array([])
rho3arr = np.array([])
rho4arr = np.array([])
rho5arr = np.array([])
rho6arr = np.array([])
rho7arr = np.array([])
rho8arr = np.array([])
rho9arr = np.array([])


for i in rad0: 
    rho0arr = np.append(rho0arr,rho0(i/6371))
for i in rad1: 
    rho1arr = np.append(rho1arr,rho1(i/6371))
for i in rad2: 
    rho2arr = np.append(rho2arr,rho2(i/6371))
for i in rad3: 
    rho3arr = np.append(rho3arr,rho3(i/6371))
for i in rad4: 
    rho4arr = np.append(rho4arr,rho4(i/6371))
for i in rad5: 
    rho5arr = np.append(rho5arr,rho5(i/6371))
for i in rad6: 
    rho6arr = np.append(rho6arr,rho6(i/6371))
for i in rad7: 
    rho7arr = np.append(rho7arr,rho7(i/6371))
for i in rad8: 
    rho8arr = np.append(rho8arr,rho8(i/6371))
for i in rad9: 
    rho9arr = np.append(rho9arr,rho9(i/6371))
    
#fill in the gaps

discont0 = [1221.5,rho0(1221.5/6371)]
discont1 = [1221.5,rho1(1221.5/6371)]
discont2 = [3480,rho1(3480/6371)]
discont3 = [3480,rho2(3480/6371)]
discont4 = [5701,rho2(5701/6371)]
discont5 = [5701,rho3(5701/6371)]
discont6 = [5771,rho3(5771/6371)]
discont7 = [5771,rho4(5771/6371)]
discont8 = [5971,rho4(5971/6371)]
discont9 = [5971,rho5(5971/6371)]
discont10 = [6151,rho5(6151/6371)]
discont11 = [6151,rho6(6151/6371)]
discont12 = [6346.6,rho6(6346.6/6371)]
discont13 = [6346.6,rho7(6346.6/6371)]
discont14 = [6356,rho7(6356/6371)]
discont15 = [6356,rho8(6356/6371)]
discont16 = [6368,rho8(6368/6371)]
discont17 = [6368,rho9(6368/6371)]

x_discont0_1 = [discont0[0],discont1[0]]
y_discont0_1 = [discont0[1],discont1[1]]

x_discont2_3 = [discont2[0],discont3[0]]
y_discont2_3 = [discont2[1],discont3[1]]

x_discont4_5 = [discont4[0],discont5[0]]
y_discont4_5 = [discont4[1],discont5[1]]

x_discont6_7 = [discont6[0],discont7[0]]
y_discont6_7 = [discont6[1],discont7[1]]

x_discont8_9 = [discont8[0],discont9[0]]
y_discont8_9 = [discont8[1],discont9[1]]

x_discont10_11 = [discont10[0],discont11[0]]
y_discont10_11 = [discont10[1],discont11[1]]

x_discont12_13 = [discont12[0],discont13[0]]
y_discont12_13 = [discont12[1],discont13[1]]

x_discont14_15 = [discont14[0],discont15[0]]
y_discont14_15 = [discont14[1],discont15[1]]

x_discont16_17 = [discont16[0],discont17[0]]
y_discont16_17 = [discont16[1],discont17[1]]

plt.plot(rad0,rho0arr, 'k')
plt.plot(x_discont0_1,y_discont0_1, 'k')
plt.plot(rad1,rho1arr, 'k')
plt.plot(x_discont2_3,y_discont2_3, 'k')
plt.plot(rad2,rho2arr, 'k')
plt.plot(x_discont4_5,y_discont4_5, 'k')
plt.plot(rad3,rho3arr, 'k')
plt.plot(x_discont6_7,y_discont6_7, 'k')
plt.plot(rad4,rho4arr, 'k')
plt.plot(x_discont8_9,y_discont8_9, 'k')
plt.plot(rad5,rho5arr, 'k')
plt.plot(x_discont10_11,y_discont10_11, 'k')
plt.plot(rad6,rho6arr, 'k')
plt.plot(x_discont12_13,y_discont12_13, 'k')
plt.plot(rad7,rho7arr, 'k')
plt.plot(x_discont14_15,y_discont14_15, 'k')
plt.plot(rad8,rho8arr, 'k')
plt.plot(x_discont16_17,y_discont16_17, 'k')
plt.plot(rad9,rho9arr, 'k')

plt.title("Preliminary Reference Earth Model")
plt.xlabel("Radius/km")
plt.ylabel("Density/g $cm^-3$")

plt.show()
