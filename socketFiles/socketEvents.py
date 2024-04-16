from app import socketio
from flask_jwt_extended import jwt_required, get_jwt_identity
import json

@socketio.on('connect')
@jwt_required()
def handle_connect():
    sender = get_jwt_identity()
    print(f'Client connected: {sender}')

@socketio.on('disconnect')
@jwt_required()
def handle_disconnect():
    sender = get_jwt_identity()
    print(f'Client disconnected: {sender}')


@socketio.on("reciveHeartApi")#en la de corazon  no se da 
@jwt_required()
def reciveDateHeart(data):
    datoPlus = data
    print(datoPlus)
    #Estos datos se enviaran al front para los datos del corazon
    socketio.emit("sendFrontHeart",json.dumps(datoPlus))



@socketio.on("notifyStartTemp")
@jwt_required()
def notifyTemp(data):  # Agregar un parámetro para recibir datos del evento
    try:
        datoPlus = {"key": 1}
        # Esto se enviará a la API de julian para que avise al ESP32 para tomar la temperatura
        print(datoPlus)
        socketio.emit("sendApiTemp", json.dumps(datoPlus))
    except Exception as e:
        print(f"Error al emitir evento sendApiTemp: {e}")


@socketio.on("reciveTempApi")
@jwt_required()
def reciveDateTemperature(data):
    datoPlus = data
   
    socketio.emit("sendTempFront",json.dumps(datoPlus))
    

