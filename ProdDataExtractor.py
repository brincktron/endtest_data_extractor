import pandas as pd
import os
import sys

# list of single-number rating folders
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

# create all paths
relative_path = 'et-data'
filenames = []
full_path = []

# go through the selected folders and find all files within
for idx, name in enumerate(filepaths):
    filenames.append(os.listdir(relative_path + '/' + name))
    y = 0
    while y < len(filenames[idx]):
        full_path.append(relative_path + '/' + name + '/' + filenames[idx][y])
        y += 1

# a function that returns only the first, second, third and last column of the data-files
def panda_read_data(path):
    pandatable = pd.read_csv(path, sep='\t')
    value = pandatable.iloc[:, [0,1,2, -1]]
    return value

# Generate the first line with headers and...
complete = panda_read_data(full_path[0])

# ... append the rest of the data from the data files
for paths in full_path[1:]:
    temp_data = panda_read_data(paths)
    complete = complete.merge(temp_data, on=['Serialnr', 'Date', 'Time'])
    if complete.shape[0] != temp_data.shape[0]:
        sys.exit('error in data format, cannot combine files')

# write to
complete.to_csv('CBD single numbers.txt', sep='\t')

print 'end test data extraction complete...'