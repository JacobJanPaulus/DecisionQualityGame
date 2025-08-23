# Import required python modules
from flask import Flask
from flask_socketio import SocketIO
from routes import routes
from sockets import register_socket_handlers
from decision_problems import load_decision_problems

# Define the python app
app = Flask(__name__)
socketio = SocketIO(app)

# Load the decision problems when starting the application
load_decision_problems()

# Register the routes (URLs) for the app
app.register_blueprint(routes)

# Register the socket handlers
register_socket_handlers(socketio)

if __name__ == '__main__':
    socketio.run(app, debug=True)
