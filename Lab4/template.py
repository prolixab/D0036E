from skimage import io
import numpy as np

def match_template(main_image, template_image):
    main_image_y, main_image_x = main_image.shape
    template_image_y, template_image_x = template_image.shape
    rows = main_image_y - template_image_y
    columns = main_image_x - template_image_x
    results_array = [[0 for x in range(columns)] for y in range(rows)]
    for i in range(rows):
        for j in range(columns):
            part_image = main_image[i:i + template_image_y, j:j + template_image_x]
            results_array[i][j] = calculate_value(part_image, template_image)
    return results_array


def calculate_value(part_image, template_image):
    part_image_np=np.array(part_image)
    template_image_np=np.array(template_image)
    diff=part_image_np-template_image_np


    # for i in range(rows):
    #     for j in range(columns):
    #         diff = part_image[i][j] - template_image[i][j]
    #         sum += abs(diff)
    return diff.sum()
