import os
from PIL import Image
from PIL.ExifTags import TAGS


###################################################################
## ---------------CHANGE THIS----------------- ##

dir_path = 'C:\\Users\\ishaq.idris\\Pictures\\test' #change to required directory 
img_type = 'jpg'#note only looking for files with this file extension

###################################################################

files = os.listdir(dir_path + '\\')
for jpg_file in files:
    if jpg_file.endswith(img_type): 
        im = Image.open(dir_path + '\\' + jpg_file)
        date = im._getexif()[36867]
        formatted_date = date.replace(":", "_").replace(" ", "_")
        print formatted_date
        im.close()
        print os.path.basename(dir_path)
        print dir_path
        os.rename(dir_path + '\\' + jpg_file, dir_path + '\\' + formatted_date + "_" + os.path.basename(dir_path) + ".jpg")
        
