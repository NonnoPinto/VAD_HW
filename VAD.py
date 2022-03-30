"""
Questo programma analizza dei file audio 8 bit PCM
a pacchetti di 160 byte equivalenti a 20 ms (8000 Hz)
e usa la trasformata di Fourier della lbireria Numpy (fft)
per implenetare un algoritmo VAD (Voice Activity Detection)
ed eliminare il rumore di fondo
"""
from numpy import fft, max, abs
import struct

MIN_FREQ = 200
MAX_FREQ = 3600

print("Quale file vuoi importare (basta il numero)?")
index = int(input())

#controlla che sia un possibile file
while (index < 1 or index > 5):
    print ("Hai scritto un numero sbagliato, ritenta")
    index = int(input())
index = str(index)

#array complesso
cplx_arr = []

#crea e apre il file di output
name = "outputaudio"+index+".data"
out = open(name, "wb")

#apre file di input
name = "inputaudio"+index+".data"

with(open(name, "rb")) as f:
    while True:
        #array di lettura
        inp_arr = []
        smpl_arr = []
        mag_arr = []
        #importa 160 byte in un array
        try:
            for i in range (0,160):
                inp_arr.append(f.read(1))
                smpl_arr.append(float(struct.unpack('B', inp_arr[i])[0]))              #la conversione risulta "sporca" perchè la normale conversione avviene da 4 byte
                if smpl_arr[i] > 127: smpl_arr[i] = (256-smpl_arr[i]) * (-1)
        #se gli N byte del file non sono multipli di 160, esce
        except:
            break
        cplx_arr = fft.fft(smpl_arr)
        #cerco il massimo valore e lo confronto con il range vocale
        mag_arr = abs(cplx_arr)
        max_val = max(mag_arr)
        #verifica la presenza del rumore di fondo
        if (max_val < MIN_FREQ or max_val > MAX_FREQ):  #rumore presente
            for i in range (0, 160):
                out.write(b'\x00')
        else:                                           #rumore assente
            for i in inp_arr:
                out.write(i)
