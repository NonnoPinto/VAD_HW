import webrtcvad
"""
vad = webrtcvad.Vad(2)

sample_rate = 16000
frame_duration = 10  # ms
frame = b'\x00\x00' * int(sample_rate * frame_duration / 1000)
print (frame)
print(f'{vad.is_speech(frame, 8000)}')


file = open("Multimedia_HW1_1226024/inputaudio1.data", "rb")
file_content = file.read()
"""

vad = webrtcvad.Vad()

sample_rate = 8000
frame_duration= 20

with open("Multimedia_HW1_1226024/inputaudio1.data", "rb") as f:
    byte = f.read(1)
    while byte != "":
        frame = byte * int(sample_rate * frame_duration / 1000)
        #print (frame)
        print(f'{vad.is_speech(frame, 8000)}', end = " ")
        byte = f.read(1)