import urllib

import PIL
import numpy as np
import pokebase as pb
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

plt.title("Pokemon Image")
plt.xlabel("X pixel scaling")
plt.ylabel("Y pixels scaling")
s3 = pb.SpriteResource('pokemon', 10081)
image = mpimg.imread(s3.img_data)
plt.imshow(image)
plt.show()