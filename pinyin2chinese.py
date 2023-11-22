# _*_ coding : utf-8 _*_
# @Time : 2023/9/16 11:01
# @Author : Origami
# @File : pinyin2chinese
# @Project : TestSpeechRecognition
from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag


def p2c(arr):
    dagparams = DefaultDagParams()
    result = dag(dagparams, arr, path_num=1, log=False)
    res = ''
    for item in result:
        res = ''.join(item.path)
    return res