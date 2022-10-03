# Nikon-TiE2-stage-movement

The camera was not capturing the images at the start because Micro Manager-2 was not able to recognize Hamamatsu. Later, I changed the path in Hardware Configuration Wizard. Then the configuration was successful.

## Libraries installation

python is installed with this link: https://phoenixnap.com/kb/how-to-install-python-3-windows

pip is installed with this link: https://phoenixnap.com/kb/install-pip-windows

matplotlib is installed using the command:  pip install matplotlib

PySimpleGUI is installed using the command:  python -m pip install PySimpleGUI

pymmcore is installed using the following command:  python -m pip install --user pymmcore
     
MMCore library has many commands useful for stage movement. This link is used for writing code:  https://micro-manager.org/apidoc/MMCore/latest/class_c_m_m_core.html

## How it works

After running the code in cmd, the stage moves and captures images. Sometimes, we observe no images(completely black). That's because of light intensity. Keeping track of light intensity is also important. 

# Image registration
Image registration is an image processing technique used for aligning multiple images of the same scene. This technique helps us in getting image offset. Offset in the sense, it's the slight difference in the movement of certain area of an image. 

Firstly, we tried image registration using skimage. But then, the results were not so accurate.
## Skimage registration

Code snippet:
</br>
def registration(reference_image, moving_image):
    shifts, error, phasediff = phase_cross_correlation(reference_image, moving_image, upsample_factor=1, overlap_ratio=0.3)
    return shifts
Link used for referring skimage registration- https://scikit-image.org/docs/stable/api/skimage.registration.html#skimage.registration.phase_cross_correlation

After this, we referred to otsu thresholding.

## Otsu thresholding
This method separates background and foreground pixels. The algorithm iteratively searches for the threshold that minimizes the within-class variance where it is a weighted sum of variances of the two classes (background and foreground). 

<p align="center">Links used to understand otsu thresholding:</p>
https://hbyacademic.medium.com/otsu-thresholding-4337710dc519
http://www.ripublication.com/ijaerdoi/2015/ijaerv10n9_20.pdf
https://muthu.co/otsus-method-for-image-thresholding-explained-and-implemented/

Github code link:
https://github.com/muthuspark/ml_research/blob/master/Otsu%20Thresholding%20implementation.ipynb

