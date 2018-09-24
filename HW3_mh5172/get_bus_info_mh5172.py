import requests
import json
import pandas as pd
import sys
url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + sys.argv[1] +'&VehicleMonitoringDetailLevel=calls&LineRef='+ sys.argv[2]
data = requests.get(url)
text = json.loads(data.text)
siri_read = text['Siri']
ServiceDelivery_read = siri_read['ServiceDelivery']
VehicleMonitoringDelivery_read = ServiceDelivery_read['VehicleMonitoringDelivery']
VehicleActivity_read = VehicleMonitoringDelivery_read[0]['VehicleActivity']
num = len(VehicleActivity_read)
LNG = []
LAT = []
for i in range(num):
    location = VehicleActivity_read[i]['MonitoredVehicleJourney']['VehicleLocation']
    LNG.append(location['Longitude'])
    LAT.append(location['Latitude'])
MonitoredVehicleJourney_read = VehicleActivity_read[0]['MonitoredVehicleJourney']
OnwardCalls_read = MonitoredVehicleJourney_read['OnwardCalls']
Onwardcall_read = OnwardCalls_read['OnwardCall']
stop_name = Onwardcall_read[0]['StopPointName']
status = Onwardcall_read[0]['Extensions']['Distances']['PresentableDistance']
STOP_NAME = []
STATUS = []
for j in range(num):
    MonitoredVehicleJourney_read = VehicleActivity_read[j]['MonitoredVehicleJourney']
    OnwardCalls_read = MonitoredVehicleJourney_read['OnwardCalls']
    Onwardcall_read = OnwardCalls_read['OnwardCall']
    if Onwardcall_read is None:
        stop_name == 'N/A'
        status == 'N/A'
    else:
        stop_name = Onwardcall_read[0]['StopPointName']
        status = Onwardcall_read[0]['Extensions']['Distances']['PresentableDistance']
    STOP_NAME.append(Onwardcall_read[0]['StopPointName'])
    STATUS.append(Onwardcall_read[0]['Extensions']['Distances']['PresentableDistance'])
file = pd.DataFrame({'Latitude':LAT,'Longitude':LNG,'Stop_Name':STOP_NAME,'Status':STATUS})
file.to_csv('%s.csv'%(sys.argv[2]),sep = ',')