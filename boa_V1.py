import numpy as np
import json
import urlib.request
import dataset
import datetime
import time
import commentjson
import asyncio
import nidaqmx
import keyboard
import sys
import statistics
SAMPLE_FREQUENCY=1

class Boa:
    def __init__(self):

    async def __load_configs(self, config):
    # this function loads the config file
        with open(config) as f:
            config_dict = commentjson.load(f)

        return config_dict

    async def __open_database(self, dbname):
        # this function opens the database and the right table
        db = dataset.connect('sqlite:///peterstestdb.db')
        DT = datetime.datetime.now()
        filename = DT.strftime('%d_%b_%Y_%H_%M_%S')
        table = db[filename]

        return table

    async def set_pump_voltage(self, pump, voltage):
        with nidaqx.Task() as task:

        return status

    async def read_sensor_values(self ,sensor):
        return value

    def run_cheatmode(self,file_name = False):
        DT = datetime.datetime.now()
        FILE_NAME = DT.strftime('%d_%b_%Y_%H_%M_%S')
        SAMPLE_FREQUENCY=1
        if file_name:
            FILE_NAME = file_name

        db = dataset.connect('sqlite:///testdatabase.db')
        table = db['']
        with urlib.request.urlopen("http://192.168.1.2/JsonUpdateParamIdValues.cgi?"+str(time.time())) as url:
                with nidamx.Task() as task:
                    #Pump output channels
                    task.ao_channels.add_ao_voltage_chan("Dev2/ao0")
                    task.ao_channels.add_ao_voltage_chan('Dev2/ao1')
                    # Inputs from sensor:
                    # SOC sensor
                    task.ai_channels.add_ai_voltage_chan("Dev2/ai7")
                    # TODO: will need to figure out whit
                    # ai0; flowrate +
                    task.ai_channels.add_ai_voltage_chan("Dev2/ai0")
                    #ai1; flowrate -
                    task.ai_channels.add_ai_voltage_chan("Dev2/ai1")
                    # inlet pressure +
                    task.ai_channels.add_ai_voltage_chan("Dev2/ai2")
                    # inlet pressure -
                    task.ai_channels.add_ai_voltage_chan("Dev2/ai3")
                    # outlet pressure +
                    task.ai_channels.add_ai_voltage_chan("Dev2/ai4")
                    # outlet pressure -
                    task.ai_channels.add_ai_voltage_chan("Dev2/ai5")


                    while 1 :
                        if keyboard.is_pressed('p'):
                            # set the pump voltages to 0
                            task.write([0,0], auto_start=True)
                            time.sleep(2)
                            sys.exit('Pumps should have shut down. If they have not then we have a problem')

                        voltage_data = json.loads(url.read().decode())
                        other_data = task.read()

                        mean_voltage = statistics.mean([float(voltage_data['id87'],float([voltage_data['id_88']]))])
                        current = float(voltage_data['id1'])
                        table.insert(dict(
                            time = time.time(),
                            voltage=mean_voltage,
                            current=current,
                            inlet_pressure=,
                            inlet_flow_rate=,
                            outlet_pressure=,
                            outlet_flow_rate=,
                            state_of_charge=,

                        ))
                        print("Current ")

                        time.sleep(SAMPLE_FREQUENCY)



        return
def __main():
    m = Boa(database_name)
    m.run_cheatmode()



if __name__ == '__main__':
    # asyncio.run(__main(),debug=True)
    __main()










if __name__ == '__main__':
    __main()