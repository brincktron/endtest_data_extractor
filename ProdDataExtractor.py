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
relative_path = 'et-data'

# create all paths
filenames = []
full_path = []
x = 0
while x < len(filepaths):
    filenames.append(os.listdir(relative_path + '/' + filepaths[x]))
    y = 0
    while y < len(filenames[x]):
        full_path[x] = relative_path + '/' + filepaths[x] + '/' + filenames[x][y]
    x += 1

# with pandas
finalDf = pd.DataFrame()
def panda_read_data(path, heading):
    pandatable = pd.read_table(path)
    value  =pandatable[heading]
    return value

x = 0
y = 0
#with pandas
finalDf = pd.DataFrame()
while x < len(filepaths):
    y = 0
    if y == 0:
        finalDf[filepaths[x]] = panda_read_data(full_path[x], filepaths[x])
    else:
        finalDf[filepaths[x]].append(panda_read_data(full_path, filepaths[x]))
    x += 1

print hej
