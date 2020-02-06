import os, glob, cv2
import ypoften as of

def save_resize(imgpath, tffolder, maxw=-99, maxh=-99, maxside=-99, maxsize=-99):
    img = cv2.imread(imgpath, cv2.IMREAD_UNCHANGED)
    ofilesize = os.path.getsize(imgpath)
    if img is None:
        print("image format is not supported")
        return(None)
    elif img.ndim == 2:
        img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    elif img.ndim == 3: 
        h, w, nc = img.shape[:3]
        if nc == 4:
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        elif nc != 3:
            print("image format is not supported")
            return(None)
    else:
        print("image format is not supported")
        return(None)

    img.astype("uint8")
    h, w = img.shape[:2]
    oh, ow = img.shape[:2]
    ar = w/h
    if maxside > 0:  # resize base on maximum side
        if w > h:
            if w > maxside:
                w = maxside
                h = w/ar
        else:
            if h > maxside:
                h = maxside
                w = h * ar
    if maxw > 0: # resize base on maximum width
        if w > maxw:
            w = maxw
            h = w/ar
    if maxh > 0: # resize base on maximum height
        if h > maxh:
            h = maxh
            w = h * ar
    if maxsize > 0: # resize base on maximum size
        if w*h > maxsize:
            h = (maxsize/ar) ** 0.5
            w = (maxsize*ar) ** 0.5
    w = int(w+0.5); h = int(h+0.5)
    resized = cv2.resize(img, (w, h), interpolation = cv2.INTER_AREA)

    imgname = os.path.basename(imgpath)
    imgsavepath = os.path.join(tffolder, 'resize', os.path.splitext(imgname)[0] + '.jpg')
    of.create_path(imgsavepath) 
    cv2.imwrite(imgsavepath, resized)
    rlist = [ofilesize, ow, oh, w, h]
    print('original file size',ofilesize)
    print('original height & width',ow,oh)
    print('resized height & width',w,h)
    return(rlist)

def main():
    imgfolder = os.path.join('img all','')
    tffolder = os.path.join("img transform",'')
    resultpath = os.path.join('img result', 'preprocess.txt')
    imgpaths = glob.glob(imgfolder + '*')

    for j, imgpath in enumerate(imgpaths[:]):
        print("-"*100)
        imgname = os.path.basename(imgpath) 
        print(j, imgname)
        rlist = save_resize(imgpath, tffolder, maxside = 300)
        wlist = [imgname] + rlist[:]
        of.save_list_to_txt(wlist, resultpath)
    print("DONE"*50)

if __name__== "__main__":
    main()