from PIL import ImageGrab, ImageOps
import numpy as np

while 1:
    image = ImageGrab.grab((190, 440, 200, 450))
    image = ImageOps.grayscale(image)
    imageNp = np.array(image.getcolors())
    imageNpMean = imageNp.mean()
    print(imageNpMean)
    #image.show()