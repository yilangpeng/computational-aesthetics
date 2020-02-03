# Computational aesthetics

In this repository you can find codes for caculating various visual attributes in Python.

Include:

## Color-related attributes
* RGB
* HSV
* XYZ
* Brightness
* Contrast
* Colorfulness
* Color variety
* Percentages of eleven basic colors: red, orange, yellow, green, blue, pink, purple, brown, gray, black, white

## Composition-related attributes
* Height, width, size, aspect ratio
* Visual complexity
  * JPEG filesize
  * Edge density
  * Edge distribution
  * Bounding box
* Rule of thirds
* Symmetry
(will be updated later)

## Content-related atttributes
* Number of faces
* Face size
(will be updated later)

## How to use
1. Install the following packages
* numpy
* opencv
* scikit-image

2. Create three folders
* img original: place the images you want to process inside this folder. Please convert all your images to .JPG format first.
* img transform: this folder saves the transformed versions (e.g., edge detection)
* img result: this folder saves results in .txt files.

3. Run each Python script

## basic.py
This script caculates the following visual attributes:
* filesize: the filesize of the image. Can be used as an indicator of visual complexity.
* w, h: width and height of the image (in pixels).
* ar, size: aspect ratio and image size.
* rgbR, rgbG, rgbB, rgbR_sd, rgbG_sd, rgbB_sd: means and standard deviations of R, G, B values.
* hue, saturation, value, hue_sd, saturation_sd, value_sd: means and standard deviations of H, S, V values.
* xyzX, xyzY, xyzZ, xyzX_sd, xyzY_sd, xyzZ_sd: : means and standard deviations of X, Y, Z values. Y is an indicator of luminance.
* bright, bright_sd: mean and standard deviation of brightness
* contrast: contrast. The script finds a range in the brightess histogram that covers 95% of the mass of the histogram.
* colorful: colorfulness [(Hasler & Suesstrunk, 2003)](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/5007/0000/Measuring-colorfulness-in-natural-images/10.1117/12.477378.short?SSO=1)
* hue_count: hue count, an indicatorof color variety [(Ke et al., 2006)](https://ieeexplore.ieee.org/abstract/document/1640788)

## colorname.py
This script assigns each RGB value into one of the eleven basic colors (black, blue, brown, gray, green, orange, pink, purple, red, white, yellow) based on a dataset in [(Van De Weijer et al., 2009)](https://ieeexplore.ieee.org/abstract/document/4270243). It caculates the percentages of eleven basic colors and creates a PNG file that stores the assigned colors.

### examples
<p float="left">
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20all/Chefchaouen1.jpg" width="400" />
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20transform/colorname/Chefchaouen1.png" width="400" /> 
</p>
<p float="left">
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20all/Philadelphia7.jpg" width="300" />
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20transform/colorname/Philadelphia7.png" width="300" /> 
</p>

## edge.py
This script detects edges in images and caculates edge-related visual attributes.
* edge density: the area occupied by edge points, an indicator of feature complexity.
* edge distribution: the average distance between edge points among all pairs of edge pointsm.
* bounding box: the size of a box that contains at least 95% of all the edge points.

## References
Please cite the following articles:
* Peng, Y., & Jemmott III, J. B. (2018). Feast for the eyes: Effects of food Perceptions and computer vision features on food photo popularity. International Journal of Communication, 12: 313–336 [PDF](https://ijoc.org/index.php/ijoc/article/view/6678)
* Peng, Y. (2018). Same candidates, different faces: Uncovering media bias in visual portrayals of presidential candidates with computer vision. Journal of Communication, 68(5): 920-941. [PDF](https://www.researchgate.net/profile/Yilang_Peng2/publication/328005872_Same_Candidates_Different_Faces_Uncovering_Media_Bias_in_Visual_Portrayals_of_Presidential_Candidates_with_Computer_Vision/links/5bb9a125a6fdcc9552d50673/Same-Candidates-Different-Faces-Uncovering-Media-Bias-in-Visual-Portrayals-of-Presidential-Candidates-with-Computer-Vision.pdf)
