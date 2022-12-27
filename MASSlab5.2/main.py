import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pywt.data
from numpy import ndarray
from scipy.signal import find_peaks, peak_widths

sygnal1808 = pd.read_csv('1823.csv', sep=",")

#zobrazowanie danych pomiarowych
plt.figure(figsize=(12,10))
plt.subplot(3, 1, 1)
plt.plot(sygnal1808['ECG'][5500:6500])
plt.title('Sygnał ECG')
plt.subplot(3, 1, 2)
plt.plot(sygnal1808['IMP'][5500:6500])
plt.title('Sygnał IMP')
plt.subplot(3, 1, 3)
plt.plot(sygnal1808['Z0'][5500:6500])
plt.title('Sygnał Z0')
plt.show()

#__________________________Sygnal EKG_______________________________
#wyznaczenie QRS
coeffs8 = pywt.wavedec(sygnal1808['ECG'][5000:6000], 'coif5', level=4)
cA2, cD4, cD3, cD2, cD1 = coeffs8
cD4 *= 0
cD3 *= 0
cD2 *= 0
cD1 *= 0
c8 = pywt.waverec(coeffs8, 'coif5')

peaks8: ndarray = (find_peaks(c8, height=100))[0]

#określenie połowy długości pomiędzy pikami

odleglosc1 = (peaks8[1]-peaks8[0])/200
polowa1 = odleglosc1/2
print("polowa odleglosci w ECG dla w s: ", polowa1)

odleglosc2 = (peaks8[2]-peaks8[1])/200
polowa2 = odleglosc2/2
print("polowa odleglosci w ECG dla w s: ", polowa2)

odleglosc3 = (peaks8[3]-peaks8[2])/200
polowa3 = odleglosc3/2
print("polowa odleglosci w ECG dla w s: ", polowa3)

odleglosc4 = (peaks8[4]-peaks8[3])/200
polowa4 = odleglosc4/2
print("polowa odleglosci w ECG dla w s: ", polowa4)


#wykres z podzialami
p = 112
kropka1 = round(((peaks8[1]-peaks8[0])/2))
kropka2 = round((peaks8[2]-peaks8[1])/2+p)
kropka3 = round(((peaks8[3]-peaks8[2])/2)+(p*2))
kropka4 = round(((peaks8[4]-peaks8[3])/2)+(p*3))
kropka5 = round(((peaks8[4]-peaks8[3])/2)+(p*4))

plt.plot(c8)
plt.plot(peaks8, c8[peaks8], "*", kropka5, c8[kropka5], "x",kropka4, c8[kropka4], "x", kropka3,  c8[kropka3], "x", kropka2, c8[kropka2], "x", kropka1,  c8[kropka1], "x")
plt.show()

#___________________________Sygnal IMP______________________________
#wykonanie pochodnej sygnału IMP
plt.figure(figsize=(18,12))
rozniczka8 = np.diff(sygnal1808['IMP'][5000:6000])
plt.plot(rozniczka8)
plt.show()

coeffsIMP = pywt.wavedec(sygnal1808['IMP'][5000:6000], 'coif5', level=4)
cA1, ck4, ck3, ck2, ck1 = coeffsIMP
ck4 *= 0
ck3 *= 0
ck2 *= 0
ck1 *= 0
cIMP = pywt.waverec(coeffsIMP, 'coif5')

peaksIMP: ndarray = (find_peaks(cIMP, height=100000))[0]
plt.plot(cIMP)
plt.plot(peaksIMP, cIMP[peaksIMP], "x")
plt.show()

#określenie połowy długości pomiędzy pikami
odleglosc1IMP = (peaksIMP[1]-peaksIMP[0])/200
polowa1IMP = odleglosc1IMP/2
print("polowa odleglosci w IMP dla w s: ", polowa1IMP)

odleglosc2IMP = (peaksIMP[2]-peaksIMP[1])/200
polowa2IMP = odleglosc2IMP/2
print("polowa odleglosci w IMP dla w s: ", polowa2IMP)

odleglosc3IMP = (peaksIMP[3]-peaksIMP[2])/200
polowa3IMP = odleglosc3IMP/2
print("polowa odleglosci w IMP dla w s: ", polowa3IMP)

odleglosc4IMP = (peaksIMP[4]-peaksIMP[3])/200
polowa4IMP = odleglosc4IMP/2
print("polowa odleglosci w IMP dla w s: ", polowa4IMP)

#wykres z podzialami
p = 180
kropka1IMP = round(((peaksIMP[1]-peaksIMP[0])/2))
kropka2IMP = round((peaksIMP[2]-peaksIMP[1])/2+p)
kropka3IMP = round(((peaksIMP[3]-peaksIMP[2])/2)+(p*2))
kropka4IMP = round(((peaksIMP[4]-peaksIMP[3])/2)+(p*3))
kropka5IMP = round(((peaksIMP[4]-peaksIMP[3])/2)+(p*4))

plt.plot(cIMP)
plt.plot(peaksIMP, cIMP[peaksIMP], "*", kropka5IMP, cIMP[kropka5IMP], "x",kropka4IMP, cIMP[kropka4IMP], "x", kropka3IMP,  cIMP[kropka3IMP], "x", kropka2IMP, cIMP[kropka2IMP], "x", kropka1IMP,  cIMP[kropka1IMP], "x")
plt.show()

#Obliczenie THC (1/Z0)
thc = 1/sygnal1808['Z0'][5500:6500]
plt.plot(thc)
plt.show()

plt.figure(figsize=(12,10))
plt.subplot(3, 1, 1)
plt.plot(c8)
plt.plot(peaks8, c8[peaks8], "*", kropka5, c8[kropka5], "x",kropka4, c8[kropka4], "x", kropka3,  c8[kropka3], "x", kropka2, c8[kropka2], "x", kropka1,  c8[kropka1], "x")
plt.title('Sygnał ECG')
plt.subplot(3, 1, 2)
plt.plot(cIMP)
plt.plot(peaksIMP, cIMP[peaksIMP], "*", kropka5IMP, cIMP[kropka5IMP], "x",kropka4IMP, cIMP[kropka4IMP], "x", kropka3IMP,  cIMP[kropka3IMP], "x", kropka2IMP, cIMP[kropka2IMP], "x", kropka1IMP,  cIMP[kropka1IMP], "x")
plt.title('Sygnał IMP')
plt.subplot(3, 1, 3)
plt.plot(thc)
plt.title('THC')
plt.show()

#odejmowanie wartości C od wartości R
sumaIMP = polowa4IMP+polowa3IMP+polowa2IMP+polowa1IMP
sredniaIMP = (sumaIMP/4)*1000

sumaECG = polowa1+polowa2+polowa3+polowa4
sredniaECG = (sumaECG/4)*1000

roznica = sredniaIMP-sredniaECG
print("Roznica w czasie pomiędzy polowkowymi odleglosciami C a R wynosi: ", roznica, "[ms]")

roznicaP1 = peaksIMP[0] - peaks8[1]
roznicaP2 = peaksIMP[1] - peaks8[2]
roznicaP3 = peaksIMP[2] - peaks8[3]
roznicaP4 = peaksIMP[3] - peaks8[4]

roznicaALL = (roznicaP1+roznicaP2+roznicaP3+roznicaP4)/4

print("Srednia roznica w czasie pomiedzy pikiem C a pikiem R: ", roznicaALL, "[ms]")