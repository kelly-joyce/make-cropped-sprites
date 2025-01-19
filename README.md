# make-cropped-sprites
Features python code that takes a png image containing multiple sprite images and outputs multiple files cropping each individual sprite image.

# Summary

This code uses an input of a transparent background image that contain multiple sprites and outputs a folder that crops these sprite into individual images using OpenCV. Before closing, it will also show a preview of the original image, the alpha layer of the image, and a preview of where each crop was for the sprites. The order outputted is roughly from the bottom-up.

# Before Using

Please install cv2 and matplotlib before running this if you haven't before. You can do so by running ```pip install cv2``` and ```pip install matplotlib``` in your console.

The code asks for the filename that will be inputted. At the moment, this file must be in the same directory as this Python file.

The output folder it asks for must also be in the same directory as the code.

# Extra Things

I have edited this code to be used in a more general setting compared to when I first used it. However, this code's main purpose was for my personal use, so apologies for the weird text inputs. This is my first program using OpenCV. The code is commented for some clarity to how it works.

There is one issue that if the sprite has a hole in, it will output the hole as an extra picture. If the length and width of the sprite is less than 20px by 20px, it will not be in the output as I had these limits in place to prevent excess output of stray pixels and small holes in sprites.
