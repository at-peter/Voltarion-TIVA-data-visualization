import nidaqmx
import time
import numpy as np 
from nidaqmx.stream_readers import AnalogMultiChannelReader
s = np.zeros([3])
# ai7 is the photodiode sensor 
with nidaqmx.Task() as task: 
    # setting up the voltage channels for 
    task.ai_channels.add_ai_voltage_chan("Dev2/ai7")
    task.ai_channels.add_ai_voltage_chan("Dev2/ai1")
    task.ai_channels.add_ai_voltage_chan("Dev2/ai2")
    # task.ai_channels.add_ai_voltage_chan("Dev2/ai3")
    # task.ai_channels.add_ai_voltage_chan("Dev2/ai4")
    reader = AnalogMultiChannelReader(task)
    with nidaqmx.Task() as task2:
        volatage_array=[3,3] 
        task2.ao_channels.add_ao_voltage_chan("Dev2/ao0")
        task2.ao_channels.add_ao_voltage_chan("Dev2/ao1")
        task2.write(volatage_array, auto_start=True)
        for i in range(0,20):
            x = reader.read_many_sample(s)

            print(s)
            time.sleep(1)
        task2.write([0,0], auto_start=True)


def start_sensor_task(sensors):
    with nidaqmx.Task() as task:
        for sensor in sensors:
            print(sensor)
            task.ai_channels.add_ai_voltage_chan("Dev2/"+sensor)
        print(task)
    return task

# sensors = ['ai0', 'ai1']
# task = start_sensor_task(sensors)
# print(task)
# for i in range(5):
#     s = task.read()
#     print(s)
#     time.sleep(1)
    
# def read_sensor_value(sensor_task):
#     with nidaqmx.Task() as task:
#         task.ai_channels.add_ai_voltage_chan("Dev2/"+sensor)
    

def set_voltage(voltage ):
    volatage_array = [voltage,voltage]
    with nidaqmx.Task() as task: 
        task.ao_channels.add_ao_voltage_chan("Dev2/ao0")
        task.ao_channels.add_ao_voltage_chan("Dev2/ao1")
        task.write(volatage_array, auto_start=True)
    
# set_voltage(0)

# for i in range(5):
#     print(i)
#     if i == 0:
#         set_voltage(3)
    
#     if i == 4:
#         set_voltage(0)
#     time.sleep(2)
    
# set_voltage(0)
# print("its done! Kill the power if the pumps are still on")


