from flask import Flask, request, jsonify
from flask_socketio import SocketIO
import transcription_service
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 全ルートでCORSを有効化
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/hc')
def hc():
    return app.send_static_file('hc.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        audio_file = request.files['audio_data']
        if audio_file:
            text = transcription_service.transcribe(audio_file)
            if text:
                socketio.emit('transcription', {'text': text})
                return jsonify({"message": "File transcribed successfully"}), 200
            else:
                return jsonify({"message": "Transcription failed"}), 400
        else:
            return jsonify({"message": "No file found"}), 400

if __name__ == '__main__':
    if not os.path.exists("./data"):
        os.makedirs("./data")
    socketio.run(app, debug=True, host="0.0.0.0")
