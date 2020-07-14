#0-1221.5
def vs0(i):
    s0 = 3.6678 - 4.4475 * i ** 2
    return s0

#1221.5-3480
def vs1(i):
    s1 = 0
    return s1

#3480-3630
def vs2(i): 
    s2 = 6.9254 + 1.4672 * i - 2.0834 * i ** 2 + 0.9783 * i ** 3 
    return s2

#3630-5600
def vs3(i): 
    s3 = 11.1671 - 13.7818 * i + 17.4575 * i ** 2 - 9.2777 * i ** 3
    return s3

#5600-5701
def vs4(i): 
    s4 = 22.3459 - 17.2473 * i - 2.0834 * i ** 2 + 0.9783 * i ** 3
    return s4

#5701-5771
def vs5(i):
    s5 = 9.9839 - 4.9324 * i 
    return s5

#5771-5971
def vs6(i): 
    s6 = 22.3512 - 18.5856 * i
    return s6
    
#5971-6151
def vs7(i): 
    s7 = 8.9496 - 4.4597 * i
    return s7

#6151-6291
def vs8(i):
    s8 = 2.38715 + 2.1249 * i 
    return s8

#6291-6346.6 is the same as vp8
def vs9(i): 
    s9 = 2.38715 + 2.1249 * i 
    return s9

#6346.6-6356
def vs10(i): 
    s10 = 3.9000
    return s10

#6356-6368
def vs11(i): 
    s11 = 3.2000
    return s11

#6368-6371
def vs12(i):
    s12 = 0
    return s12

vs0arr = np.array([])
vs1arr = np.array([])
vs2arr = np.array([])
vs3arr = np.array([])
vs4arr = np.array([])
vs5arr = np.array([])
vs6arr = np.array([])
vs7arr = np.array([])
vs8arr = np.array([])
vs9arr = np.array([])
vs10arr = np.array([])
vs11arr = np.array([])
vs12arr = np.array([])

for i in rad0: 
    vs0arr = np.append(vs0arr,vs0(i/6371))
for i in rad1: 
    vs1arr = np.append(vs1arr,vs1(i/6371))
for i in rad2: 
    vs2arr = np.append(vs2arr,vs2(i/6371))
for i in rad3: 
    vs3arr = np.append(vs3arr,vs3(i/6371))
for i in rad4: 
    vs4arr = np.append(vs4arr,vs4(i/6371))
for i in rad5: 
    vs5arr = np.append(vs5arr,vs5(i/6371))
for i in rad6: 
    vs6arr = np.append(vs6arr,vs6(i/6371))
for i in rad7: 
    vs7arr = np.append(vs7arr,vs7(i/6371))
for i in rad8: 
    vs8arr = np.append(vs8arr,vs8(i/6371))
for i in rad9: 
    vs9arr = np.append(vs9arr,vs9(i/6371))
for i in rad10: 
    vs10arr = np.append(vs10arr,vs10(i/6371))
for i in rad11: 
    vs11arr = np.append(vs11arr,vs11(i/6371))
for i in rad12: 
    vs12arr = np.append(vs12arr,vs12(i/6371))
    
discont0 = [1221.5,vs0(1221.5/6371)]
discont1 = [1221.5,vs1(1221.5/6371)]
discont2 = [3480,vs1(3480/6371)]
discont3 = [3480,vs2(3480/6371)]
discont4 = [3630,vs2(3630/6371)]
discont5 = [3630,vs3(3630/6371)]
discont6 = [5600,vs3(5600/6371)]
discont7 = [5600,vs4(5600/6371)]
discont8 = [5701,vs4(5701/6371)]
discont9 = [5701,vs5(5701/6371)]
discont10 = [5771,vs5(5771/6371)]
discont11 = [5771,vs6(5771/6371)]
discont12 = [5971,vs6(5971/6371)]
discont13 = [5971,vs7(5971/6371)]
discont14 = [6151,vs7(6151/6371)]
discont15 = [6151,vs8(6151/6371)]
discont16 = [6346.6,vs8(6346.6/6371)]
discont17 = [6346.6,vs9(6346.6/6371)]
discont18 = [6356,vs9(6356/6371)]
discont19 = [6356,vs10(6356/6371)]
discont20 = [6368,vs10(6368/6371)]
discont21 = [6368,vs11(6368/6371)]

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

x_discont18_19 = [discont18[0],discont19[0]]
y_discont18_19 = [discont18[1],discont19[1]]

x_discont20_21 = [discont20[0],discont21[0]]
y_discont20_21 = [discont20[1],discont21[1]]
    
plt.plot(rad0,vs0arr, 'k')
plt.plot(rad1,vs1arr, 'k')
plt.plot(rad2,vs2arr, 'k')
plt.plot(rad3,vs3arr, 'k')
plt.plot(rad4,vs4arr, 'k')
plt.plot(rad5,vs5arr, 'k')
plt.plot(rad6,vs6arr, 'k')
plt.plot(rad7,vs7arr, 'k')
plt.plot(rad8,vs8arr, 'k')
plt.plot(rad9,vs9arr, 'k')
plt.plot(rad10,vs10arr, 'k')
plt.plot(rad11,vs11arr, 'k')
plt.plot(rad12,vs12arr, 'k')

plt.plot(x_discont0_1,y_discont0_1, 'k')
plt.plot(x_discont2_3,y_discont2_3, 'k')
plt.plot(x_discont4_5,y_discont4_5, 'k')
plt.plot(x_discont6_7,y_discont6_7, 'k')
plt.plot(x_discont8_9,y_discont8_9, 'k')
plt.plot(x_discont10_11,y_discont10_11, 'k')
plt.plot(x_discont12_13,y_discont12_13, 'k')
plt.plot(x_discont14_15,y_discont14_15, 'k')
plt.plot(x_discont16_17,y_discont16_17, 'k')
plt.plot(x_discont18_19,y_discont18_19, 'k')
plt.plot(x_discont20_21,y_discont20_21, 'k')

plt.title("S wave velocity against radius")
plt.xlabel("Radius/km")
plt.ylabel("Velocity/km $s^-1$")

plt.show()
