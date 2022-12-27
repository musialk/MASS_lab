import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pywt import wavedec, waverec
from scipy.signal import find_peaks

adn108 = pd.read_csv('108annotations.csv', delim_whitespace=True)
adn201 = pd.read_csv('201annotations.csv', delim_whitespace=True)

ecg108 = pd.read_csv('108.csv', sep=",")
ecg108 = ecg108[7000:9000]
ecg108 = ecg108/200
ecg201 = pd.read_csv('201.csv', sep=",")
ecg201 = ecg201[5000:7000]
ecg201 = ecg201/200

coeffs108MLII = wavedec(ecg108["'MLII'"], 'bior3.3', level=6)
cA1, cD6, cD5, cD4, cD3, cD2, cD1 = coeffs108MLII
cD6 = cD6 * 0
cD5 = cD5 * 0
cD4 = cD4 * 0
cD3 = cD3 * 0
cD2 = cD2 * 0
cD1 = cD1 * 0
MLII108 = waverec(coeffs108MLII, 'bior3.3')

coeffs108V1 = wavedec(ecg108["'V1'"], 'sym4', level=6)
cA2, cD6, cD5, cD4, cD3, cD2, cD1 = coeffs108V1
cD6 = cD6 * 0
cD5 = cD5 * 0
cD4 = cD4 * 0
cD3 = cD3 * 0
cD2 = cD2 * 0
cD1 = cD1 * 0
V1108 = waverec(coeffs108V1, 'sym4')

coeffs201MLII = wavedec(ecg201["'MLII'"], 'sym6', level=6)
cA3, cD6, cD5, cD4, cD3, cD2, cD1 = coeffs201MLII
cD6 = cD6 * 0
cD5 = cD5 * 0
cD4 = cD4 * 0
cD3 = cD3 * 0
cD2 = cD2 * 0
cD1 = cD1 * 0
MLII201 = waverec(coeffs201MLII, 'sym6')

coeffs201V1 = wavedec(ecg201["'V1'"], 'sym6', level=6)
cA4, cD6, cD5, cD4, cD3, cD2, cD1 = coeffs201V1
cD6 = cD6 * 0
cD5 = cD5 * 0
cD4 = cD4 * 0
cD3 = cD3 * 0
cD2 = cD2 * 0
cD1 = cD1 * 0
V1201 = waverec(coeffs201V1, 'sym6')

plt.figure(figsize=(18,11))
plt.subplot(221)
plt.plot(MLII108)
plt.title('Sygnal 108 - MLII')
plt.ylabel('Napięcie [V]')
plt.xlabel('Czas [s]')
plt.subplot(222)
plt.plot(V1108)
plt.title('Sygnal 108 - V1')
plt.ylabel('Napięcie [V]')
plt.xlabel('Czas [s]')
plt.subplot(223)
plt.plot(MLII201)
plt.title('Sygnal 201 - MLII')
plt.ylabel('Napięcie [V]')
plt.xlabel('Czas [s]')
plt.subplot(224)
plt.plot(V1201)
plt.title('Sygnal 201 - V1')
plt.ylabel('Napięcie [V]')
plt.xlabel('Czas [s]')
plt.show()

Rytm, _= find_peaks(MLII108, height=5.1)
peaks1 = Rytm / 360
RR1 = 60/(peaks1[1] - peaks1[0])
print(round(RR1,1))

Rytm, _= find_peaks(MLII201, height=5.5)
peaks2 = Rytm / 360
RR2 = 60/(peaks2[1] - peaks2[0])
print(round(RR2,1))

def detekcja(sygnal, adnotacja):
    TP=FN=FP=0
    tab=[]
    for value in adnotacja:
        czas=sygnal[value-27:value+27]
        Pik,_=find_peaks(czas, height=0.5*czas.max())
        if Pik.size==1:
            TP+=1
            FP+=Pik.size-1
            indeks=np.abs(Pik-27).argmin()
            tab.append(abs(Pik[indeks]-27))
        elif Pik.size<1:
            FN+=1
    #Se=round(TP / (TP + FN) * 100,2)
    #P=round(TP/(TP+FP)*100,2)
    return print('TP=',TP,'FP=',FP,"FN=",FN)

detekcja(MLII108,adn108['Sample'][3000:10000])
detekcja(MLII201,adn201['Sample'][3000:10000])