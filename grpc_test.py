# _*_ coding : utf-8 _*_
# @Time : 2023/9/16 10:14
# @Author : Origami
# @File : grpc_test
# @Project : TestSpeechRecognition
import asrt_sdk

stream_asr_text = ""
stream_buffer_text = ""


def wav2hanzi():
    HOST = '127.0.0.1'
    PORT = '20002'
    PROTOCOL = 'grpc'
    speech_recognizer = asrt_sdk.get_speech_recognizer(HOST, PORT, PROTOCOL)
    FILENAME = 'test1.wav'
    result = speech_recognizer.recognite_file(FILENAME)
    # print("wav文件识别结果:", result)

    wave_data = asrt_sdk.read_wav_datas(FILENAME)
    result = speech_recognizer.recognite_speech(wave_data.str_data,
                                                wave_data.sample_rate,
                                                wave_data.channels,
                                                wave_data.byte_width)
    # print("wav声学识别响应:", result)
    # print("wav声学识别结果:", result.result_data)
    pinyin_arr = result.result_data

    result = speech_recognizer.recognite_language(result.result_data)

    # print("语言模型识别响应:", result)
    print("语言模型识别结果:", result.text_result)

    # result = speech_recognizer.recognite(wave_data.str_data,
    #                                      wave_data.sample_rate,
    #                                      wave_data.channels,
    #                                      wave_data.byte_width)
    #
    # print("wav完整识别响应:", result)
    # print("wav完整识别结果:", result.text_result)

    def make_wav_generator():
        for _ in range(2):
            yield wave_data.str_data, wave_data.sample_rate, wave_data.channels, wave_data.byte_width

    def callback_func(ret):
        global stream_asr_text
        global stream_buffer_text
        # print("流式识别响应：", ret)
        # print("流式识别结果：", ret.status_code, ret.text_result)
        if ret.status_code == 200000:
            stream_asr_text += ret.text_result
            stream_buffer_text = ""
        elif ret.status_code == 206000:
            stream_buffer_text = ret.text_result
        else:
            print("流式语音识别出错！", ret.status_code, ret.status_message)

        # print("当前语音识别内容:", stream_asr_text + stream_buffer_text)

    speech_recognizer.recognite_stream(make_wav_generator, 1, callback_func)
    return pinyin_arr


wav2hanzi()
