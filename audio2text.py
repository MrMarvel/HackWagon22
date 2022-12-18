
from vosk import Model, KaldiRecognizer, SetLogLevel
from pydub import AudioSegment
import subprocess
import json
import os
import ffmpeg


def get_text(filename):
    SetLogLevel(0)

    #Проверка наличия модели
    if not os.path.exists("model"):
        exit(1)

    # Устанавливаем Frame Rate
    FRAME_RATE = 44100
    #FRAME_RATE = 8000
    CHANNELS = 1
    model = Model("model")
    rec = KaldiRecognizer(model, FRAME_RATE)
    rec.SetWords(True)
    #С помозью библиотеки pydub делается предобработка аудио
    wav = AudioSegment.from_wav('train.wav')
    wav = wav.set_channels(CHANNELS)
    wav = wav.set_frame_rate(FRAME_RATE)

    # Преобразование вывода в json
    rec.AcceptWaveform(wav.raw_data)
    result = rec.Result()
    text = json.loads(result)["text"]

    # Записываем результат в файл "data.txt"
    with open('data.txt', 'w') as f:
        json.dump(text, f, ensure_ascii=False, indent=4)