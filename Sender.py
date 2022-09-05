import csv
import random
from pathlib import Path

PARAMETER1_MIN = 0
PARAMETER1_MAX = 45
PARAMETER2_MIN = 20
PARAMETER2_MAX = 80
Sensor_ReadingCount = 50
Parameter_name =  ['Temperature' , 'SOC']

def CheckifFileExists(filename):
    path = Path(filename)
    return True if path.is_file() else False

def WriteSensorReadings(file = 'SensorReadings.csv'):
    with open(file, mode='w',newline='') as SensorInput:
        SensorInput = csv.writer(SensorInput, delimiter=',')
        SensorInput.writerow(Parameter_name)
        for item in range(0,Sensor_ReadingCount):
            item = [random.randint(PARAMETER1_MIN,PARAMETER1_MAX), random.randint(PARAMETER2_MIN,PARAMETER2_MAX)]
            SensorInput.writerow(item)

def ReadSensorReadings(file = 'SensorReadings.csv'):
    if CheckifFileExists(file):
        BatteryParameter1_Values = []
        BatteryParameter2_Values = []
        with open(file, mode='r') as csv_file:
            SensorReadings = csv.reader(csv_file, delimiter=',')
            BatteryParameters = next(SensorReadings) 
            print(f'{", ".join(BatteryParameters)}')
            for Readings in SensorReadings:
                print(f'{Readings[0]},{Readings[1]}')
                BatteryParameter1_Values.append(Readings[0])
                BatteryParameter2_Values.append(Readings[1])
            return BatteryParameters,BatteryParameter1_Values, BatteryParameter2_Values
    else :
        return None

#file = 'SensorReadings.csv'
#WriteSensorInput(file)
#ReadSensorReadings(file)



















