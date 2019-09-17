import image

p = image.Pixel(45, 76, 200)
print(p.getRed())


import image
img = image.Image("luther.jpg")

print(img.getWidth())
print(img.getHeight())

p = img.getPixel(100, 30)
print(p.getRed(), p.getGreen(), p.getBlue())
