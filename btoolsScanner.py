import time
import math

from beacontools import BeaconScanner, IBeaconFilter

def calcDistanceBT(rssi, tx_power):
     if rssi == 0:
          return -1.0
     ratio = rssi*1.0/tx_power
     if ratio < 1.0 : 
          return math.pow(ratio,10)
     else: 
          accuracy = (0.89976)*math.pow(ratio,7.7095) + 0.111
          return accuracy

def callback(bt_addr, rssi, packet, additional_info):
    distance = calcDistanceBT(rssi, packet.tx_power)
    print("distance = %d" % distance)
    print("<%s, %d> %s %s" % (bt_addr, rssi, packet, additional_info))

# scan for all iBeacon advertisements from beacons with the specified uuid
# scanner = BeaconScanner(callback,
#     device_filter=IBeaconFilter(uuid="2f234454-cf6d-4a0f-adf2-f4911ba9ffa6")
# )
scanner = BeaconScanner(callback) 

scanner.start()
time.sleep(5)
scanner.stop()
