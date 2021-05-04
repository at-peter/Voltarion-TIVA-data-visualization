import nidaqmx
import time
import sys
def get_name():
    '''
    This function gets the name of attached devices 
    '''
    import nidaqmx.system
    system = nidaqmx.system.System.local() 
    for device in system.devices:
        devs = device.name
        print(devs)

    return devs

def make_task(name):
    '''
    This function makes a task and gives it a name
    '''
    task = nidaqmx.task.Task(name)
    return task

def end_task(task):
    '''
    This function closes a task 
    '''
    try: 
        task.close()
        return 1 
    except: 
        print('an exception happened ', sys.exc_info()[0])
        return 0
    
def add_ao_channel(task, channel_array):
    '''
    This function adds Analog output channel to a task
    '''
    for channel in enumerate(channel_array):
        task.ao_channels.add_ao_voltage_chan(channel[1])
    
def write_to_ao_channel(task, values):
    try: 
        task.write(values)
    except: 
        print('an exception happened ', sys.exc_info()[0])

def add_ai_channel(task, channel_array):
    for channel in enumerate(channel_array):
        task.ai_channels.add_ai_voltage_chan(channel[1])



if __name__ == "__main__":
    dev_name = get_name()
    test_task = make_task('test')
    second_task = make_task('input')
    add_ai_channel(second_task, [dev_name+'/ai1'])
    add_ao_channel(test_task, [dev_name+'/ao0', dev_name+'/ao1'])
    pump1 = int(input("Pump 1 voltage: "))
    pump2 = int(input("Pump 2 voltage: "))
    # Main loop
    while True:
        try:
            data = second_task.read(3)
            print(data)
            time.sleep(1)
            write_to_ao_channel(test_task,[pump2,pump1])
            data =second_task.read(3)
            print(data)
            time.sleep(1)
            write_to_ao_channel(test_task, [0,0])
            time.sleep(1)
            data = second_task.read(3)
            print(data)
        except KeyboardInterrupt:
            #This code executes when ctr-c is pressed so that the pumps shut down
            print('Keyboard interupt detected')
            #Shutdown the pump:
            write_to_ao_channel(test_task, [0,0])
            print('voltage to pumps sent to 0')
            # close the tasks: 
            c = end_task(test_task)
            d = end_task(second_task)
            print('tasks shut down')
            #this line exits the program 
            sys.exit(0)
      
        
    # for i in range(4):
    #     write_to_ao_channel(test_task, [1,1])
    #     write_to_ao_channel(test_task,[0,0])
    # add_ai_channel(second_task, [dev_name+'/ai1'])
    # second_task.start()
    # for i in range(5):
    #     second_task = make_task('input')
    #     add_ai_channel(second_task, [dev_name+'/ai0'])
    #     data = second_task.read(5)
    #     print(data) # TODO: figure out why the
    #     time.sleep(1)
    #     second_task.close()

    # It seems that ending the task does not actually clear the values in channels. 
    # this means that when shutting down the system I will have to actually write zeroes to it.
    c = end_task(test_task)
    d = end_task(second_task)
    print('exit code', c)
    print('exit code', d)

