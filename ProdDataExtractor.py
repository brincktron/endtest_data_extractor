import time
start_time = time.time()
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
relative_path = 'et-data/2018-08-01_161409'
filenames = []
full_path = []

# a function that returns only the first, second, third and last column of the data-files
def panda_read_data(path):
    pandatable = pd.read_csv(path, sep='\t')
    value = pandatable.iloc[:, [0,1,2, -1]]
    return value

# go through the selected folders and find all files within
for idx, name in enumerate(filepaths):
    filenames.append(os.listdir(relative_path + '/' + name))
    full_path.append(relative_path + '/' + name + '/' + filenames[idx][0])
    print 'reading: ' + full_path[idx]
    complete = panda_read_data(full_path[-1])
    y = 1
    while y < len(filenames[idx]):
        full_path.append(relative_path + '/' + name + '/' + filenames[idx][y])
        print 'reading: ' + full_path[-1]
        temp_data = panda_read_data(full_path[-1])
        complete = complete.append(temp_data)
        y += 1
    if idx == 0:
        complete_structure = complete
    if idx > 0:
        complete_structure = complete_structure.merge(complete, on=['Serialnr', 'Date', 'Time'])

# write to
#complete_structure.to_csv('CBD single numbers.txt', sep='\t')
complete_structure.to_excel('CBD single numbers.xlsx')

print 'end test data extraction complete...'
print ("\n --- %s seconds ---" % round(time.time() - start_time,3))
