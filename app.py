# _*_ coding : utf-8 _*_
# @Time : 2023/9/16 11:07
# @Author : Origami
# @File : app
# @Project : TestSpeechRecognition
import os

from grpc_test import wav2hanzi
from pinyin2chinese import p2c

from get_wav import recoder

# r = recoder()
# r.recoder()
# r.savewav("test1.wav")
pinyin_arr = wav2hanzi()

# for i in range(len(pinyin_arr)):
#     pinyin_arr[i] = pinyin_arr[i][:-1]
#
# res = p2c(pinyin_arr)
# print(res)
