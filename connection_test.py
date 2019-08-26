from connect_to_board import Modbusconnection
import urllib.request, json
import time

if __name__ == "__main__":
    # test = Modbusconnection()
    # flag = test.connect_modbus()
    # print(flag)



    # this code is able to get the Current JSON information from the server 
    with urllib.request.urlopen("http://192.168.1.2/JsonUpdateParamIdValues.cgi?"+str(time.time())) as url:
        data = json.loads(url.read().decode())
        # data = url.read().decode()
        print(data)
        print(type(data))