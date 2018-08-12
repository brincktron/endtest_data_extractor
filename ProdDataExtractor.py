import csv
import pandas as pd
import numpy as np
import os
#df.to_csv("submission2.csv", index=False)
filepaths = ['CBDFull[DutMic0]',
             'CBDFull[DutMic1]',
             'CBDFull[DutMic1-DutMic2]',
             'CBDFull[DutMic2]',
             'CBDHF[DutMic0]',
             'CBDHF[DutMic1]',
             'CBDHF[DutMic1-DutMic2]',
             'CBDHF[DutMic2]',
             'CBDLF[DutMic0]',
             'CBDLF[DutMic1]',
             'CBDLF[DutMic1-DutMic2]',
             'CBDLF[DutMic2]',
             'CBDMF[DutMic0]',
             'CBDMF[DutMic1]',
             'CBDMF[DutMic1-DutMic2]',
             'CBDMF[DutMic2]',
             ]
full_path = 'et-data/CBDHF[DutMic0]/CBDHF[DutMic0] 2018-08-01.txt'
relative_path = 'et-data'
filenames = []
x = 0
while x < len(filepaths):
    filenames.append(os.listdir(relative_path + '/'+ filepaths[x]))
    x += 1

# with csv reader arrays
def csv_read_data(path):
    value = []
    serial = []
    with open(path, 'r') as f:
        next(f) # skip headings
        reader = csv.reader(f, delimiter='\t')
        # the data we are interested in are the first (serial) and the last (CBD data) value
        for data in reader:
            serial.append(data[0])
            value.append(data[-1])
    return serial, value


# with pandas
finalDf = pd.DataFrame()
def panda_read_data(path, heading):
    pandatable = pd.read_table(path)
    serial = pandatable.Serialnr
    value  =pandatable[heading]
    return serial, value

serial = []
complete_data = {}
x = 0

#with pandas
finalDf = pd.DataFrame()
while x < len(filepaths):
    y = 0
    while y < len(filenames[x]):
        full_path = relative_path + '/' + filepaths[x] + '/' + filenames[x][y]
        # with pandas
        pandaserial, finalDf[filepaths[x]] = panda_read_data(full_path, filepaths[x])
        if y == 0:
            complete_data[filepaths[x] + 'serial'], complete_data[filepaths[x]] = csv_read_data(full_path)
        else:
            complete_data[filepaths[x] + 'serial'].extend(csv_read_data(full_path)[0])
            complete_data[filepaths[x]].extend(csv_read_data(full_path)[1])
        y += 1
    x += 1
serial, value = csv_read_data(relative_path + '/' + filepaths[1] + '/' + filenames[1][0])

# check serial numbers
#for x in complete_data
#    if complete_data[filepaths[x]] ==
#with numpy arrays

print hej
