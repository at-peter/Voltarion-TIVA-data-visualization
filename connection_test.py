# from connect_to_board import Modbusconnection
import urllib.request, json
import time
import csv 

if __name__ == "__main__":
    # test = Modbusconnection()
    # flag = test.connect_modbus()
    # print(flag)

    keys = ['id1', 'id83','id87','id90']



    with open('test_charging_data_lunch.csv', mode = 'w') as data_file:
        data_writer = csv.writer(data_file, delimiter=',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
        
        while 1:
            with urllib.request.urlopen("http://192.168.1.2/JsonUpdateParamIdValues.cgi?"+str(time.time())) as url:
            # this code is able to get the Current JSON information from the server 
                data = json.loads(url.read().decode()) 
                # data = url.read().decode()
                # print(data)
                # print(type(data))
                # for key in keys:
                #     print(data[key])
                print('.')
                data_writer.writerow([str(time.time()), data['id1'], data ['id83'], data['id87'], data['id90']])
                time.sleep(1) 


              
            
# TODO: Make a class for this so that I can just call it in server.py
            
class Csv_logger ():


    def __init__(self):
    self.ip = '192.168.1.2'
    self.keys = []

    def _openConnection(self):


    def _getData(self):


            
            
    
        
        