from glob import glob
from PIL import Image
from zipfile import ZipFile
from os import path
from shutil import rmtree

def unzip(path):
    with ZipFile(path, 'r') as zipObj:
        zipObj.extractall('./stich_temp')

def merge_images(dir):
    images = glob(dir + "/*.png")
    
    total_width = 0
    total_height = 0
    max_width = 0
    max_height = 0
    ix =[]

    for image in images:
        with open(image, 'rb') as file:
                im = Image.open(file)
                im.load()
                size = im.size
                w = size[0]
                h = size[1]
                total_width += w 
                total_height += h
    
                if h > max_height:
                    max_height = h
                if w > max_width:
                    max_width = w
                ix.append(im) 

    final_image = Image.new('RGB', (max_width, total_height))

    pre_w = 0
    pre_h = 0
    for img in ix:
        final_image.paste(img, (pre_w, pre_h, pre_w+max_width, pre_h + img.size[1]))
        pre_h += img.size[1]
    
    final_image.save('stiched.png', quality=100)
    final_image.show()

    if path.exists(path.abspath('./stich_temp')):
        rmtree(path.abspath('./stich_temp'))

def main():
    image_dir = input("What directory to you want to get the images from?: ")

    if image_dir.endswith('.zip'):
        unzip(image_dir)
        image_dir = path.abspath('./stich_temp') + "/" + path.basename(image_dir).split('.')[0]

    merge_images(image_dir)

if __name__ == '__main__':
    main()