# from connect_to_board import Modbusconnection
import urllib.request, json
import time
import csv 

if __name__ == "__main__":
    # test = Modbusconnection()
    # flag = test.connect_modbus()
    # print(flag)

keys = ['id1', 'id83','id87','id90']



with open('test_charging_data3.csv', mode = 'w') as data_file:
    data_writer = csv.writer(data_file, delimiter=',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
    with urllib.request.urlopen("http://192.168.1.2/JsonUpdateParamIdValues.cgi?"+str(time.time())) as url:
        while 1:
            # this code is able to get the Current JSON information from the server 
                data = json.loads(url.read().decode()) 
                # data = url.read().decode()
                # print(data)
                # print(type(data))
                print(data['id1'])
                # data_writer.writerow([str(time.time()), str(data['id1'])])

              
            
            
        
            
            
    
        