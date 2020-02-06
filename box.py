import os, glob, cv2, random
import numpy as np
from PIL import Image, ImageDraw
import ypoften as of

def size_of_box(box):
    x1, y1, x2, y2 = box
    return (x2-x1+1)*(y2-y1+1)

def value_of_box(box, table):
    x1, y1, x2, y2 = box
    return table[x2,y2] + table[x1,y1] - table[x2,y1] - table[x1,y2]

# get a box that contains a certain percentage of all values
def find_save_box(bw, drimgsavepath, m = 0.95, savetf = True, k = 1): # k interval for checking pixels
    nrow, ncol = bw.shape
    # first create a summed-area table
    table = np.zeros((nrow,ncol), dtype=np.int)  # create an empty table
    table[0,0] = bw[0,0]
    for y in range(1,ncol): # for points x = 0
        table[0,y] = bw[0,y] + table[0,y-1]
    for x in range(1,nrow): # for points y = 0
        table[x,0] = bw[x,0] + table[x-1,0]
    for x in range(1,nrow):
        for y in range(1,ncol):
            table[x,y] = bw[x,y] - table[x-1,y-1] + table[x,y-1] + table[x-1,y]

    total = table[nrow-1, ncol-1]
    if total > 0:
        minvalue = int(total * m) # contain at least this value
        print("threshold", total, m, minvalue)
    
        minbox = [0, 0, nrow-1, ncol-1]  # create the bounding box, starting from the whole image
        minsize = nrow*ncol  # stores value for the size of the bounding box
    
        for x1 in range(0, nrow):    # now search for the minimal bounding box that contains minvalue
            min_x2 = nrow
            while value_of_box((x1, 0, min_x2-1, ncol - 1), table) >= minvalue:
                min_x2 = min_x2 - 1
            if min_x2 == nrow: break
            for x2 in range(min_x2, nrow):
                y2 = ncol - 1
                while value_of_box( (x1, 0, x2, y2 - 1), table ) >= minvalue:
                    y2 = y2 - 1
                for y1 in range(0, ncol):
                    while value_of_box( (x1, y1, x2, y2), table) < minvalue:
                        y2 = y2 + 1
                        if y2 == ncol: break;
                    if y2 == ncol: break
                    current_box = (x1, y1, x2, y2)
                    if size_of_box(current_box) <= minsize:
                        minbox = [x1, y1, x2, y2]
                        minsize = size_of_box(minbox)
    
        minsize_percent = minsize/(nrow*ncol)
        
        if savetf:
            drimg = cv2.cvtColor(bw, cv2.COLOR_GRAY2BGR)
            drimg = cv2.rectangle(drimg,(minbox[1], minbox[0]),(minbox[3], minbox[2]),(0,204,255),4)
            # OpenCV uses x, y coordinates similar to PIL (but "coordinates" in arrays are reversed)
            # top-left corner and bottom-right corner of rectangle, color, line width
            # (0,204,255) is color orange; note OpenCV default is BGR space, so B & G are swapped; 
            of.create_path(drimgsavepath)
            cv2.imwrite(drimgsavepath, drimg) # save image
    else:
        minsize_percent = -99999
        minbox = -99999
        if savetf:
            drimg = cv2.cvtColor(bw, cv2.COLOR_GRAY2BGR)
            of.create_path(drimgsavepath)
            cv2.imwrite(drimgsavepath, drimg)
    print("bounding box", minbox, minsize_percent)
    return([minbox, minsize_percent])

def attr_box(imgpath, tffolder, tfmethod = 'edge canny', m = 0.95, savetf = True):
    imgname = os.path.basename(imgpath)
    tfpath = os.path.join(tffolder, tfmethod, imgname.replace('.jpg','.png'))
    bw = cv2.imread(tfpath, 0) # load the image
    drimgsavepath = os.path.join(tffolder, 'box ' + tfmethod, imgname.replace('.jpg','.png'))
    box_list = find_save_box(bw, drimgsavepath, m = m, savetf = savetf)
    return(box_list)

def main():
    imgfolder = os.path.join('img all','')
    tffolder = os.path.join("img transform",'')
    resultpath = os.path.join('img result', 'box.txt')
    imgpaths = glob.glob(imgfolder + '*')

    for j, imgpath in enumerate(imgpaths[:]):
        print("-"*100)
        imgname = os.path.basename(imgpath)
        print(j, imgname)
        wlist = [imgname] + attr_box(imgpath, tffolder)
        of.save_list_to_txt(wlist, resultpath)
    print("DONE"*50)

if __name__== "__main__":
    main()
