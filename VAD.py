import webrtcvad

vad = webrtcvad.Vad(3)

sample_rate = 8000
frame_duration= 20

o = open("outputVAD1.data", "wb")

with open("inputaudio1.data", "rb") as f:
    byte = f.read(1)
    while byte != b'':
        frame = byte * int(sample_rate * frame_duration / 1000)
        if (vad.is_speech(frame, 8000)):
            o.write(byte)
        else:
            o.write(b'\x00\x00')
        byte = f.read(1)
