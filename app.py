import os
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Message: {msg}")
    send(msg, broadcast=True)  # send message to everyone

if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    socketio.run(app,host='0.0.0.0',port=port)
      