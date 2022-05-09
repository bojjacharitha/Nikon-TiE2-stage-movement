import pymmcore
import os.path
from pylab import *
import matplotlib.pyplot as plt
import PySimpleGUI 
import h5py

mm_dir = "C:/Program Files/Micro-Manager-2"
mmc = pymmcore.CMMCore()
mmc.setDeviceAdapterSearchPaths([mm_dir])
mmc.loadSystemConfiguration(os.path.join(mm_dir, "MMConfig_demo.cfg"))

#original reference position to the user
pos = mmc.setXYPosition(30000.0,9000.0)
pos = mmc.getXYPosition()
print(pos)


#1146880 = 2048*560 
#2048*2048 is the array size for each single capture of the image
#560 = 14*40 where 14 is the row wise divisions and 40 is the column wise divisions of slide
arr1 = [[0 for i in range(1146880)] for j in range(2048)]
for i in range(0,1146880,2048):
    mmc.snapImage()
    img = mmc.getImage();
    arr = np.asarray(img)
    if (mmc.getXPosition()>=-3000 or mmc.getXPosition()<=3000):
       pos = mmc.setXYPosition(mmc.getXPosition()+1500.0,mmc.getYPosition())
    else:
       pos = mmc.setXYPosition(mmc.getXPosition(),mmc.getYPosition()+1500.0)
 
    for j in range(2048):
        for k in range(2048):
            arr1[j][i+k] = arr[j][k]

# creating a file
f = h5py.File('test1.hdf5', 'w')
dset = f.create_dataset("default", data = arr1)
f.close()