r = float(input("Radius in km: "))
x = r / 6371

def rho(x): 
    rho = a0 + a1 * x + a2 * x ** 2 + a3 * x ** 3
    rho = round(rho, 5)
    return rho 

def vp(x): 
    vp = b0 + b1 * x + b2 * x ** 2 + b3 * x ** 3
    vp = round(vp, 5)
    return vp

def vs(x): 
    vs = c0 + c1 * x + c2 * x ** 2 + c3 * x ** 3
    vs = round(vs, 5)
    return vs

def vpv(x):
    vpv = b0v + b1v * x
    vpv = round(vpv, 5)
    return vpv

def vph(x):
    vph = b0h + b1h * x
    vph = round(vph, 5)
    return vph

def vsv(x):
    vsv = c0v + c1v * x
    vsv = round(vsv, 5)
    return vsv

def vsh(x):
    vsh = c0h + c1h * x
    vsh = round(vsh, 5)
    return vsh

a0 = 0 
a1 = 0
a2 = 0
a3 = 0
   
b0 = 0
b1 = 0
b2 = 0
b3 = 0

c0 = 0
c1 = 0
c2 = 0
c3 = 0


if r <= 1221.5 and r > 0:
    a0 = 13.0885 
    a1 = 0
    a2 = -8.8381
    a3 = 0
    
    b0 = 11.2622
    b1 = 0
    b2 = -6.3640
    b3 = 0
    
    c0 = 3.6678
    c1 = 0
    c2 = -4.4475
    c3 = 0
elif r <= 3480 and r > 1221.5: 
    a0 = 12.5815
    a1 = -1.2638
    a2 = -3.6426
    a3 = -5.5281
       
    b0 = 11.0487
    b1 = -4.0362
    b2 = 4.8023
    b3 = -13.5732
    
    c0 = 0
    c1 = 0
    c2 = 0
    c3 = 0
elif r <= 3630 and r > 3480: 
    a0 = 7.9565
    a1 = -6.4761
    a2 = 5.5283
    a3 = -3.0807
       
    b0 = 15.3891
    b1 = -5.3181
    b2 = 5.5242
    b3 = -2.5514
    
    c0 = 6.9254
    c1 = 1.4672
    c2 = -2.0834
    c3 = 0.9783
elif r <= 5600 and r > 3630:
    a0 = 7.9565
    a1 = -6.4761
    a2 = 5.5283
    a3 = -3.0807
       
    b0 = 24.9520
    b1 = -40.4673
    b2 = 51.4832
    b3 = -26.6419
    
    c0 = 11.1671
    c1 = -13.7818
    c2 = 17.4575
    c3 = -9.2777
elif r <= 5701 and r > 5600: 
    a0 = 7.9565
    a1 = -6.4761
    a2 = 5.5283
    a3 = -3.0807
       
    b0 = 29.2766
    b1 = -23.6027
    b2 = 5.5242
    b3 = -2.5514
    
    c0 = 22.3459
    c1 = -17.2473
    c2 = -2.0834
    c3 = 0.9783
elif r <= 5771 and r > 5701: 
    a0 = 5.3197
    a1 = -1.4836
    a2 = 0
    a3 = 0
       
    b0 = 19.0957
    b1 = -9.8672
    b2 = 0
    b3 = 0
    
    c0 = 9.9839
    c1 = -4.9324
    c2 = 0
    c3 = 0
elif r <= 5971 and r > 5771: 
    a0 = 11.2494
    a1 = -8.0298
    a2 = 0
    a3 = 0
       
    b0 = 39.7027
    b1 = -32.6166
    b2 = 0
    b3 = 0
    
    c0 = 22.3512
    c1 = -18.5856
    c2 = 0
    c3 = 0
elif r <= 6151 and r > 5971:
    a0 = 7.1089
    a1 = -3.8045
    a2 = 0
    a3 = 0
       
    b0 = 20.3926
    b1 = -12.2569
    b2 = 0
    b3 = 0
    
    c0 = 8.9496
    c1 = -4.4597
    c2 = 0
    c3 = 0
elif r <= 6291 and r > 6151: 
    a0 = 2.6910
    a1 = 0.6924
    a2 = 0 
    a3 = 0
       
    b0v = 0.8317
    b1v =  7.2180
    
    b0h = 3.5908
    b1h =  4.6172
    
    c0v = 5.8582
    c1v =  -1.4678
    
    c0h = -1.0839
    c1h =  5.7176
elif r <= 6346.6 and r > 6291: 
    a0 = 2.6910 
    a1 = 0.6924
    a2 = 0
    a3 = 0
       
    b0v = 0.8317
    b1v =  7.2180
    
    b0h = 3.5908
    b1h = 4.6172
    
    c0v = 5.8582
    c1v =  -1.4678
    
    c0h = -1.0839
    c1h = 5.7176
elif r <= 6356 and r > 6346.6: 
    a0 = 2.9000
    a1 = 0
    a2 = 0
    a3 = 0
    
    b0 = 6.800
    b1 = 0
    b2 = 0
    b3 = 0
    
    c0 = 3.900
    c1 = 0
    c2 = 0
    c3 = 0
elif r <= 6368 and r > 6356: 
    a0 = 2.600
    a1 = 0
    a2 = 0
    a3 = 0
    
    b0 = 5.800
    b1 = 0
    b2 = 0
    b3 = 0
    
    c0 = 3.200
    c1 = 0
    c2 = 0
    c3 = 0
elif r <= 6371 and r > 6368: 
    a0 = 1.020
    a1 = 0
    a2 = 0
    a3 = 0
    
    b0 = 1.450
    b1 = 0
    b2 = 0
    b3 = 0
    
    c0 = 0
    c1 = 0
    c2 = 0
    c3 = 0 
    
    print("Radius value in the ocean.")
elif r < 0 or r > 6346.4: 
    a0 = 0 
    a1 = 0
    a2 = 0
    a3 = 0
       
    b0 = 0
    b1 = 0
    b2 = 0
    b3 = 0
    
    c0 = 0
    c1 = 0
    c2 = 0
    c3 = 0
    
    print("Invalid radius value.")
    

print("Density: ", rho(x), "gcm^-3")
if r <= 6346.6 and r > 6151: 
    print("P velocity (H): ", vph(x), "kms^-1")
    print("P velocity (V): ", vpv(x), "kms^-1")
    print("S velocity (H): ", vsh(x), "kms^-1")
    print("S velocity (V): ", vsv(x), "kms^-1")
else: 
    print("P velocity: ", vp(x), "kms^-1")
    print("S velocity: ", vs(x), "kms^-1")
