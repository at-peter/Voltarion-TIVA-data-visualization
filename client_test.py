import socketio 
import asyncio

loop = asyncio.get_event_loop()
sio = socketio.AsyncClient()

@sio.on('connect')
def connect():
    print('Connected to server')

@sio.on('message')
async def message(data):
    print("Received data from server: " + str(data["Voltage"]) + str(data["Current"])+ str(data["temperature"]))

async def start_client():
    await sio.connect('http://localhost:3000')
    await sio.wait()

if __name__ == "__main__":
    
    loop.run_until_complete(start_client())
    # loop.stop()
    

