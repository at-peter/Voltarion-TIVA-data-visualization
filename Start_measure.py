import urllib.request, json
import time
import datetime
import csv 
import dataset
SAMPLE_FREQUENCY = 1 # in hertz
if __name__ == "__main__":
    DT = datetime.datetime.now()
    FILE_NAME = DT.strftime('%d_%b_%Y_%H_%M_%S')
    print("Data will be saved to " + FILE_NAME +'.csv')

    db = dataset.connect('sqlite:///batterydata.db')
    with open(str(FILE_NAME) + '.csv', mode = 'w') as data_file:
        data_writer = csv.writer(data_file, delimiter=',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
        table = db['FILE_NAME']
        while 1:
            with urllib.request.urlopen("http://192.168.1.2/JsonUpdateParamIdValues.cgi?"+str(time.time())) as url:
            # this code is able to get the Current JSON information from the server 
                data = json.loads(url.read().decode()) 
                #This saves the data to the csv file 
                data_writer.writerow([str(time.time()), data['id1'], data ['id83'], data['id87'], data['id90']])
                table.insert(dict(
                    time = time.time(),
                    voltage = data['id87'],
                    current = data['id1']
                    ))
                print("Voltage: ",data['id87']," Current: ", data['id1'])
                
                time.sleep(SAMPLE_FREQUENCY) 
   