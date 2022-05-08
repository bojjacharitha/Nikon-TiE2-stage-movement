import pymmcore
import os.path
from pylab import *
import matplotlib.pyplot as plt
import PySimpleGUI 

mm_dir = "C:/Program Files/Micro-Manager-2"
mmc = pymmcore.CMMCore()
mmc.setDeviceAdapterSearchPaths([mm_dir])
mmc.loadSystemConfiguration(os.path.join(mm_dir, "MMConfig_demo.cfg"))
mmc.snapImage()
img = mmc.getImage();
arr = np.asarray(img)
print(arr)
ion() # Activate interactive mode
figure()
plt.imshow(arr,cmap = 'gray')
plt.show()

width = mmc.getImageWidth()
print(width)
height = mmc.getImageHeight()
print(height)
pos = mmc.getXYPosition()
print(pos)
pos = mmc.setXYPosition(mmc.getXPosition()+1000.0,mmc.getYPosition()+1000.0)
pos = mmc.getXYPosition()
print(pos)
