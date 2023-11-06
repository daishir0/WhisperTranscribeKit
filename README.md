# WhisperTranscribeKit

## Overview
WhisperTranscribeKit is a real-time audio transcription service leveraging OpenAI's Whisper model. It provides a web interface for recording audio and displays transcriptions live as they are processed.

## Installation
- Clone the repository: `git clone <repository-url>`
- Install the required Python packages: `pip install -r requirements.txt`
- Make sure `ffmpeg` is installed on your system for audio processing. On Ubuntu, you can install it with `sudo apt-get install ffmpeg`.

## Usage
- Start the Flask server with `python app.py`.
- Open your web browser and navigate to `http://localhost:5000/`.
- Use the provided buttons to start and stop audio recordings and view transcriptions in real-time.

## Notes
- An OpenAI API key is required to interact with the Whisper model.
- Ensure you have set the correct server address in the `index.html` socket connection setup.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

# WhisperTranscribeKit

## 概要
WhisperTranscribeKitは、OpenAIのWhisperモデルを利用したリアルタイム音声転写サービスです。録音したオーディオのリアルタイムでの転写をウェブインターフェースで表示します。

## インストール方法
- リポジトリをクローンします: `git clone <repository-url>`
- 必要なPythonパッケージをインストールします: `pip install -r requirements.txt`
- 音声処理のためにシステムに`ffmpeg`がインストールされていることを確認してください。Ubuntuでは、`sudo apt-get install ffmpeg`でインストールできます。

## 使い方
- `python app.py`でFlaskサーバーを起動します。
- ウェブブラウザを開き、`http://localhost:5000/`にアクセスします。
- 録音の開始と停止を行うボタンを使用し、リアルタイムで転写を表示します。

## 注意点
- Whisperモデルと対話するためにはOpenAI APIキーが必要です。
- `index.html`のソケット接続設定に正しいサーバーアドレスを設定してください。

## ライセンス
このプロジェクトはMITライセンスの下でライセンスされています。詳細はLICENSEファイルを参照してください。
