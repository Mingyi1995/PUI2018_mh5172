import requests
import json
import sys
url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + sys.argv[1] +'&VehicleMonitoringDetailLevel=calls&LineRef='+ sys.argv[2]
if not len(sys.argv) == 3:
	print ('wrong input')
else:
	data = requests.get(url)
	text = json.loads(data.text)
	siri_read = text['Siri']
	ServiceDelivery_read = siri_read['ServiceDelivery']
	VehicleMonitoringDelivery_read = ServiceDelivery_read['VehicleMonitoringDelivery']
	if 'ErrorCondition' in VehicleMonitoringDelivery_read[0]:
		if 'API key is not authorized' in VehicleMonitoringDelivery_read[0]['ErrorCondition']['OtherError']['ErrorText']:
			print ('API key is not authorized')
		elif 'No such route' in VehicleMonitoringDelivery_read[0]['ErrorCondition']['OtherError']['ErrorText']:
			print ('No such route')
	else:
		VehicleActivity_read = VehicleMonitoringDelivery_read[0]['VehicleActivity']
		print('Bus Line:',sys.argv[2])
		num = len(VehicleActivity_read)
		for i in range(num):
			location = VehicleActivity_read[i]['MonitoredVehicleJourney']['VehicleLocation']
			longitude = location['Longitude']
			latitude = location['Latitude']
			print('Bus',i,'is at latitude',latitude,'and longitude',longitude)