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
#mmc.snapImage()
#img = mmc.getImage();
#arr = np.asarray(img)
#print(arr.shape)
#ion() # Activate interactive mode
#figure()
#plt.imshow(arr,cmap = 'gray')
#plt.show()

#width = mmc.getImageWidth()
#print(width)
#height = mmc.getImageHeight()
#print(height)
#pos = mmc.getXYPosition()
#print(pos)
pos = mmc.setXYPosition(30000.0,9000.0)
pos = mmc.getXYPosition()
print(pos)


arr1 = [[0 for i in range(10)] for j in range(5)]
for i in range(0,10,5):
    mmc.snapImage()
    img = mmc.getImage();
    arr = np.asarray(img)
    if (mmc.getXPosition()>=-3000 or mmc.getXPosition()<=3000):
       pos = mmc.setXYPosition(mmc.getXPosition()+1500.0,mmc.getYPosition())
    else:
       pos = mmc.setXYPosition(mmc.getXPosition(),mmc.getYPosition()+1500.0)
 
    for j in range(5):
        for k in range(5):
            arr1[j][i+k] = arr[j][k]

# creating a file
f = h5py.File('test1.hdf5', 'w')
dset = f.create_dataset("default", data = arr1)
f.close()
