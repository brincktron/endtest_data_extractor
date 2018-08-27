import pandas as pd
import os
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

def panda_read_data(path):
    pandatable = pd.read_csv(path, sep='\t')
    value = pandatable.iloc[:, [0,1,2, -1]]
    return value

complete = panda_read_data(full_path[0])
for paths in full_path[1:]:
    temp_data = panda_read_data(paths)
    complete = complete.merge(temp_data, on=['Serialnr', 'Date', 'Time'])


complete.to_csv('complete.txt', sep='\t')
