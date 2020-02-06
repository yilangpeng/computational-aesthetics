import os, glob, cv2, sys
import numpy as np
import ypoften as of

def attr_basic(imgpath, contrast_range=0.95, hue_count_alpha = 0.05):
    img = cv2.imread(imgpath) # note: OpenCV uses BGR space
    filesize = os.path.getsize(imgpath) # file size
    h, w = img.shape[:2] # width, height
    ar = w/h; size = w*h # aspect ratio, image size
    print("file size, height, width, aspect ratio, size",filesize, h, w, ar, size)

    # RGB
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    rgbR, rgbG, rgbB = np.mean(rgb, axis = (0,1))
    rgbR_sd, rgbG_sd, rgbB_sd = np.std(rgb, axis = (0,1))
    print("RGB (means & SDs)", rgbR, rgbG, rgbB, rgbR_sd, rgbG_sd, rgbB_sd)

    # HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue, saturation, value = np.mean(hsv, axis = (0,1))
    hue_sd, saturation_sd, value_sd = np.std(hsv, axis = (0,1)) 
    print("HSV (means & SDs)", hue, saturation, value, hue_sd, saturation_sd, value_sd)

    # XYZ
    xyz = cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)
    xyzX, xyzY, xyzZ = np.mean(xyz, axis = (0,1)) 
    xyzX_sd, xyzY_sd, xyzZ_sd = np.std(xyz, axis = (0,1)) 
    print("XYZ (means & SDs)", xyzX, xyzY, xyzZ, xyzX_sd, xyzY_sd, xyzZ_sd)

    # brightness
    gray = cv2.imread(imgpath, 0)
    bright = np.mean(gray) # brightness
    bright_sd = np.std(gray)

    # contrast
    hist = np.bincount(gray.ravel(),minlength=256) # create a histogram of brightness values
    sum = np.sum(hist) # get sum of the histogram
    p = (1 - contrast_range)/2;  q = (1 + contrast_range)/2
    low_sum = sum * p; high_sum = sum * q
    cumsum = np.cumsum(hist)
    low_idx = (np.abs( cumsum - low_sum )).argmin() # find a range that covers (q-p) percent of the histogram
    high_idx = (np.abs( cumsum - high_sum )).argmin()
    contrast = high_idx - low_idx
    print("brightness, brightness (SD), contrast", bright, bright_sd, contrast)
    
    # colorfulness
    rgb = rgb.astype(float) # OpenCV reads image in unit8 (range 0-255), so first converts to float
    l_rgbR, l_rgbG, l_rgbB = cv2.split(rgb) # get lists of R, G, B values
    l_rg = l_rgbR - l_rgbG
    l_yb = 0.5*l_rgbR  + 0.5*l_rgbG - l_rgbB
    rg_sd  = np.std(l_rg); rg_mean = np.mean(l_rg)
    yb_sd  = np.std(l_yb); yb_mean = np.mean(l_yb)
    rg_yb_sd = (rg_sd**2 + yb_sd**2)**0.5
    rg_yb_mean = (rg_mean**2 + yb_mean**2)**0.5
    colorful = rg_yb_sd + (rg_yb_mean * 0.3)
    print("colorfulness", colorful)

    # color variety
    h, w, m = hsv.shape[:3]
    hsv_l = hsv.reshape(h*w, m) # reshape to a "list" of HSV values
    hsv_g = hsv_l[(hsv_l[:,1] >= 255*0.2) & (hsv_l[:,2] >= 255*0.15) & (hsv_l[:,2] <= 255*0.95)]
    # select only "good" hue values: saturation > 0.2; 0.15 < lightness < 0.95
    # note: H ranges from 0 to 180, S and V from 0 to 255
 
    hgood = hsv_g[:,0] # get all good hue values in a 1-D array
    if len(hgood) > 0: 
        bins = np.linspace(0, 180, 20, endpoint=False) # create 20 bins on H value
        # note: np.linspace returns evenly spaced numbers over a specified interval
        digitized = np.digitize(hgood, bins)
        # return the indices of the bins to which each hue value belongs
        digitized = digitized - 1 # minus 1 since digitized bin index starts from 1 
        bin_ns = [len(digitized[digitized == i]) for i in range(0, len(bins))] # count pixels in each bin
        bin_ns = np.array(bin_ns)
        count_indexes = np.where(bin_ns > hue_count_alpha * max(bin_ns))[0] 
        # get "countable" bins larger than the threshold (=alpha * the largest bin)
        hue_count = len(count_indexes) # get hue count
    else:
        hue_count = 0
    print("color variety", hue_count)

    attrlist = [filesize, w, h, ar, size,
                rgbR, rgbG, rgbB, rgbR_sd, rgbG_sd, rgbB_sd, 
                hue, saturation, value, hue_sd, saturation_sd, value_sd,
                xyzX, xyzY, xyzZ, xyzX_sd, xyzY_sd, xyzZ_sd,
                bright, bright_sd, contrast, colorful, hue_count]

    print("basic attributes", attrlist)
    return(attrlist)

def main():
    imgfolder = os.path.join('img all','')
    tffolder = os.path.join("img transform",'')
    resultpath = os.path.join('img result', 'basic.txt')
    imgpaths = glob.glob(imgfolder + '*')

    for j, imgpath in enumerate(imgpaths[:]):
        print("-"*100)
        imgname = os.path.basename(imgpath)
        print(j, imgname)
        wlist = [imgname] + attr_basic(imgpath)
        of.save_list_to_txt(wlist, resultpath)
    print("DONE"*50)

if __name__== "__main__":
    main()
