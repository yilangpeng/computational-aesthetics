# Computational aesthetics [under construction]

Computationally caculated visual attributes have been demonstrated to predict a wide range of outcomes, such as images' aesthetic appeal, popularity on social media, and interestingness. In this repository you can find Python codes to caculate various visual attributes, including:
* Color-related attributes, such as brightness, contrast, colorfulness, color variety, and percentages of basic colors
* Composition-related attributes, such as visual complexity, rule of thirds, symmetry

If you find this repository useful, please consider citing the following articles:
* Peng, Y., & Jemmott III, J. B. (2018). Feast for the eyes: Effects of food Perceptions and computer vision features on food photo popularity. [PDF](https://ijoc.org/index.php/ijoc/article/view/6678)
* Peng, Y. (2018). Same candidates, different faces: Uncovering media bias in visual portrayals of presidential candidates with computer vision. [PDF](https://www.researchgate.net/profile/Yilang_Peng2/publication/328005872_Same_Candidates_Different_Faces_Uncovering_Media_Bias_in_Visual_Portrayals_of_Presidential_Candidates_with_Computer_Vision/links/5bb9a125a6fdcc9552d50673/Same-Candidates-Different-Faces-Uncovering-Media-Bias-in-Visual-Portrayals-of-Presidential-Candidates-with-Computer-Vision.pdf)

## How to use
1. Install the following packages
* numpy
* opencv
* scikit-image
* Pillow

2. Create folders
* img all: place the images you want to process inside this folder. Please convert all your images to .JPG format first.
* img transform: this folder saves the transformed versions (e.g., edge detection)
* img result: this folder saves results in .txt files.

3. Run each Python script

## basic.py
This script caculates some basic visual attributes:
* filesize: the file size of the image. Can be used as an indicator of visual complexity.
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
This script assigns each RGB value into one of the eleven basic colors (black, blue, brown, gray, green, orange, pink, purple, red, white, yellow) based on a dataset in [(Van De Weijer et al., 2009)](https://ieeexplore.ieee.org/abstract/document/4270243). It caculates the percentages of these basic colors and creates a PNG file that stores the assigned colors.

### example
<p float="left">
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20all/Philadelphia7.jpg" width="400" />
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20transform/colorname/Philadelphia7.png" width="400" /> 
</p>

## edge.py
This script detects edges in images and caculates edge-related visual attributes.
* edensity: edge density, calculated as the area occupied by edge points. This attribute is an indicator of visual complexity.
* edist: edge distribution, calculated as the average distance between edge points among all pairs of edge points. This attribute is an indicator of visual complexity.

### example
<p float="left">
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20all/Chefchaouen2.jpg" width="300" />
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20transform/edge%20canny/Chefchaouen2.png" width="300" /> 
</p>

## segment.py
This script conducts image segmentation using two methods in scikit-image: quickshit and normalized cut. It then caculates the number of segments and the size of the largest, second largest, and third largest segment. 
* nseg: number of segments, which can be an indicator of visual complexity.
* nseg_l: number of segments that are larger than a threshold (5% of the image area)
* size0, size1, size2: the size of the largest, second largest, and third largest segment.

<p float="left">
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20all/Texas1.jpg" width="400" />
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20transform/segment%20normalized_cut/Texas1 ava.png" width="400" /> 
</p>

## box.py
This script finds a box that contains at least 95% of values in a grayscale image. The grayscale image can be an edge map or a saliency map.

## saliency.py
This script creates a saliency map of the image and caculate saliency-related visual attributes.

## preprocess.py
This script conducts some preprocessing of the data. It converts still PNG and GIF files to JPG format and resizes large images.

## References
* Peng, Y., & Jemmott III, J. B. (2018). Feast for the eyes: Effects of food Perceptions and computer vision features on food photo popularity. International Journal of Communication, 12: 313–336 [PDF](https://ijoc.org/index.php/ijoc/article/view/6678)
* Peng, Y. (2018). Same candidates, different faces: Uncovering media bias in visual portrayals of presidential candidates with computer vision. Journal of Communication, 68(5): 920-941. [PDF](https://www.researchgate.net/profile/Yilang_Peng2/publication/328005872_Same_Candidates_Different_Faces_Uncovering_Media_Bias_in_Visual_Portrayals_of_Presidential_Candidates_with_Computer_Vision/links/5bb9a125a6fdcc9552d50673/Same-Candidates-Different-Faces-Uncovering-Media-Bias-in-Visual-Portrayals-of-Presidential-Candidates-with-Computer-Vision.pdf)
