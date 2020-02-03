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
* Percentages of eleven basic colors: red, orange, yellow, green, blue, pink, purple, brown, gray, black, white
* Color variety

## Composition-related attributes
* Height
* Width
* Size
* Aspect ratio
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
This file caculates the following visual attributes:
* filesize: the filesize of the image. Can be used as an indicator of visual complexity.
* w, h: width and height of the image (in pixels).
* ar, size: aspect ratio & image size
* rgbR, rgbG, rgbB, rgbR_sd, rgbG_sd, rgbB_sd: means and standard deviations of R, G, B values
* hue, saturation, value, hue_sd, saturation_sd, value_sd: means and standard deviations of H, S, V values
* xyzX, xyzY, xyzZ, xyzX_sd, xyzY_sd, xyzZ_sd: : means and standard deviations of X, Y, Z values. Y can be an indicator of percevied luminance
* bright, bright_sd: mean and standard deviation of brightness
* contrast: finds a range that covers 95% of the mass of the brightess histogram
* colorful: colorfulness
* hue_count: color variety

## References
Please cite the following articles:
* Peng, Y., & Jemmott III, J. B. (2018). Feast for the eyes: Effects of food Perceptions and computer vision features on food photo popularity. International Journal of Communication, 12: 313–336 [PDF](https://ijoc.org/index.php/ijoc/article/view/6678)
* Peng, Y. (2018). Same candidates, different faces: Uncovering media bias in visual portrayals of presidential candidates with computer vision. Journal of Communication, 68(5): 920-941. [PDF](https://www.researchgate.net/profile/Yilang_Peng2/publication/328005872_Same_Candidates_Different_Faces_Uncovering_Media_Bias_in_Visual_Portrayals_of_Presidential_Candidates_with_Computer_Vision/links/5bb9a125a6fdcc9552d50673/Same-Candidates-Different-Faces-Uncovering-Media-Bias-in-Visual-Portrayals-of-Presidential-Candidates-with-Computer-Vision.pdf)
