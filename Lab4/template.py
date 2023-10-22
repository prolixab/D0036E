from skimage import io
import numpy as np


def match_template(main_image, template_image):
    """
    Calculates a result matrix of all cross-correlations of the
    template_image against piece by piece areas of the main image,
    based on upper left pixel.
    :param main_image: grayscale image in which the template is sought
    :param template_image: grayscale template image.
    :return: results array with 1all cross correlations. Note the
    results array has smaller x and y dimensions than the main image.
    """
    main_image_y, main_image_x = main_image.shape
    template_image_y, template_image_x = template_image.shape
    rows = main_image_y - template_image_y
    columns = main_image_x - template_image_x
    results_array = np.array([[0 for x in range(columns)] for y in range(rows)], dtype=float)
    for i in range(rows):
        for j in range(columns):
            part_image = main_image[i:i + template_image_y, j:j + template_image_x]
            results_array[i][j] = calculate_value(part_image, template_image)
    return results_array


def calculate_value(a, b):
    """
    Function to calculate the cross-correlation value of the template image
    and a section of an original image
    :param a: np array containing the original image section
    :param b: np array containing the template image
    :return: cross correlation score normalized to between 1,-1
    """
    sum = np.sum((a - a.mean()) * (b - b.mean()))
    std = a.std() * b.std()
    result = sum / std
    x, y = a.shape
    N = float(x * y)
    result /= N
    return result
