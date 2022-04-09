import os
from math import floor
from adafruit_rplidar import RPLidar
import threading
import time

class Lidar:
    stopLidar = False
    max_distance = 0
    scan_data = [0]*360

    def __init__(self):
        self.lidarThr = threading.Thread(target=self.startLidarFn)
        self.lidar = RPLidar(None, 'COM5', timeout=3)


    def startLidarFn(self):
        for scan in self.lidar.iter_scans():
            for (_, angle, distance) in scan:
                self.scan_data[min([359, floor(angle)])] = distance
            if self.stopLidar: return

    def _stopLidarFn(self):
        self.lidar.stop()
        self.lidar.stop_motor()
        self.lidar.disconnect()

    def startLidarThread(self):
        self.lidarThr.start()

    def stopLidarThread(self):
        self.stopLidar = True
        time.sleep(2)
        self._stopLidarFn()

    def getLidarData(self):
        print(self.scan_data)
    
lidar = Lidar()
lidar.startLidarThread()
time.sleep(2)
lidar.getLidarData()
lidar.stopLidarThread()