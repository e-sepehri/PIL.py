from PIL import Image
from PIL import ImageDraw
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN)
from PIL import ImageFont
from PIL import ImageSequence


def image_rotation(image):
    print("print 1- for Turn Left "
          "      2- for Turn Right"
          "      3- for Transpose"
          "      4- Set yourself")
    u = int(input('Only numbers 1,2,3,4: '))
    if u == 1:
        im1 = image.rotate(-90, expand=1)
        im1.show()
    elif u == 2:
        im1 = image.rotate(90, expand=1)
        im1.show()
    elif u == 3:
        im1 = image.transpose(method=Image.FLIP_LEFT_RIGHT)
        im1.show()
    elif u == 4:
        x = int(input("Enter Number to rotate the image: "))
        im1 = image.rotate(x)
        im1.show()
    else:
        print('Invalid input...Try again.')


def image_crop(image):
    print('how do you want to crop?')
    print('print 1- for Left Cut')
    print('      2- for Center Cut')
    print('      3- for Right Cut')
    print('      4-(or any numbers) for set by yourself')
    x = int(input('Numbers 1,2,3,4 :'))
    if x == 1:
        im1 = image.crop((0, 0, im.width//2, im.height))
        im1.show()
    elif x == 2:
        im2 = image.crop((im.width//4, im.height//4, im.width*0.75, im.height*0.75))
        im2.show()
    elif x == 3:
        im3 = image.crop((im.width//2, 0, im.width, im.height))
        im3.show()
    else:
        print('Size of your image:', image.size)
        left = int(input('How much to cut from the Left? '))
        top = int(input('How much to cut from the Top? '))
        right = int(input('How much to cut from the Right? '))
        bottom = int(input('How much to cut from the Bottom? '))
        im1 = image.crop((left, top, right, bottom))
        im1.show()


def image_resize(image):
    print('Print 1:Resize or 2:Reduce??')
    x = input('... ')
    x = x.lower()
    if x == 'resize' or x == '1':
        w = int(input('Enter Width>>'))
        h = int(input('Enter height>>'))
        resized_im = image.resize((w, h))
        return resized_im.show()
    elif x == 'reduce' or x == '2':
        p = int(input('Enter the reduction percentage: '))
        im1 = image.reduce(p)
        return im1.show()
        # im1.save('C:/Users/Shahram/Desktop/1.jpg')
    else:
        print('Invalid input')


def image_resolution(image):
    x = int(input("Enter the quality number: "))
    image.save("C:/Users/Shahram/Desktop/new.jpg", quality=x)
    im1 = Image.open("C:/Users/Shahram/Desktop/new.jpg")
    im1.show()


def watermark_addition(image):
    draw = ImageDraw.Draw(image)
    black = (0, 0, 0)
    txt = input('Write the text: ')
    print('Enter x & y parameters as position:')
    x1 = int(input("x= "))
    y1 = int(input("y= "))
    fontsize = int(input("font's size: "))
    pos = (x1, y1)
    font = ImageFont.truetype("Naylime-Font_soha-li.ir.ttf", fontsize)
    draw.text(pos, txt, fill=black, font=font)
    return image.show()


def photo_addition(image):
    path = input('watermark image path:')
    im1 = Image.open(path)
    p = int(input('Enter the reduction percentage: '))
    watermark_photo = im1.reduce(p)
    print('Enter x & y parameters as position:')
    x, y = int(input("x= ")), int(input("y= "))
    image.paste(watermark_photo, (x, y))
    image.show()


def collage():
    clg = Image.new("RGBA", (1500, 1500), color=(255, 255, 255, 255))
    ls = [100, 200, 300, 400, 500, 600, 700, 800, 900]

    n = 0
    for i in range(0, 1500, 500):
        for j in range(0, 1500, 500):
            file = "C:/Users/Shahram/Desktop/" + str(ls[n]) + ".jpg"
            im1 = Image.open(file).convert("RGBA")
            im1 = im1.resize((500, 500))
            clg.paste(im1, (i, j))
            n += 1

    clg.show()
    print("do you want add a watermark?")
    x = input("y|n: ")
    if x == 'y':
        result = watermark_addition(clg)
        result.show()
    elif x == 'n':
        pass
    else:
        print('Wrong input')


def color_layers_collage(image):
    clg = Image.new("RGBA", (1500, 1500), color=(0, 0, 0, 0))
    photo = image.convert("RGBA")
    photo = photo.resize((500, 500))
    for i in range(0, 1500, 500):
        rr = 00
        bb = 0
        gg = 150
        for j in range(0, 1500, 500):
            hue = Image.new("RGBA", (photo.size), color=(rr, gg, bb))
            new_img = Image.blend(photo, hue, 0.5)
            rr += 50
            bb += 50
            gg -= 50
            clg.paste(new_img, (i, j))
    clg.show()
    return clg


def blur(img):
    im1 = img.filter(BLUR)
    return im1


def edge_enhance(img):
    im1 = img.filter(EDGE_ENHANCE)
    return im1


def find_edge(img):
    im1 = img.filter(FIND_EDGES)
    return im1


def gray(img):
    gray_img = img.convert("L")
    return gray_img


def blue_merge(img):
    red, green, blue = img.split()
    im1 = Image.merge("RGB", (blue, green, red))
    return im1


def purple_merge(img):
    red, green, blue = img.split()
    im1 = Image.merge("RGB", (green, blue, green))
    return im1


def red_merge(img):
    red, green, blue = img.split()
    im1 = Image.merge("RGB", (red, blue, blue))
    return im1


def pink_merge(img):
    red, green, blue = img.split()
    im1 = Image.merge("RGB", (red, blue, green))
    return im1


def yellow_merge(img):
    red, green, blue = img.split()
    im1 = Image.merge("RGB", (red, red, blue))
    return im1


def image_filter(img):
    filter_list = Image.new("RGBA", (1500, 1500), color=(255, 255, 255, 255))
    image = img.resize((500, 500))
    a = blur(image)
    b = edge_enhance(image)
    c = find_edge(image)
    d = purple_merge(image)
    e = red_merge(image)
    f = blue_merge(image)
    g = pink_merge(image)
    h = yellow_merge(image)
    i = gray(image)
    lst = [a, b, c, d, e, f, g, h, i]
    n = 0
    for i in range(0, 1500, 500):
        for j in range(0, 1500, 500):
            filter_list.paste(lst[n], (i, j))
            n += 1

    draw = ImageDraw.Draw(filter_list)
    font = ImageFont.truetype('comic.ttf', 44)
    draw.text((0, 0), '1.Blurring', fill=(0, 0, 0), font=font)
    draw.text((0, 500), '2.Edge enhance', fill=(0, 0, 0), font=font)
    draw.text((0, 1000), '3.Find edge', fill=(255, 255, 255), font=font)
    draw.text((500, 0), '4.Purpling', fill=(0, 0, 0), font=font)
    draw.text((500, 500), '5.Reding', fill=(0, 0, 0), font=font)
    draw.text((500, 1000), '6.Bluing', fill=(0, 0, 0), font=font)
    draw.text((1000, 0), '7.Pinking', fill=(0, 0, 0), font=font)
    draw.text((1000, 500), '8.Yellowing', fill=(0, 0, 0), font=font)
    draw.text((1000, 1000), '9.Gray', fill=(0, 0, 0), font=font)
    filter_list.show()

    inx = input('Which one did you mean? ')
    x = inx.lower()
    if x == '1' or x == 'blur' or x == 'blurring':
        c = blur(img)
        c.show()
    elif x == '2' or x == 'edge enhance':
        c = edge_enhance(img)
        c.show()
    elif x == '3' or x == 'find edge':
        c = find_edge(img)
        c.show()
    elif x == '4' or x == 'purple':
        c = purple_merge(img)
        c.show()
    elif x == '5' or x == 'red' or x == 'reding':
        c = red_merge(img)
        c.show()
    elif x == '6' or x == 'bluing' or x == 'blue':
        c = blue_merge(img)
        c.show()
    elif x == '7' or x == 'pink' or x == 'pinking':
        c = purple_merge(img)
        c.show()
    elif x == '8' or x == 'yellow':
        c = yellow_merge(img)
        c.show()
    elif x == '9' or x == 'gray':
        c = gray(img)
        c.show()
    else:
        print("Sorry, I haven't that filter...")


def gif_maker():
    images = []
    for i in range(100, 1000, 100):
        images.append("C:/Users/Shahram/Desktop/" + str(i) + '.jpg')

    frames = []
    for i in images:
        new = Image.open(i)
        new_frame = new.resize((1200, 1200))
        frames.append(new_frame)

    frames[0].save('C:/Users/Shahram/Desktop/gif.gif',
                   format='GIF', append_images=frames[1:], save_all=True, duration=800, loop=0)


def sequence():
    path_gif = input('Enter the path: ')
    im = Image.open(path_gif)
    counter = 0
    for fr in ImageSequence.Iterator(im):
        fr.save('C:/Users/Shahram/Desktop/gifsq/fr%r.png'%counter)
        counter += 1


def rectangle_drawing(image):
    draw_rect = ImageDraw.Draw(image)
    draw_rect.rectangle((100, 100, 500, 500), fill=(255, 255, 255))
    image.show()


print('What changes do you want to make?')
print('>>> 1.Resize')
print('>>> 2.Crop')
print('>>> 3.Rotate')
print('>>> 4.adding photo')
print('>>> 5.adding text')
print('>>> 6.filter')
print('>>> 7.collage')
print('>>> 8.color layers collage')
print('>>> 9.gif')
print('>>> 10.gif sequence')
print('>>> 11.draw')
inp = input('--- ')
it = inp.lower()
try:
    if it == '1' or it == 'resize':
        path = input('Enter the path of image: ')
        im = Image.open(path)
        output = image_resize(im)
    elif it == '2' or it == 'crop':
        path = input('Enter the path of image: ')
        im = Image.open(path)
        output = image_crop(im)
    elif it == '3' or it == 'rotate':
        path = input('Enter the path of image: ')
        im = Image.open(path)
        output = image_rotation(im)
    elif it == '4' or it == 'adding photo' or it == 'add':
        path = input('Enter the path of image: ')
        im = Image.open(path)
        output = photo_addition(im)
    elif it == '5' or it == 'adding text' or it == 'txt':
        path = input('Enter the path of image: ')
        im = Image.open(path)
        output = watermark_addition(im)
    elif it == '6' or it == 'filter':
        path = input('Enter the path of image: ')
        im = Image.open(path)
        output = image_filter(im)
    elif it == '7' or it == 'collage' or it == 'clg':
        output = collage()
    elif it == '8' or it == 'color layers collage' or it == 'layer':
        path = input('Enter the path of image: ')
        im = Image.open(path)
        output = color_layers_collage(im)
    elif it == '9' or it == 'gif':
        output = gif_maker()
    elif it == '10' or it == 'gif sequence':
        output = sequence()
    elif it == '11' or it == 'draw':
        path = input('Enter the path of image: ')
        im = Image.open(path)
        output = rectangle_drawing(im)
    else:
        print("Wrong input, Try again!")
except FileNotFoundError:
    print("File doesn't exist, write the path correctly")
except SystemError:
    print("The cutting distance is not set correctly")
except:
    print("Unexpected error!")
    