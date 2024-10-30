from os import name
from PIL import Image
import PIL


def trim_left(img):
    same = True
    x = 0
    while same:
        pix = img.getpixel((0, 0))
        for y in range(img.size[1]):
            if pix != img.getpixel((0, y)):
                same = False
                break
        if same:
            img = img.crop((1, 0, img.size[0], img.size[1]))
    return img


def trim_right(img):
    same = True
    x = 0
    while same:
        pix = img.getpixel((img.size[0] - 1, 0))
        for y in range(img.size[1]):
            if pix != img.getpixel((img.size[0] - 1, y)):
                same = False
                break
        if same:
            img = img.crop((0, 0, img.size[0] - 1, img.size[1]))
    return img


def concat_img(img1, img2):
    img1 = trim_left(img1)
    img1 = trim_right(img1)
    img2 = trim_left(img2)
    img2 = trim_right(img2)

    img = Image.new("RGB", (img1.size[0] + img2.size[0], img1.size[1]))
    img.paste(img1, (0, 0))
    img.paste(img2, (img1.size[0], 0))
    return img


def save_img(img1, img2, name):
    img = concat_img(img1, img2)
    img.save(name)


img1 = Image.open("./campusmap/campusmap-04.png")
img2 = Image.open("./campusmap/campusmap-05.png")
name = "./page/mapdata_1.png"
save_img(img1, img2, name)
img1 = Image.open("./campusmap/campusmap-06.png")
img2 = Image.open("./campusmap/campusmap-07.png")
name = "./page/mapdata_2.png"
save_img(img1, img2, name)
img1 = Image.open("./campusmap/campusmap-08.png")
img2 = Image.open("./campusmap/campusmap-09.png")
name = "./page/mapdata_3.png"
save_img(img1, img2, name)
img1 = Image.open("./campusmap/campusmap-10.png")
img2 = Image.open("./campusmap/campusmap-11.png")
name = "./page/mapdata_4.png"
save_img(img1, img2, name)
img1 = Image.open("./campusmap/campusmap-12.png")
img2 = Image.open("./campusmap/campusmap-13.png")
name = "./page/mapdata_5.png"
save_img(img1, img2, name)
img1 = Image.open("./campusmap/campusmap-14.png")
img2 = Image.open("./campusmap/campusmap-15.png")
name = "./page/mapdata_6.png"
save_img(img1, img2, name)
