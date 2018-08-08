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
relative_path = 'et-data/'
filenames = []
x = 0
while x < len(filepaths):
    filenames.append(os.listdir(relative_path + filepaths[x]))
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
serial = []
complete_data = {}
x = 0
while x < len(filepaths):
    y = 0
    while y < len(filenames[x]):
        complete_data[filepaths[x] + 'serial'], complete_data[filepaths[x]] = csv_read_data(relative_path + '/' + filepaths[x] + '/' + filenames[x][y])
        y += 1
    x += 1
serial, value = csv_read_data(relative_path + '/' + filepaths[1] + '/' + filenames[1][0])

#with numpy arrays


# with pandas
pandatable = pd.read_table(full_path)
table1 = pandatable.Serialnr
