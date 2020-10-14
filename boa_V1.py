import numpy as np
import json
import urllib.request
import dataset
import datetime
import time
# import commentjson
import asyncio
import nidaqmx
import keyboard
import sys
import statistics
SAMPLE_FREQUENCY=1

class Boa:
    def __init__(self):
        
        return None 
    # async def __load_configs(self, config):
    # # this function loads the config file
    #     with open(config) as f:
    #         config_dict = commentjson.load(f)

    #     return config_dict

    # async def __open_database(self, dbname):
    #     # this function opens the database and the right table
    #     db = dataset.connect('sqlite:///peterstestdb.db')
    #     DT = datetime.datetime.now()
    #     filename = DT.strftime('%d_%b_%Y_%H_%M_%S')
    #     table = db[filename]

    #     return table

    # async def set_pump_voltage(self, pump, voltage):
    #     with nidaqx.Task() as task:

    #     return status

    # async def read_sensor_values(self ,sensor):
    #     return value

    def run_cheatmode(self,file_name = False):
        DT = datetime.datetime.now()
        FILE_NAME = DT.strftime('%d_%b_%Y_%H_%M_%S')
        SAMPLE_FREQUENCY=1
        if file_name:
            FILE_NAME = file_name

        db = dataset.connect('sqlite:///testdatabase.db')
        table = db[FILE_NAME]
       
        
    
        #Pump output channels
        # Inputs from sensor:
        # ai0; flowrate +
        # sensors1.ai_channels.add_ai_voltage_chan("Dev2/ai0")
        #ai1; flowrate -
        # sensors1.ai_channels.add_ai_voltage_chan("Dev2/ai1")
        # # inlet pressure +
        # sensors1.ai_channels.add_ai_voltage_chan("Dev2/ai2")
        # # inlet pressure -
        # sensors.ai_channels.add_ai_voltage_chan("Dev2/ai3")
        # # outlet pressure +
        # sensors.ai_channels.add_ai_voltage_chan("Dev2/ai4")
        # # outlet pressure -
        # sensors.ai_channels.add_ai_voltage_chan("Dev2/ai5")
        # # SOC sensors
        # sensors.ai_channels.add_ai_voltage_chan("Dev2/ai7")
            
        with nidaqmx.Task() as task5:
            task5.ao_channels.add_ao_voltage_chan("Dev2/ao0")
            task5.ao_channels.add_ao_voltage_chan('Dev2/ao1')
            
            print('Program initialized, press s to start. ')
            while 1 :
                with urllib.request.urlopen("http://192.168.1.2/JsonUpdateParamIdValues.cgi?"+str(time.time())) as url:
                    if keyboard.is_pressed('s'):
                        task5.write([3,3],auto_start=True)
                        print('Starting pumps')
                    if keyboard.is_pressed('p'):
                        # set the pump voltages to 0
                        print('Shutting down')
                        task5.write([0,0], auto_start=True)
                        time.sleep(2)
                        task5.close()
                        # sensors1.close()
                        sys.exit('Pumps should have shut down. If they have not then we have a problem')

                    voltage_data = json.loads(url.read().decode())
                    with nidaqmx.Task() as sensors1:
                        sensors1.ai_channels.add_ai_voltage_chan("Dev2/ai0")
                        #ai1; flowrate -
                        sensors1.ai_channels.add_ai_voltage_chan("Dev2/ai1")
                        # # inlet pressure +
                        sensors1.ai_channels.add_ai_voltage_chan("Dev2/ai2")
                        other_data = sensors1.read()
                        sensors1.close()
                    
                    print(other_data)
                    mean_voltage = statistics.mean([float(voltage_data['id87']),float(voltage_data['id88'])])
                    # mean_voltage = float(voltage_data)
                    current = float(voltage_data['id1'])
                    table.insert(dict(
                        time = time.time(),
                        voltage=mean_voltage,
                        current=current
                        # inlet_pressure=,
                        # inlet_flow_rate=,
                        # outlet_pressure=,
                        # outlet_flow_rate=,
                        # state_of_charge=,

                    ))
                    print("Current: ", current, "Voltage: ", mean_voltage)

                    time.sleep(SAMPLE_FREQUENCY)

def __main():
    
    m = Boa()
    m.run_cheatmode('Test_run1')



if __name__ == '__main__':
    # asyncio.run(__main(),debug=True)
    __main()










if __name__ == '__main__':
    __main()