import eventlet
from flask_socketio import SocketIO

socketio = SocketIO()


def init_app(app):

    socketio.init_app(app)

    if __name__ == '__main__':
        socketio.run(app, host='127.0.0.1',
                     port=8000,
                     use_reloader=True,
                     debug=True)

        