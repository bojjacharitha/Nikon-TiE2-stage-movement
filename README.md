# Nikon-TiE2-stage-movement

The camera was not capturing the images at the start because Micro Manager-2 was not able to recognize Hamamatsu. Later, I changed the path in Hardware Configuration Wizard. Then the configuration was successful.

#Libraries installation

python is installed with this link: https://phoenixnap.com/kb/how-to-install-python-3-windows

pip is installed with this link: https://phoenixnap.com/kb/install-pip-windows

matplotlib is installed using the command:  pip install matplotlib

PySimpleGUI is installed using the command:  python -m pip install PySimpleGUI

pymmcore is installed using the following command:  python -m pip install --user pymmcore
     
MMCore library has many commands useful for stage movement. This link is used for writing code:  https://micro-manager.org/apidoc/MMCore/latest/class_c_m_m_core.html

#How it works

After running the code in cmd, the stage moves and captures images. Sometimes, we observe no images(completely black). That's because of light intensity. Keeping track of light intensity is also important. 

