import unittest
from Sender import *

class BMS_Sender(unittest.TestCase):
  def test_readcsv(self):
    self.assertTrue(ReadSensorInput()[0]=="Temperature, SOC")

unittest.main()