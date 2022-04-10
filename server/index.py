from flask import Flask

from lidar import Lidar

app = Flask(__name__)

lidar = Lidar()

@app.route('/start_lidar')
def startLidar():
    lidar.startLidarThread()
    return ''

@app.route('/stop_lidar')
def stopLidar():
    lidar.stopLidarThread()
    return ''

@app.route('/get_lidar_data')
def getLidarData():
    return ', '.join(str(e) for e in lidar.getData())

app.run(host='127.0.0.1', port='3001')





