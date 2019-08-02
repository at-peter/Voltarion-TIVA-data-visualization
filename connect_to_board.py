from pyModbusTCP.client import ModbusClient
import time

c = ModbusClient(host="192.168.1.2", port=502, auto_open=True)


while True:
    # open or reconnect TCP to server
    if not c.is_open():
        if not c.open():
            print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))
    
    if c.is_open():
        current = c.read_holding_registers(1,3)
        voltage = c.read_holding_registers(89, 3)
        temperature = c.read_holding_registers(83, 3)

        if current:
            print("Current 1", str(current))
            print("Voltage X4", str(voltage))
            print("Temperature", str(temperature))
            print("------------------------------")
    time.sleep(5)
    