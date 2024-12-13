
from flask import Flask, render_template
from flask_socketio import SocketIO,send, emit

app = Flask(__name__,template_folder='templates')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,cors_allowed_origins="*")

@app.route('/',methods=['GET'])
def index():
    return render_template("index.html")
    # return "hello world"

@socketio.on('connect')
def test_connect():
    send('welcome')

@socketio.on('send_message')
def handle_message(message):
    print(message)
    emit('receive_message', message, broadcast=True)

    # send(message, broadcast=True)




if __name__ == "__main__":
    socketio.run(app,allow_unsafe_werkzeug=True)
