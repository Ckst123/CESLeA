from flask import Flask, request, jsonify
import os
from message import create_msg

IPC_FIFO_NAME = 'ipc'
fifo = os.open(IPC_FIFO_NAME, os.O_CREAT | os.O_RDWR)

app = Flask(__name__)
speaker_dict = {}
reverse_speaker_dict = {}


def write_message(msg):
    msg = msg.encode('utf8')
    msg = create_msg(msg)
    os.write(fifo, msg)


@app.route('/tts', methods=['POST'])
def tts():
    if request.method == 'POST':
        text = request.form['text']
        if len(text) == 0:
            return 'no text'
        print(text)
        write_message('tts\t' + text)
        return 'OK'
    else:
        return '잘못된 접근입니다.'


@app.route("/stt", methods=['POST'])
def stt():
    text = request.form['text']
    print(text)
    write_message('stt\t' + text)
    return "200 OK"


@app.route("/spk", methods=['POST'])
def spk():
    text = request.form['text']
    print(text)
    write_message('spk\t' + text)
    return "200 OK"


@app.route("/env", methods=['POST'])
def env():
    text = request.form['text']
    print(text)
    write_message('env\t' + text)
    return "200 OK"


def run_app():
    app.run(host='0.0.0.0', port='8080', debug=True)


if __name__ == "__main__":
    run_app()
