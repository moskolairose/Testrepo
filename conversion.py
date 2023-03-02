import cv2, os
base_path = "/media/rose/ESi207/Bresil_AOI/Stack_data/tiff/"
new_path = "/media/rose/ESi207/tiff_to_jpeg/"
for infile in os.listdir(base_path):
    print ("file : " + infile)
    read = cv2.imread(base_path + infile)
    outfile = infile.split('.')[0] + '.jpg'
    cv2.imwrite(new_path+outfile,read,[int(cv2.IMWRITE_JPEG_QUALITY), 200])

