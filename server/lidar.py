import os
from math import floor
from adafruit_rplidar import RPLidar
import threading
import time

class Lidar:
    stopLidar = False
    max_distance = 0
    scan_data = [0]*360
    lidar = RPLidar(None, 'COM5')
    lidar.stop_motor()
    thrStarted = False

    def __init__(self):
        self.lidarThr = threading.Thread(target=self.startLidarFn)

    def startLidarFn(self):
        for scan in self.lidar.iter_scans():
            for (_, angle, distance) in scan:
                self.scan_data[min([359, floor(angle)])] = distance
            if self.stopLidar: return

    def _stopLidarFn(self):
        self.lidar.stop()
        self.lidar.stop_motor()

    def startLidarThread(self):
        self.lidar.start_motor()
        time.sleep(3)
        if (self.thrStarted == False):
            self.lidarThr.start()
            self.thrStarted = True

    def stopLidarThread(self):
        self.stopLidar = True
        time.sleep(2)
        self._stopLidarFn()

    def getData(self):
        return self.scan_data
    