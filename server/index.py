from flask import Flask
import flask
from flask_cors import CORS

from lidar import Lidar

app = Flask(__name__)

lidar = Lidar()
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/": {"origins": "http://localhost:3000/"}})

@app.route('/start_lidar')
def startLidar():
    lidar.startLidarThread()
    response = flask.jsonify({'data': ''})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/stop_lidar')
def stopLidar():
    lidar.stopLidarThread()
    response = flask.jsonify({'data': ''})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_lidar_data')
def getLidarData():
    response = flask.jsonify({'data': lidar.getData()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

app.run(host='127.0.0.1', port='3001')





