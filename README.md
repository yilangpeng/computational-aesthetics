# Computational aesthetics

Computationally calculated visual attributes have been demonstrated to predict a wide range of outcomes, such as images' aesthetic appeal, popularity on social media, and interestingness. In this repository, you can find Python codes to calculate a variety of visual attributes, such as brightness, contrast, colorfulness, color variety, percentages of different colors, and visual complexity.

If you find this repository useful and use some codes in your work, please cite the following articles.
* Peng, Y., & Jemmott III, J. B. (2018). Feast for the eyes: Effects of food Perceptions and computer vision features on food photo popularity. [PDF](https://ijoc.org/index.php/ijoc/article/view/6678)
* Peng, Y. (2018). Same candidates, different faces: Uncovering media bias in visual portrayals of presidential candidates with computer vision. [PDF](https://www.researchgate.net/profile/Yilang_Peng2/publication/328005872_Same_Candidates_Different_Faces_Uncovering_Media_Bias_in_Visual_Portrayals_of_Presidential_Candidates_with_Computer_Vision/links/5bb9a125a6fdcc9552d50673/Same-Candidates-Different-Faces-Uncovering-Media-Bias-in-Visual-Portrayals-of-Presidential-Candidates-with-Computer-Vision.pdf)

## How to use
1. Install the following packages
* Pillow
* numpy
* opencv
* scikit-image (for segment.py)

2. Create folders
* img all: place the images you want to process inside this folder. Please convert all your images to .jpg format first. You can also use preprocess.py to resize large pictures.
* img transform: this folder saves the transformed versions (e.g., edge detection)
* img result: this folder saves results in .txt files.

3. Run the following Python script

## basic.py
This script calculates basic visual attributes, including:
* filesize: the file size of the image. This can be used as an indicator of visual complexity.
* w, h: width and height of the image (in pixels).
* ar, size: aspect ratio (w/h) and image size (w*h).
* rgbR, rgbG, rgbB, rgbR_sd, rgbG_sd, rgbB_sd: means and standard deviations of R, G, B values.
* hue, saturation, value, hue_sd, saturation_sd, value_sd: means and standard deviations of H, S, V values.
* xyzX, xyzY, xyzZ, xyzX_sd, xyzY_sd, xyzZ_sd: means and standard deviations of X, Y, Z values. Y is an indicator of luminance.
* bright, bright_sd: mean and standard deviation of brightness
* contrast: contrast. The script finds a range in the brightness histogram that covers 95% of the mass of the histogram.
* colorful: colorfulness [(Hasler & Suesstrunk, 2003)](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/5007/0000/Measuring-colorfulness-in-natural-images/10.1117/12.477378.short?SSO=1)
* hue_count: hue count, an indicator of color variety or visual complexity [(Ke et al., 2006)](https://ieeexplore.ieee.org/abstract/document/1640788)

## colorname.py
This script assigns each RGB value into one of the eleven basic colors (black, blue, brown, gray, green, orange, pink, purple, red, white, yellow) based on a dataset in [(Van De Weijer et al., 2009)](https://ieeexplore.ieee.org/abstract/document/4270243). It calculates the percentages of these basic colors and creates a PNG file that illustrates the assigned colors.

### example
<p float="left">
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20all/Philadelphia7.jpg" width="400" />
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20transform/colorname/Philadelphia7.png" width="400" /> 
</p>

<p float="left">
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20all/Chefchaouen1.jpg" width="400" />
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20transform/colorname/Chefchaouen1.png" width="400" /> 
</p>

## edge.py
This script detects edges in images and calculates edge-related visual attributes. It also creates a PNG file that stores the edges.
* edensity: edge density, calculated as the area occupied by edge points. This attribute is an indicator of visual complexity.
* edist: edge distribution, calculated as the average distance between two edge points among all pairs of edge points. This attribute is an indicator of visual complexity. To speed up calculations, this script randomly selects 1000 edge points, but you can change this setting in the script.

### example
<p float="left">
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20all/Barcelona1.jpg" width="400" />
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20transform/edge%20canny/Barcelona1.png" width="400" /> 
</p>

<p float="left">
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20all/Bagan1.jpg" width="400" />
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20transform/edge%20canny/Bagan1.png" width="400" /> 
</p>

## box.py
This script finds a box that contains at least 95% of values in a grayscale image and creates a PNG file that shows the box. The grayscale image can be an edge map or a saliency map. 
* minsize_percent: the size of the bounding box, divided by the image size. It can be an indicator of visual complexity.
<p float="left">
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20all/Essaouira1.jpg" width="400" />
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20transform/box%20edge%20canny/Essaouira1.png" width="400" /> 
</p>

<p float="left">
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20all/Suzhou2.jpg" width="400" />
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20transform/box%20edge%20canny/Suzhou2.png" width="400" /> 
</p>

## segment.py
This script conducts image segmentation using two methods in scikit-image: quickshit and normalized cut. It then calculates the number of segments and the sizes of the top three largest segments.
* nseg: number of segments, which can be an indicator of visual complexity.
* nseg_l: number of segments that are larger than a threshold (5% of the image area)
* size0, size1, size2: the size of the largest, the second largest, and the third largest segment.

<p float="left">
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20all/Yellowknife1.jpg" width="400" />
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20transform/segment%20normalized_cut/Yellowknife1 ava.png" width="400" /> 
</p>

<p float="left">
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20all/Cordoba1.jpg" width="400" />
  <img src="https://github.com/lithiumfortytwo/computational-aesthetics/blob/master/img%20transform/segment%20normalized_cut/Cordoba1 ava.png" width="400" /> 
</p>

## preprocess.py
This script conducts some preprocessing of the data. It converts still PNG and GIF files to JPG format and resizes large images.

Note: Images in this repository are copyrighted (I take many photos when I am not doing research). Please contact me if you need to use them for other purposes.
