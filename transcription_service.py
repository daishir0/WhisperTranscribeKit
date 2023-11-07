import openai
import os
import subprocess
from datetime import datetime

openai.api_key = 'OPENAI-API-KEY'

def convert_to_wav(input_file_path, output_format="wav"):
    # 出力ファイルパスを決定
    output_file_path = input_file_path.replace(".aac", f".{output_format}")
    # FFmpegを使用してフォーマット変換を実行
    command = ["ffmpeg", "-i", input_file_path, output_file_path]
    subprocess.run(command, check=True)
    # 新しいファイルパスを返す
    return output_file_path

def save_temporary_file(audio_file_stream, format="aac"): # AAC形式をデフォルトとして受け付けます。
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

def transcribe(audio_file_stream):
    # AACファイルを一時的に保存
    file_path = save_temporary_file(audio_file_stream)
    # AACをWAVに変換
    wav_file_path = convert_to_wav(file_path)
    
    # OpenAI APIでテキストに変換
    with open(wav_file_path, "rb") as audio_file:
        response = openai.Audio.transcribe(model="whisper-1", file=audio_file)
    
    # 一時ファイルを削除
    os.remove(file_path)
    os.remove(wav_file_path)
    
    # 結果を保存
    save_transcription(response['text'])
    return response['text']
