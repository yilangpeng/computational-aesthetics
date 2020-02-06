import os, shutil

def create_path(filepath):
    filepathfolder = os.path.dirname(filepath) 
    if not os.path.exists(filepathfolder): os.makedirs(filepathfolder)

def copy_file(filepath1, filepath2):
    filepathfolder2 = os.path.dirname(filepath2) 
    if not os.path.exists(filepathfolder2): os.makedirs(filepathfolder2)
    shutil.copy2(filepath1, filepath2)

def save_list_to_txt(wlist, filesavepath):
    create_path(filesavepath)
    slist = [str(x) for x in wlist]
    jlist = '\t'.join(slist)
    with open(filesavepath, "a") as resultf:
        resultf.write(jlist + '\n')
