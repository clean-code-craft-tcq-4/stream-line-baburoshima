import sys

COUNT_FOR_SMA = 5

def remove_invalid_value(value_list):
    value_list = [value for value in value_list if value != 'InvalidRange']
    return value_list

def get_valid_data(value_list):
    par = value_list[0]
    value_list.pop(0)
    value_list = remove_invalid_value(value_list)
    value_list = [int(value) for value in value_list]
    return par, value_list
    
def get_data_from_input_stream(input_stream):
    sensor1_value_list = []
    sensor2_value_list = []

    for reading in input_stream:
        reading = reading.strip("\n").replace(" ","").split(",")
        sensor1_value_list.append(reading[0])
        sensor2_value_list.append(reading[1])
            
    sensor1_parameter, sensor1_value_list = get_valid_data(sensor1_value_list)
    sensor2_parameter, sensor2_value_list = get_valid_data(sensor2_value_list)                
    return sensor1_parameter,sensor1_value_list,sensor2_parameter,sensor2_value_list

def get_max_min_value(value_list):
    if value_list != []:
        return min(value_list),max(value_list)
    else:
        return None,None

def print_max_min(sensor1,sensor1_values,sensor2,sensor2_values):
    sensor1_min, sensor1_max = get_max_min_value(sensor1_values)
    sensor2_min, sensor2_max = get_max_min_value(sensor2_values)
    if sensor1_min != None:
        print("Min value of " + sensor1 + " is " + str(sensor1_min))
        print("Max value of " + sensor1 + " is " + str(sensor1_max))
    else:
        print(sensor1 + " value list is empty")
    if sensor2_min != None:
        print("Min value of " + sensor2 + " is " + str(sensor2_min))
        print("Max value of " + sensor2 + " is " + str(sensor2_max))
    else:
        print(sensor2 + " value list is empty")

def get_simple_moving_average(value_list):
    sma = 0
    if len(value_list) >= COUNT_FOR_SMA:
        for i in range(1,COUNT_FOR_SMA+1):
            sma = sma+value_list[-i]
        sma = sma/COUNT_FOR_SMA
        return sma
    else:
        return None

def print_simple_moving_average(sensor1,sensor1_values,sensor2,sensor2_values):
    sensor1_sma = get_simple_moving_average(sensor1_values)
    sensor2_sma = get_simple_moving_average(sensor2_values)
    if sensor1_sma != None:
        print("Simple Moving Average of last " + str(COUNT_FOR_SMA) + " values of " + sensor1 + " is " + str(sensor1_sma))
    else:
        print("Number of values in " + sensor1 + " list is less than " + str(COUNT_FOR_SMA))
    if sensor2_sma != None:
        print("Simple Moving Average of last " + str(COUNT_FOR_SMA) + " values of " + sensor2 + " is " + str(sensor2_sma))
    else:
        print("Number of values in " + sensor2 + " list is less than " + str(COUNT_FOR_SMA))
    
def main_func(input_stream):
    if input_stream != "":
        sensor1,sensor1_values,sensor2,sensor2_values = get_data_from_input_stream(input_stream)
        print_max_min(sensor1,sensor1_values,sensor2,sensor2_values)
        print_simple_moving_average(sensor1,sensor1_values,sensor2,sensor2_values)
    else:
        print("Input stream empty")

if __name__ == "__main__":
    lines_read = sys.stdin.readlines()
    main_func(lines_read)
