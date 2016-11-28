import numpy as np
from scipy import misc, ndimage
from PIL import Image
import shutil

def denoise(im):
    '''
    Input: takes in image data array
    Returns: image data array, with gaussian denoising applied
    '''
    noisy = im + 0.4 * im.std() * np.random.random(im.shape)
    return ndimage.gaussian_filter(noisy,2)

# TOP TEN PERCENT
# files = ["AutoGrab001","AutoGrab009","AutoGrab016","AutoGrab020","AutoGrab031","AutoGrab032","AutoGrab034","AutoGrab037","AutoGrab038","AutoGrab042","AutoGrab045","AutoGrab055","AutoGrab070","AutoGrab071","AutoGrab081","AutoGrab091","AutoGrab092","AutoGrab096","AutoGrab097","AutoGrab100","AutoGrab1001","AutoGrab1026","AutoGrab104","AutoGrab1043","AutoGrab1048","AutoGrab105","AutoGrab106","AutoGrab111","AutoGrab118","AutoGrab126","AutoGrab131","AutoGrab135","AutoGrab137","AutoGrab155","AutoGrab178","AutoGrab182","AutoGrab218","AutoGrab221","AutoGrab230","AutoGrab235","AutoGrab246","AutoGrab248","AutoGrab250","AutoGrab273","AutoGrab279","AutoGrab282","AutoGrab290","AutoGrab295","AutoGrab298","AutoGrab299","AutoGrab302","AutoGrab310","AutoGrab316","AutoGrab334","AutoGrab343","AutoGrab345","AutoGrab347","AutoGrab366","AutoGrab369","AutoGrab370","AutoGrab372","AutoGrab405","AutoGrab472","AutoGrab475","AutoGrab485","AutoGrab494","AutoGrab495","AutoGrab498","AutoGrab504","AutoGrab511","AutoGrab512","AutoGrab513","AutoGrab518","AutoGrab520","AutoGrab522","AutoGrab524","AutoGrab533","AutoGrab534","AutoGrab536","AutoGrab538","AutoGrab540","AutoGrab545","AutoGrab546","AutoGrab547","AutoGrab590","AutoGrab599","AutoGrab612","AutoGrab615","AutoGrab616","AutoGrab626","AutoGrab633","AutoGrab635","AutoGrab646","AutoGrab650","AutoGrab651","AutoGrab658","AutoGrab662","AutoGrab668","AutoGrab671","AutoGrab679","AutoGrab708","AutoGrab760","AutoGrab774","AutoGrab825","AutoGrab842","AutoGrab853","AutoGrab857","AutoGrab867","AutoGrab868","AutoGrab884","AutoGrab944","AutoGrab002"]

# BOTTOM TEN PERCENT
files = ["AutoGrab463","AutoGrab468","AutoGrab467","AutoGrab466","AutoGrab464","AutoGrab1101","AutoGrab459","AutoGrab457","AutoGrab452","AutoGrab456","AutoGrab449","AutoGrab460","AutoGrab1099","AutoGrab455","AutoGrab458","AutoGrab454","AutoGrab986","AutoGrab450","AutoGrab1042","AutoGrab921","AutoGrab451","AutoGrab958","AutoGrab932","AutoGrab1100","AutoGrab1097","AutoGrab1081","AutoGrab934","AutoGrab1033","AutoGrab1032","AutoGrab465","AutoGrab994","AutoGrab983","AutoGrab790","AutoGrab1017","AutoGrab832","AutoGrab1091","AutoGrab1090","AutoGrab968","AutoGrab930","AutoGrab1098","AutoGrab972","AutoGrab898","AutoGrab920","AutoGrab572","AutoGrab741","AutoGrab712","AutoGrab987","AutoGrab426","AutoGrab440","AutoGrab900","AutoGrab953","AutoGrab1023","AutoGrab936","AutoGrab447","AutoGrab1084","AutoGrab551","AutoGrab749","AutoGrab726","AutoGrab904","AutoGrab589","AutoGrab933","AutoGrab911","AutoGrab905","AutoGrab776","AutoGrab448","AutoGrab964","AutoGrab963","AutoGrab1015","AutoGrab469","AutoGrab813","AutoGrab462","AutoGrab1039","AutoGrab952","AutoGrab924","AutoGrab061","AutoGrab1014","AutoGrab744","AutoGrab506","AutoGrab761","AutoGrab721","AutoGrab927","AutoGrab438","AutoGrab943","AutoGrab1096","AutoGrab746","AutoGrab800","AutoGrab168","AutoGrab1019","AutoGrab772","AutoGrab579","AutoGrab794","AutoGrab961","AutoGrab1093","AutoGrab1068","AutoGrab975","AutoGrab409","AutoGrab978","AutoGrab748","AutoGrab082","AutoGrab489"]

for file in files:
    print(file)
    src = "C:/Github/ASTRON-1263/data/cropped/" + file + ".fits.jpg"
    dst = "C:/Github/ASTRON-1263/data/closest/" + file + ".fits.jpg"
    shutil.copyfile(src, dst)

    dst_denoise = "C:/Github/ASTRON-1263/data/closest_denoise/" + file + ".fits.jpg"
    image_data = np.array(Image.open(dst))
    misc.imsave(dst_denoise, denoise(image_data))