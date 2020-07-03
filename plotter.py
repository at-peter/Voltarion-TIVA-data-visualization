import matplotlib.pyplot as plt
import numpy as np
import csv
import plotly.graph_objects as go



if __name__ == '__main__':
    # open the csv file and extract the data
    data_for_plot = []
    with open('test_charging_may22_1.csv', mode='r') as data_file:
        csv_reader = csv.DictReader(data_file, fieldnames=['time','current', 'temp', 'voltage', 'temp2'])
        print(csv_reader)
        for row in csv_reader:
            data_for_plot.append(row['current'])

    x = np.arange(len(data_for_plot))

    fig = go.Figure(data=go.Scatter(x=x, y =data_for_plot, mode='markers'))
    fig.show()
    # plt.plot(x,data_for_plot)
    # plt.yticks(np.arange(-0.5,3.5, 0.5))
    # plt.title('Voltage')
    # plt.show()