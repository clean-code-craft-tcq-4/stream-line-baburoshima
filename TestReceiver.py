import unittest
from unittest.mock import patch, call
import Receiver
from Receiver import check_invalid_value, get_data_from_input_stream, get_max_min_value, print_max_min, get_simple_moving_average, print_simple_moving_average, main_func 

class TestReceiver(unittest.TestCase):

    #Test check_invalid_value with InvalidRange
    def test_check_invalid_value_with_InvalidRange(self):
        input_list = ["34","43","InvalidRange","55","InvalidRange"]
        expected_list = ["34","43","55"]
        actual_list = check_invalid_value(input_list)
        self.assertEqual(actual_list,expected_list)

    #Test check_invalid_value without InvalidRange
    def test_check_invalid_value_without_InvalidRange(self):
        input_list = ["34","43","55"]
        expected_list = ["34","43","55"]
        actual_list = check_invalid_value(input_list)
        self.assertEqual(actual_list,expected_list)
    
    #Test get_data_from_input_stream with valid values
    def test_get_data_with_valid_values(self):
        input_stream = ['Temperature, SOC\n', '37,21\n', '20,31\n', '45,50\n', '40,30\n', '35,50\n'] 
        sensor1,sensor1_values,sensor2,sensor2_values = get_data_from_input_stream(input_stream)
        self.assertEqual(sensor1,"Temperature")
        self.assertEqual(sensor1_values,[37,20,45,40,35])
        self.assertEqual(sensor2,"SOC")
        self.assertEqual(sensor2_values,[21,31,50,30,50])

    #Test get_data_from_input_stream with invalid values
    def test_get_data_with_invalid_values(self):
        input_stream = ['Temperature, SOC\n', '37,21\n', 'Invalid Range,78\n', '20,31\n', '45,Invalid Range\n', '40,30\n', '35,50\n'] 
        sensor1,sensor1_values,sensor2,sensor2_values = get_data_from_input_stream(input_stream)
        self.assertEqual(sensor1,"Temperature")
        self.assertEqual(sensor1_values,[37,20,45,40,35])
        self.assertEqual(sensor2,"SOC")
        self.assertEqual(sensor2_values,[21,78,31,30,50])

    #Test get_max_min_value list with values
    def test_get_max_min_list_values(self):
        min_val,max_val = get_max_min_value([12,23,52,22])
        self.assertEqual(min_val,12)
        self.assertEqual(max_val,52)

    #Test get_max_min_value with empty list
    def test_get_max_min_empty_list(self):
        min_val,max_val = get_max_min_value([])
        self.assertEqual(min_val,None)
        self.assertEqual(max_val,None)

    #Test print_max_min list with values
    #Mocking print function
    @patch('builtins.print')
    def test_print_max_min(self,mock_print):
        print_max_min("Temperature",[12,22,32,42,2],"SOC",[10,20,25,30,35])
        self.assertEqual(mock_print.mock_calls,[call("Min value of Temperature is 2"),
                                                call("Max value of Temperature is 42"),
                                                call("Min value of SOC is 10"),
                                                call("Max value of SOC is 35")])

    #Test print_max_min empty list of temperature and SOC
    #Mocking print function
    @patch('builtins.print')
    def test_print_max_min_both_empty_list(self,mock_print):
        print_max_min("Temperature",[],"SOC",[])
        self.assertEqual(mock_print.mock_calls,[call("Temperature value list is empty"),
                                                call("SOC value list is empty")])

    #Test print_max_min empty list of only temperature
    #Mocking print function
    @patch('builtins.print')
    def test_print_max_min_temp_empty_list(self,mock_print):
        print_max_min("Temperature",[],"SOC",[20,30,35])
        self.assertEqual(mock_print.mock_calls,[call("Temperature value list is empty"),
                                                call("Min value of SOC is 20"),
                                                call("Max value of SOC is 35")])

    #Test print_max_min empty list of only SOC
    #Mocking print function
    @patch('builtins.print')
    def test_print_max_min_soc_empty_list(self,mock_print):
        print_max_min("Temperature",[20,40,30],"SOC",[])
        self.assertEqual(mock_print.mock_calls,[call("Min value of Temperature is 20"),
                                                call("Max value of Temperature is 40"),
                                                call("SOC value list is empty")])


    #Test get_simple_moving_average with value_list = COUNT_FOR_SMA
    def test_get_sma_list_equal_count(self):
        self.assertEqual(get_simple_moving_average([2,3,5,6,8]),4.8)

    #Test get_simple_moving_average with value_list < COUNT_FOR_SMA
    def test_get_sma_list_lessthan_count(self):
        self.assertEqual(get_simple_moving_average([]),None)

    #Test get_simple_moving_average with value_list > COUNT_FOR_SMA
    def test_get_sma_list_greaterthan_count(self):
        self.assertEqual(get_simple_moving_average([2,3,5,6,8,9]),6.2)

    #Test print_simple_moving_average with valid list
    #Mocking print function
    @patch('builtins.print')
    def test_print_sma_valid_list(self,mock_print):
        print_simple_moving_average("Temperature",[11,12,22,32,42,2],"SOC",[11,10,20,25,30,35])
        self.assertEqual(mock_print.mock_calls,[call("Simple Moving Average of last 5 values of Temperature is 22.0"),
                                                call("Simple Moving Average of last 5 values of SOC is 24.0")])

    #Test print_simple_moving_average list with values = COUNT_FOR_SMA
    #Mocking print function
    @patch('builtins.print')
    def test_print_sma_list_equal_count(self,mock_print):
        print_simple_moving_average("Temperature",[12,22,32,42,2],"SOC",[10,20,25,30,35])
        self.assertEqual(mock_print.mock_calls,[call("Simple Moving Average of last 5 values of Temperature is 22.0"),
                                                call("Simple Moving Average of last 5 values of SOC is 24.0")])

    #Test print_simple_moving_average both list with values < COUNT_FOR_SMA
    #Mocking print function
    @patch('builtins.print')
    def test_print_sma_list_less_count(self,mock_print):
        print_simple_moving_average("Temperature",[22,32,42,2],"SOC",[20,25,30,35])
        self.assertEqual(mock_print.mock_calls,[call("Number of values in Temperature list is less than 5"),
                                                call("Number of values in SOC list is less than 5")])

    #Test print_simple_moving_average only temperature list with values < COUNT_FOR_SMA
    #Mocking print function
    @patch('builtins.print')
    def test_print_sma_templist_less_count(self,mock_print):
        print_simple_moving_average("Temperature",[22,32,42,2],"SOC",[10,20,25,30,35])
        self.assertEqual(mock_print.mock_calls,[call("Number of values in Temperature list is less than 5"),
                                                call("Simple Moving Average of last 5 values of SOC is 24.0")])

    #Test print_simple_moving_average only SOC list with values < COUNT_FOR_SMA
    #Mocking print function
    @patch('builtins.print')
    def test_print_sma_soclist_less_count(self,mock_print):
        print_simple_moving_average("Temperature",[12,22,32,42,2],"SOC",[20,25,30,35])
        self.assertEqual(mock_print.mock_calls,[call("Simple Moving Average of last 5 values of Temperature is 22.0"),
                                                call("Number of values in SOC list is less than 5")])
                                                
    #Test main_func with no values
    #Mocking print function
    @patch('builtins.print')
    def test_main_func_no_values(self,mock_print):
        main_func("")
        mock_print.assert_called_with("Input stream empty")

    
    #Test main_func with valid values
    @patch('Receiver.get_data_from_input_stream',return_value = ["Temepature",[37,5,20,45,40,35],"SOC",[21,78,31,50,30,50]])
    @patch('Receiver.print_max_min')
    @patch('Receiver.print_simple_moving_average')
    def test_main_func_with_values(self,mock_print_simple_moving_average,mock_print_max_min,mock_get_data_from_input_stream):
        input_stream = "Temperature, SOC\n37,21\n5,78\n20,31\n45,50\n40,30\n35,50"
        main_func(input_stream)
        self.assertEqual(mock_get_data_from_input_stream.call_count,1)
        self.assertEqual(mock_print_max_min.call_count,1)
        self.assertEqual(mock_print_simple_moving_average.call_count,1)
     
if __name__ == '__main__':
    unittest.main()
