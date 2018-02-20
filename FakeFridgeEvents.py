from simple_salesforce import Salesforce
from dotenv import load_dotenv

import os
import time
import random

BASE_DIR='./'

load_dotenv(os.path.join(BASE_DIR, '.env.iotxporg'))
USERNAME=os.getenv('USERNAME')
PASSWORD=os.getenv('PASSWORD')
SECURITY_TOKEN=os.getenv('SECURITY_TOKEN')

print("uname %s pw %s token %s" % (USERNAME, PASSWORD, SECURITY_TOKEN))

sf = Salesforce(username=USERNAME, password=PASSWORD, security_token=SECURITY_TOKEN)
print(sf);


def read_temp():
        temp_c = 27.0 + (25*random.random()) 
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c
		
while True:
	print(read_temp())
	data = [{'serial_no__c': '1001','door_open__c': 'false','temp__c':read_temp()}]	
	print("Data sent: ")
	for x in data:  print("data item: ", x) 
	sf.Refrigerator_Event__e.create(data[0])
	time.sleep(15)
	print("Platform Event Sent: " )


