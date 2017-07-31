#Import localizations from hdf5 data
import h5py as h5py
import numpy as np
import glob
import os

# Loading hdf5 files
def loadlocs(path):    
    with h5py.File(path, 'r') as locs_file:
        locs = locs_file['locs'][...]
    locs = np.rec.array(locs, dtype=locs.dtype)    
    return locs

# Navigate to the script path
os.chdir('./')

# Initialize variables
channel = 0
data_exp = []
First = True

# Iterate through hdf5 files in the current folder and concatenate data
for file in glob.glob("*.hdf5"):
    locs = loadlocs(file)
    tempdata_xyz = locs[['x','y','z','frame']].copy()
    tempdata_xyz['x']=tempdata_xyz['x']*130
    tempdata_xyz['y']=tempdata_xyz['y']*130
    tempdata = np.array(tempdata_xyz.tolist())
    tempdata_channel = np.hstack((tempdata,np.zeros((tempdata.shape[0],1))+channel))
    if First:
        data_exp = tempdata_channel
        First = False
    else:
        data_exp = np.concatenate((data_exp, tempdata_channel), axis=0)
    print('Channel {} is file {}'.format(channel,file))
    channel+=1 

# Export as tab deliminated txt file
np.savetxt('concat_export.txt', data_exp, fmt=['%.1f','%.1f','%.1f','%.1f','%i'], newline='\r\n', delimiter='\t')