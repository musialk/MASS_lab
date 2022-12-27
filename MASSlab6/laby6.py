import numpy as np
import pyedflib
import scipy.signal as signal
import matplotlib.pyplot as plt

EEG = pyedflib.EdfReader('n7.edf')
sygnal = EEG.signals_in_file
signal_labels = EEG.getSignalLabels()
#print('Signal labels: ', signal_labels)

sigbufs = np.empty((8,EEG.getNSamples()[0]))
for i in np.arange(8):
    sigbufs[i,:]=EEG.readSignal(i)

freq = EEG.getSampleFrequencies()
print("Czestotliwosc: ", freq)

len = 100
fs = 128
amp = 2*np.sqrt(2)
lead = np.array(sigbufs[1])
time = np.arange(0,len)*1/fs
#print("czas: ", time)

fig,ax=plt.subplots()
ax.plot(time,lead[:len])
ax.grid()
plt.show()

f,t,Zxx=signal.stft(lead, fs, nperseg=100)
plt.pcolormesh(t[:100], f, np.abs(Zxx[:,:100]), vmin=0, vmax=amp, shading='gouraud')
plt.title('STFT')
plt.show()

def fazy_snu(stft):
    gleboki=sen=wybudzony=obudzony=0
    for i in stft:
        for s in i:
            if s <=4:
                gleboki+=1
            elif s>=8:
                sen +=1
            elif s>13:
                wybudzony+=1
            else:
                obudzony+=1
            sum= gleboki + sen + wybudzony + obudzony
            SG=round(gleboki / sum * 100)
            S= round(sen / sum*100)
            W=round(wybudzony / sum*100)
            O=round(obudzony / sum*100)
            return print('Fale theta= ', SG ,"  Fale alfa= ", S,"  Fake beta= ", W,'  Fale gamma=', O )
fazy_snu(Zxx)
