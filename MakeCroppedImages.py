"""
Copyright (c) 2025, Kelly Joyce
All rights reserved.

This source code is licensed under the MIT-style license found in the
LICENSE file in the root directory of this source tree. 
"""

import cv2
import matplotlib.pyplot as plt
import os

def read_image(filename):
    #reads images with shape of 4 (includes alpha/transparency)
    img_unchanged=cv2.imread(filename,cv2.IMREAD_UNCHANGED)

    return img_unchanged

def find_alpha(image):
    #gives alpha mask (black with white blobs, second image in final visual)
    _, mask = cv2.threshold(image[:, :, 3], 127, 255, cv2.THRESH_BINARY)

    return mask

def export_image(num,image):
    #used for each image in find dimensions
    #exports it with a number or by custom name depending on initial choice
    newpath=os.path.join(os.path.dirname(__file__), folder_name)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        print("New folder made:",newpath)

    if os.path.exists(os.path.join(newpath,output_name+str(num)+".png")):
        print("File "+output_name+str(num)+".png already exists in the directory.")
        if (not overwrite) and (input("Enter 'y' if you would like to overwrite this file: ")!='y'):
            print("Skipped")
            return None
    cv2.imwrite(os.path.join(newpath,output_name+str(num)+".png"),image)
    print(output_name+str(num)+".png Created.")


def find_dimensions(image,original_image):
    #finds the rectangle by contouring first
    contours,hierarchy = cv2.findContours(image, 1, 2)
 
    new_image=image.copy()
    new_image=cv2.cvtColor(new_image, cv2.COLOR_GRAY2BGR) #convert to give 3 color dimaensions for third image in preview
    count=1

    #looks at each blob/contour
    for i in contours:
        x,y,w,h = cv2.boundingRect(i) #find rectangle information to crop on

        if (w>20) and (h>20): #some contours are noise and aren't correct, this if statement gets rid of most of them
            cv2.rectangle(new_image,(x,y),(x+w,y+h),(0,255,0),5) #makes green rectangle on third image in final visual
            cropped_image = original_image[y:y+h, x:x+w] #crops image

            export_image(count,cropped_image) #use export_image function above
            count+=1
    print(count-1, "images found.")
        
    return new_image

def create_visual(plot1,plot2,plot3):
    # Create subplots
    fig, axs = plt.subplots(1, 3, figsize=(10, 4))

    #convert colors as cv2 is in bgr and plt is in rgb
    # Plot the original image
    rgb = cv2.cvtColor(plot1, cv2.COLOR_BGR2RGB)
    axs[0].imshow(rgb, cmap = plt.cm.Spectral)
    axs[0].set_title('Original Image Shape:'+str(plot1.shape))

    # Plot the alpha image
    rgb2 = cv2.cvtColor(plot2, cv2.COLOR_GRAY2RGB)
    axs[1].imshow(rgb2, cmap = plt.cm.Spectral)
    axs[1].set_title('Alpha Image Shape:'+str(plot2.shape))

    # Plot the rectangle image
    rgb3 = cv2.cvtColor(plot3, cv2.COLOR_BGR2RGB)
    axs[2].imshow(rgb3, cmap = plt.cm.Spectral)
    axs[2].set_title('Rectangle Image Shape:'+str(plot3.shape))

    # Display the subplots
    plt.tight_layout()
    plt.show()


os.chdir(os.path.dirname(__file__)) #make current directory what the file is in
files=list(filter(lambda x: x.endswith('.png'), os.listdir())) #find png files in directory

#Asks which png file to read
while True:
    file=input("Which file would you like to read:"+str(files)+' ')
    if file in files:
        break
    else:
        print("Does not exist. Try again. Make sure this python file is in the same directory as the image, is a .png, and has a transparent background.")

#initialize variable
folder_name=input("Give folder name to put output files into (must be in directory, if not a folder will be created): ")
output_name=input("The output files will be given in [name][number].png format. Give the name for writing the output files: ")
if input("Give 'y' if you want to overwrite files that exist in this folder and give no warnings: ")=='y':
    overwrite=True
else:
    overwrite=False

#actual running functions
page=read_image(file)
alpha=find_alpha(page.copy())
rectangles=find_dimensions(alpha.copy(),page.copy())
create_visual(page,alpha,rectangles)

    