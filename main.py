# John Jezl and David Lund

from PIL import Image
import numpy as np
from search import *

# function: create_image
# inputs:
#   path: list of (x, y) tuples representing path from start to goal
#   visited: dictionary mapping (x, y) tuples to boolean indicating if pixel was visited
#   image_array: original 2D array of pixels
#   new_image: filename for the output image
# output: none
# relationships:
#   creates and saves a new image highlighting visited pixels in green and path pixels in red
# pseudocode:
#   copy the original image array
#   for each pixel in visited, set its color to green in the copied array
#   for each pixel in path, set its color to red in the copied array
#   create a new image from the modified array and save it
def create_image(path, visited, image_array, new_image):
    modified_array = image_array.copy()
    for pixel in visited:
        x, y = pixel
        modified_array[x][y][0] = 0
        modified_array[x][y][1] = 255
        modified_array[x][y][2] = 0

    for pixel in path:
        x, y = pixel
        modified_array[x][y][0] = 255
        modified_array[x][y][1] = 0
        modified_array[x][y][2] = 0

    new_img = Image.fromarray(modified_array)
    new_img.save(new_image)


# get user inputs
img_path = input("Enter the input image name: ")
s_r = int(input("Enter the start pixel's row: "))
s_c = int(input("Enter the start pixel's column: "))
t_r = int(input("Enter the goal pixel's row: "))
t_c = int(input("Enter the goal pixel's column: "))
breadth_img_path = input("Enter the breadth first output image name: ")
best_img_path = input("Enter the best first/A* output image name: ")

# convert image to usable format
img = Image.open(img_path)
img = img.convert('RGB')
pixel_array = np.array(img)

# call searches and create images
path_breadth, visited_breadth = breath_first_search(pixel_array, (s_r,s_c),(t_r,t_c))
create_image(path_breadth, visited_breadth, pixel_array, breadth_img_path)

path_best, visited_best = best_first_search(pixel_array, (s_r,s_c),(t_r,t_c))
create_image(path_best, visited_best, pixel_array, best_img_path)

# output results
print("The shortest path from s to t has length", len(path_best) - 1)