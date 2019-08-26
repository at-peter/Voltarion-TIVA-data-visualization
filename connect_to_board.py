from pyModbusTCP.client import ModbusClient

# c = ModbusClient(host="192.168.1.2", port=502, auto_open=True)


# while True:
#     # open or reconnect TCP to server
#     if not c.is_open():
#         if not c.open():
#             print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))
    
#     if c.is_open():
#         current = c.read_holding_registers(1,3)
#         voltage = c.read_holding_registers(89, 3)
#         temperature = c.read_holding_registers(83, 3)

#         if current:
#             print("Current 1", str(current))
#             print("Voltage X4", str(voltage))
#             print("Temperature", str(temperature))
#             print("------------------------------")
#     time.sleep(5)
    


class Modbusconnection():
    def __init__(self, ip_address = "192.168.1.2"):
        self.connection = None 
        self.ip_address = ip_address
    
    def connect_modbus(self):
        self.connection = ModbusClient(host=self.ip_address, port=502, auto_open=True)
        flag = True 
        if not self.connection.is_open():
            if not self.connection.open():
                print("Unable to connect to "+ self.ip_address)
                flag = False 
        else: 
            print("Server Connected")
        return flag

    def get_data(self):
        temp = self.connection.read_holding_registers(83,1)
        volt = self.connection.read_holding_registers(89,1)
        cur = self.connection.read_holding_registers(1,1)
        data = {
            "temperature" : temp, 
            "Voltage": volt, 
            "Current": cur
        }
        return data 