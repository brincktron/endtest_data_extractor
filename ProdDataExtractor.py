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
relative_path = 'et-data'
filenames = []
full_path = []

# a function that returns only the first, second, third and last column of the data-files
def panda_read_data(path):
    pandatable = pd.read_csv(path, sep='\t')
    value = pandatable.iloc[:, [0,1,2, -1]]
    return value

# go through the selected folders and find all files within
for idx, path in enumerate(filepaths):
    filenames.append(os.listdir(relative_path + '/' + path))
    # initialize empty DataFrame for each folderpath
    complete = pd.DataFrame()
    for name in filenames[idx]:
        full_path.append(relative_path + '/' + path + '/' + name)
        print 'reading: ' + full_path[-1]
        complete = complete.append(panda_read_data(full_path[-1]))
    if idx == 0:
        completeDF = complete
    completeDF = completeDF.merge(complete, on=['Serialnr', 'Date', 'Time'])

# write to
#complete_structure.to_csv('CBD single numbers.txt', sep='\t')
completeDF.to_excel('CBD single numbers.xlsx')

print 'end test data extraction complete...'
print ("\n --- %s seconds ---" % round(time.time() - start_time, 3))
