import skimage
import os
import matplotlib.pyplot as plt

filename_path = '/home/andrew/PycharmProjects/LTU/Labs/Lab4/'
coins_filename = os.path.join(filename_path, 'coins.jpg')
astro_filename = os.path.join(filename_path, 'astronaut.jpg')

from skimage import io

## Task 1

coins_image = io.imread(coins_filename)
astro_image = io.imread(astro_filename)
print(f"Coins image has shape {coins_image.shape} and type {coins_image.dtype}")
print(f"Astro image has shape {astro_image.shape} and type {astro_image.dtype}")
print(f"In Astro point 1,100,1 has value {astro_image[1, 100, 1]}")
print(f"In Coins point 1,100 has value {coins_image[1, 100]}")
# io.imshow(image)
# io.show()
ax = plt.imshow(astro_image)
plt.show()

## Task 2
# Coins cannot be converted to grayscale since it is already grayscale.
from skimage.color import rgb2gray

grayscale = rgb2gray(astro_image)
print(f"Before grayscale conversion astro image has shape {astro_image.shape} and type {astro_image.dtype}")
print(f"After grayscale conversion astro image has shape {grayscale.shape} and type {grayscale.dtype}")
io.imshow(grayscale)
io.show()

## Task 3

from skimage.transform import rescale, resize

# Rescale astro
fig, axes = plt.subplots(nrows=2, ncols=2)

ax = axes.ravel()

# Note - channel_axis needed to rescale colour images
image_rescaled_075 = rescale(astro_image, 0.75, anti_aliasing=False, channel_axis=2)
image_rescaled_05 = rescale(astro_image, 0.5, anti_aliasing=False, channel_axis=2)
image_rescaled_025 = rescale(astro_image, 0.25, anti_aliasing=False, channel_axis=2)
image_resized = resize(astro_image, (astro_image.shape[0] / 4, astro_image.shape[1] / 4), anti_aliasing=True)

ax[0].imshow(image_rescaled_075)
ax[0].set_title("Rescaled 0.75")

ax[1].imshow(image_rescaled_05)
ax[1].set_title("Rescaled 0.5")

ax[2].imshow(image_rescaled_025)
ax[2].set_title("Rescaled 0.25")

ax[3].imshow(image_resized)
ax[3].set_title("Resized to a 1/4")

plt.tight_layout()
plt.show()

# Task 4

import numpy as np
from skimage.exposure import histogram
import matplotlib.pyplot as plt
from skimage.util import img_as_ubyte

# grayscale = rgb2gray(coins_image)

ax = plt.hist(coins_image.ravel(), bins=256)
print(coins_image.dtype)
t = 160
binary = coins_image < t
fig, ax = plt.subplots()
plt.imshow(binary, cmap="gray")
plt.show()

# Task 5
from skimage import data
from skimage.feature import match_template

#Extracting single coin image from coins
image = data.coins()
coin = image[170:220, 75:130]


result = match_template(image, coin)
ij = np.unravel_index(np.argmax(result), result.shape)
x, y = ij[::-1]

fig = plt.figure(figsize=(8, 3))
ax1 = plt.subplot(1, 3, 1)
ax2 = plt.subplot(1, 3, 2)
ax3 = plt.subplot(1, 3, 3, sharex=ax2, sharey=ax2)

ax1.imshow(coin, cmap=plt.cm.gray)
ax1.set_axis_off()
ax1.set_title('template')

ax2.imshow(image, cmap=plt.cm.gray)
ax2.set_axis_off()
ax2.set_title('image')
# highlight matched region
hcoin, wcoin = coin.shape
rect = plt.Rectangle((x, y), wcoin, hcoin, edgecolor='r', facecolor='none')
ax2.add_patch(rect)

ax3.imshow(result)
ax3.set_axis_off()
ax3.set_title('`match_template`\nresult')
# highlight matched region
ax3.autoscale(False)
ax3.plot(x, y, 'o', markeredgecolor='r', markerfacecolor='none', markersize=10)

plt.show()
