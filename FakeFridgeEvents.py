from simple_salesforce import Salesforce

import time
import random


sf = Salesforce(username='dscruggs@iotexplorer17.mds', password='S@lesforce1', security_token='heGCIBkTBgjEf4vtpnL3WdwKs')
print(sf);


def read_temp():
        temp_c = 30.0 + (25*random.random()) 
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c
		
while True:
	print(read_temp())
	data = [{'serial_no__c': '1001','door_open__c': 'false','temp__c':read_temp()}]	
	print("Data sent: ")
	for x in data:  print("data item: ", x) 
	sf.Refrigerator_Event__e.create(data[0])
	time.sleep(5)
	print("Platform Event Sent: " )


