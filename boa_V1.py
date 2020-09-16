import numpy as np
import json
import urlib.request
import dataset
import datetime
import time
import commentjson


SAMPLE_FREQUENCY=1

class Boa:
    def __init__(self):

    def __load_configs(self, config):
    # this function loads the config file
        with open(config_file) as f:
            config_dict = commentjson.load(f)

        return config_dict

    def __open_database(self, dbname):
        # this function opens the database and the right table
        db = dataset.connect('sqlite:///peterstestdb.db')
        DT = datetime.datetime.now()
        filename = DT.strftime('%d_%b_%Y_%H_%M_%S')
        table = db[filename]

        return table

    def set_pump_voltage(self, pump, voltage):
        return status

    def read_sensor_values(self ,sensor):
        return value

def __main():











if __name__ == '__main__':
    __main()