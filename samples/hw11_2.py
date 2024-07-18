import os

from matplotlib import image
from matplotlib import pyplot

path = os.path.dirname(os.path.abspath(__file__))
lenna = path + '/' + 'lenna.bmp'
flag = path + '/' + 'flag.bmp'
image1 = image.imread(lenna)
image2 = image.imread(flag)

plot_data = image1.copy()
print(image1.shape)
print(image2.shape)
for width in range(250):
    for height in range (132):
        plot_data[height][512-(250-width)] = image2[height][width]
pyplot.imshow(plot_data)
pyplot.show()