from flask import Flask
from flask_socketio import SocketIO
from flask_jwt_extended import JWTManager
from flask_cors import CORS
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = '1234'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False
app.config['JWT_ALGORITHM'] = 'HS256'
app.config['JWT_TOKEN_LOCATION'] = ['headers']
#CORS(app, origins="*")  # Habilita CORS para todas las rutas de la aplicación
socketio = SocketIO(app,cors_allowed_origins='*')
jwt = JWTManager(app)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8000)

