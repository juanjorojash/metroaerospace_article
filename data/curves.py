import numpy as np
import matplotlib.pyplot as plt
import csv
import os
Voc = 2.690 * 2
Vmp = 2.409 * 2
Imp = 0.5029 * 3
Isc = 0.5196 * 3
Rs = ( Voc - Vmp ) / Imp
a = ( Vmp * ( 1 + ( Rs*Isc ) / Voc ) + Rs*( Imp - Isc ) ) / Voc
N = np.log( 2 - 2**a) / np.log ( Imp / Isc )
print("Rs = %f" % Rs)
print("a = %f" % a)
print("N = %f" % N)
v = np.array([])
i = np.array([])
vconv = np.array([])
p = np.array([])
for x in range(0, 1024):
    I = (x * Isc) / 1023.0
    V = Voc * np.log( 2 - ( ( I / Isc ) ** N ) )
    V = V / np.log( 2 )
    V = V - Rs * ( I - Isc )
    V = V / ( 1 + ( ( Rs * Isc) / Voc) )
    P = V * I 
    i = np.append(i, I)
    v = np.append(v, V)
    p = np.append(p, P)
    if i[x] < Imp:
        VCONV = v[x] + ( ( Voc - Vmp ) / 3 )
        vconv = np.append(vconv, VCONV)
    else:
        vconv = np.append(vconv, V) 
### Remove the csv file if it exists
try:
    os.remove("data.csv")
except:
    print("csv file does not exist")
### Open the file, append header, then append data
with open("data.csv", "ab") as file:
    np.savetxt(file, np.column_stack(['V','I','P','VC']) , delimiter = ",", fmt='%s')
    np.savetxt(file, np.column_stack([v,i,p,vconv]) , delimiter = "," , fmt='%1.4f' )
### Plot the IV curve
plt.plot(v,i)
#plt.plot(v,p)
plt.plot(vconv,i)
plt.show()