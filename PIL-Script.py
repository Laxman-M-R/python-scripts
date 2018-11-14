import os
import shutil
import PIL

root_src_dir = os.path.join('.',r'Images\Directory\Path\Here')

operation = 'move' # 'copy' or 'move'

ext = ('jpg', 'jpeg', 'png', 'tiff', 'JPG')

for src_dir, dirs, files in os.walk(root_src_dir):
    for file in files:
        if file.endswith(ext):            
            im = PIL.Image.open(os.path.join(src_dir, file))
            # take image resolution by using PIL module
            wid, ht = im.size
            dir_name = str(wid) + ' X ' + str(ht)
            im.close()
            # create a directory named in the form htXwid if it does not exist
            if not os.path.exists(os.path.join(root_src_dir, dir_name)):
                dst_dir = os.path.join(root_src_dir, dir_name)
                os.mkdir(dst_dir)
            img_file = os.path.join(src_dir, file)
            dst_dir = os.path.join(root_src_dir, dir_name)
            # check whether the file is not yet copied or moved and then perform the required operaton
            if img_file != dst_dir:
                if operation is 'copy':        
                    shutil.copy(img_file, dst_dir)
                elif operation is 'move':
                    shutil.move(img_file, dst_dir)
            else:
                break
                


     
            
    

    