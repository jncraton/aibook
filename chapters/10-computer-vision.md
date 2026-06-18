# Computer Vision

**Computer vision** allows computers to process visual information. While the world looks continuous to us, computers represent images using a 2-dimensional array of colors called **pixels**.

![Pixel close-up](https://upload.wikimedia.org/wikipedia/commons/d/de/Closeup_of_pixels.JPG)

While there are many approaches and techniques for extracting information from images, some simple tricks are available to perform **feature extraction**. For example, what if we wanted to count the bricks in the following image?

![Three toy bricks](chapters/media/bricks-1.png)

One task in computer vision is deciding what information is irrelevant and can be safely discarded. For this problem, the colors of the bricks are not relevant, so can safely simplify the pixel information to remove color components and convert the image to **grayscale**.

![Converted to grayscale](chapters/media/bricks-2-grayscale.png)

This image also has many more pixels than is strictly required to count the bricks. One technique we can use is to **downsample** the image by a factor, say 4x, to remove much of the information. If we apply an average to each 4x4 chunk from the original image, we also smooth over any **image noise** or graininess from the original image.

![Downsampled](chapters/media/bricks-3-downsample.png)

This is still more complex than we need for a simple count. We don't actually care about the specific lightness of an individual pixel, we just need to know if a brick is present at that position or not. For this, we can apply **global thresholding** to each pixel. If a pixel is brighter than a certain threshold, we pull it to white, otherwise we push it to black.

![Threshold applied](chapters/media/bricks-4-threshold.png)

From here, we can apply an algorithm for **connected-component labeling** by scanning the image for black pixels, incrementing a counter, and marking all connected pixels using **flood fill**.

## Application

The brick counter described in this chapter is available as a project to complete here:

<https://github.com/jncraton/brick-count>
