import os
from glob import glob
import time

# set up directories and working environment
odir = "D:\\SURGE\\GeoTiffs_Global_Daily_1981_2020\\p05_Nebraska_Clipped\\"
idir = "D:\\SURGE\\GeoTiffs_Global_Daily_1981_2020\\p05_uncompressed\\"
inMask = "D:\\SURGE\\Nebraska_clipped\\nebraska_wgs84.shp"

start = time.time()

# read files into list
filelist = [f for f in glob(idir+"**/*.tif")]
filelist.sort()
print(filelist)

# a loop for clipping
for files in filelist:
    print(files)
    filename = os.path.basename(files)
    newname = 'Nebraska_pcp_'+ filename.split('.')[2] + filename.split('.')[3] +\
                filename.split('.')[4]+'.tif'
    outputfile = odir+newname
    cmd = 'gdalwarp -dstnodata -9999 -q\
            -cutline %s -crop_to_cutline %s %s'\
            % (inMask, files, outputfile)           # the command line to clip the raster
    os.system(cmd)
    print(newname+' is done.')
end = time.time()

print('The process took %.2f minutes.' % ((end-start)/60))
