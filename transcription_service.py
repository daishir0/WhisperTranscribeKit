import openai
import os
from pydub import AudioSegment
import soundfile as sf
from datetime import datetime

openai.api_key = 'OPENAI-API-KEY'


def transcribe(audio_file_stream):
    # 一時ファイルに保存
    file_path = save_temporary_file(audio_file_stream)
    # OpenAI APIでテキストに変換
    with open(file_path, "rb") as audio_file:
        response = openai.Audio.transcribe(model="whisper-1", file=audio_file)
    # 一時ファイルを削除
    os.remove(file_path)
    # 結果を保存
    save_transcription(response['text'])
    return response['text']

def save_temporary_file(audio_file_stream, format="wav"):
    # 現在の日時をファイル名に使用
    current_time = datetime.now().strftime("%Y%m%d-%H%M%S")
    temp_file = f"./data/temp_audio_file_{current_time}." + format
    audio_file_stream.save(temp_file)
    return temp_file

def save_transcription(text):
    # 現在の日時をファイル名に使用
    current_time = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"./data/{current_time}.txt"
    # テキストファイルとして保存
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    print(f"Transcription saved to {filename}")
