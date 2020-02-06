import os, glob
import numpy as np
from skimage import io, color, segmentation, measure, filters 
from skimage.future import graph
import ypoften as of

# get count from a label array from image segmentation algorithms
def count_from_label(label, m = 0.05):
    h, w = label.shape
    values, n_seg = measure.label(label, background=99999, return_num=True) # by default 0-valued pixels are considered as background, so set background value to 99999
    unique_counts = np.unique(values,return_counts=True)
    counts = unique_counts[1] # first array is label value, second array is count
    counts = np.flip(np.sort(counts)) # sort in a decreasing order
    nseg = len(counts) # number of segments   
    nseg_l = np.count_nonzero(counts >= (w*h*m) ) # number of segments larger than 5%
    size0 = counts[0]/(w*h) # size of the largest segment
    size1 = counts[1]/(w*h) if len(counts) > 1 else 0 # size of the second largest segment
    size2 = counts[2]/(w*h) if len(counts) > 2 else 0  # size of the third largest segment
    rlist = [nseg, nseg_l, size0, size1, size2]
    print('Segmentation',rlist)
    return(rlist)

# save label to a color image that preserves the label values and images for illustration
def save_label(imgpath, tffolder, label, tfmethod):
    img = io.imread(imgpath); imgname = os.path.basename(imgpath)
    label_new, n_label = measure.label(label, background=99999, return_num=True)
    label_new = label_new.astype('int16')

    npypath = os.path.join(tffolder, tfmethod, os.path.splitext(imgname)[0]+'.npy')
    of.create_path(npypath)
    np.save(npypath, label_new)
    
    img_tosave = color.label2rgb(label_new, img, kind='overlay')
    imgsavepath = os.path.join(tffolder, tfmethod, os.path.splitext(imgname)[0]+' overlay.png')
    of.create_path(imgsavepath)
    io.imsave(imgsavepath, img_tosave)

    img_tosave = color.label2rgb(label_new, img, kind='ava')
    imgsavepath = os.path.join(tffolder, tfmethod, os.path.splitext(imgname)[0]+' ava.png')
    of.create_path(imgsavepath)
    io.imsave(imgsavepath, img_tosave)

def tf_seg_quickshift(imgpath, tffolder, ratio=1, kernel_siz=10, max_dist=200):
    img = io.imread(imgpath)
    label = segmentation.quickshift(img, ratio=ratio, kernel_size=kernel_siz, max_dist=max_dist)    
    # https://scikit-image.org/docs/dev/api/skimage.segmentation.html
    save_label(imgpath, tffolder, label, "segment quickshift")
    return(label)

def tf_seg_normalized_cut(imgpath, tffolder, n_segments=400, compactness=1, sigma=100):
    img = io.imread(imgpath)
    label_km = segmentation.slic(img, n_segments=n_segments, compactness=compactness)
    g = graph.rag_mean_color(img, label_km, mode='similarity', sigma=sigma)  # create the region adjacency graph
    # sigma controls color similarity, higher, more similar, fewer regions
    label = graph.cut_normalized(label_km, g)
    save_label(imgpath, tffolder, label, "segment normalized_cut")    
    return(label)

def main():
    imgfolder = os.path.join('img all','')
    tffolder = os.path.join("img transform",'')
    resultpath = os.path.join('img result', 'segment.txt')
    imgpaths = glob.glob(imgfolder + '*')

    for j, imgpath in enumerate(imgpaths[20:]):
        print("-"*100)
        imgname = os.path.basename(imgpath)
        print(j, imgname)
        wlist = [imgname]

        label = tf_seg_quickshift(imgpath, tffolder)
        rlist = count_from_label(label)
        wlist = wlist[:] + rlist[:]

        label = tf_seg_normalized_cut(imgpath, tffolder)
        count_from_label(label)
        wlist = wlist[:] + rlist[:]
        of.save_list_to_txt(wlist, resultpath)
    print("DONE"*50)

if __name__== "__main__":
    main()