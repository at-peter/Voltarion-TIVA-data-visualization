import socketio
from aiohttp import web
from connect_to_board import Modbusconnection 

'''
This is 
'''

# Sio server setup 
sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

#modbus connection: 
async def background_loop():
    MBconnect = Modbusconnection()
    con = MBconnect.connect_modbus()

    while True:
        data = MBconnect.get_data() 
        await sio.emit('message', data )
        await sio.sleep(3)
        print(data)




@sio.on('connect')
def connect(sid, environ):
    print("connect ", sid)
    # This is where I can start emitting the data to the client 
    
    

@sio.on('message')
async def chat_message(sid, data):
    print("message ", data)
    await sio.emit('reply', room=sid)

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)

# one does not need these, especially for a web server that uses a webapp as a front end. 
# app.router.add_static('/static', 'static')
# app.router.add_get('/', index)


if __name__ == '__main__' :
    sio.start_background_task(background_loop)
    web.run_app(app=app, port = 3000, host = 'localhost' )
    

