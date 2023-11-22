# _*_ coding : utf-8 _*_
# @Time : 2023/9/10 15:39
# @Author : Origami
# @File : wave
# @Project : TestSpeechRecognition
import wave

f = wave.open("test1.wav", "wb")
f.setframerate(16000)
f.setnchannels(1)
f.setsampwidth(2)
f.close()
