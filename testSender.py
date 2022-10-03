import unittest
from Sender import *
import csv 
from pathlib import Path

InvalidRange_file = 'InvalidRange.csv'
rowsInvalid = [['Temperature','SOC'],['46','52'],['27','81']]
generated_file = 'Generated.csv'

class BMS_Sender(unittest.TestCase):
  def test_Writecsv(self):
      WriteSensorReadings('SensorReadings.csv')
      self.assertTrue(CheckifFileExists('SensorReadings.csv')==True)

  def test_IfFileExists(self):    
     self.assertTrue(CheckifFileExists('NonExisting.csv')==False)
     with open(generated_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerows( ['Value1','Value2'])
     self.assertTrue(CheckifFileExists(generated_file)==True)
     Path(generated_file).unlink()

  def test_readcsv(self):
      self.assertTrue(ReadSensorReadings('SensorReadings.csv')[0]==['Temperature', 'SOC'])
      self.assertTrue(0 <= int(ReadSensorReadings('SensorReadings.csv')[1][0]) <= 45)
      self.assertTrue(20 <= int(ReadSensorReadings('SensorReadings.csv')[2][1])<= 80)
      self.assertTrue(ReadSensorReadings('SensorReadings.csv')[3],50)

  def test_InvalidRanges(self):
      with open(InvalidRange_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerows(rowsInvalid)
      self.assertTrue(ReadSensorReadings(InvalidRange_file)[0]==['Temperature', 'SOC'])
      self.assertFalse(0 <= int(ReadSensorReadings(InvalidRange_file)[1][0]) <= 45)
      self.assertFalse(20 <= int(ReadSensorReadings(InvalidRange_file)[2][1]) <= 80)
      self.assertTrue(0 <= int(ReadSensorReadings(InvalidRange_file)[1][1]) <= 45)
      self.assertTrue(20 <= int(ReadSensorReadings(InvalidRange_file)[2][0])<= 80)
      Path(InvalidRange_file).unlink()

  def test_NonExistingcsv(self):
      self.assertIsNone(ReadSensorReadings('NonExisting.csv'))

unittest.main()