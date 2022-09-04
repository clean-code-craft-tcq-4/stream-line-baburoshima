import csv
import random

def WriteSensorInput():
    with open('SensorInput.csv', mode='w',newline='') as SensorInput:
        SensorInput = csv.writer(SensorInput, delimiter=',')
        SensorInput.writerow(['Temperature' , 'SOC'])
        for item in range(0,50):
            item = [random.randint(0,45), random.randint(20,80)]
            SensorInput.writerow(item)

def ReadSensorInput():
    WriteSensorInput()
    with open('SensorInput.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        BatteryParameters = []
        BatteryParamtersValues = []
        for row in csv_reader:
            if line_count == 0:
                BatteryParameters = f'{", ".join(row)}'
                print(BatteryParameters)
                line_count += 1
            else:
                BatteryParamtersValues = f'{row[0]},{row[1]}'
                print(BatteryParamtersValues)
                line_count += 1
    return BatteryParameters,BatteryParamtersValues




















