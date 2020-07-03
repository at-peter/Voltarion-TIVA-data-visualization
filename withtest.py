
import time
import csv

with open('withtest1.csv', mode = 'w') as data_file:
            data_writer = csv.writer(data_file, delimiter=' ', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
            # the for loop needs to be inside the "try/finally" structure of the with statement
            # I wonder if you could nest with statements ?
            for n in range(10):
                data_writer.writerow([str(time.time())]) 
                print('.')
                time.sleep(2)