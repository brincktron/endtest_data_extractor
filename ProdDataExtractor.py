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
for idx, name in enumerate(filepaths):
    filenames.append(os.listdir(relative_path + '/' + name))
    y = 0
    while y < len(filenames[idx]):
        full_path.append(relative_path + '/' + name + '/' + filenames[idx][y])
        y += 1

# with pandas
def panda_read_data(path, heading):
    pandatable = pd.read_table(path)
    value = pandatable[heading]
    return value

finalDf = pd.DataFrame(columns = filepaths)
appendwith = pd.read_table(full_path[0])[filepaths[0]]
finalDf = finalDf.append(appendwith)
print finalDf
print 'lort'
#for idx, path in enumerate(filepaths):
#    y = 0
#    while y < len(filenames[idx]):
#        finalDf.append(panda_read_data(full_path[idx+y], filenames[idx][y])
#        y += 1


print finalDf
