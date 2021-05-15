"""
Author: Julius Feigl
Matr.Nr.: K11829015
Exercise 4
"""
import numpy as np


def ex4(image_array, border_x, border_y):

    # Check if any of the errors has to be raised
    # NotImplementedError
    if isinstance(image_array, np.ndarray) is False:
        raise NotImplementedError
    if np.ndim(image_array) != 2:
        raise NotImplementedError

    # ValueError
    if isinstance(border_x[0], int) is False:
        raise ValueError
    if isinstance(border_x[1], int) is False:
        raise ValueError
    if isinstance(border_y[0], int) is False:
        raise ValueError
    if isinstance(border_y[1], int) is False:
        raise ValueError
    if border_x[0] < 1 or border_x[1] < 1 or border_y[0] < 1 or border_y[1] < 1:
        raise ValueError
    size_image = image_array.shape
    if size_image[0] - border_x[0] - border_x[1] < 16 or size_image[1] - border_y[0] - border_y[1] < 16:
        raise ValueError
    else:
        # Calculate input_array from image_array
        # Make copy from image_array
        input_array = np.copy(image_array)
        # cut top part
        input_array[:border_x[0], :] = 0
        # cut bottom
        input_array[input_array.shape[0] - border_x[1]: input_array.shape[0], :] = 0
        # cut left border
        input_array[border_x[0]:input_array.shape[0] - border_x[1], :border_y[0]] = 0
        # cut right border
        input_array[border_x[0]:input_array.shape[0] - border_x[1], input_array.shape[1] - border_y[1]:] = 0

        # Get known_array from input_array by using boolean mask
        known_array = input_array > 0
        # Convert to dtype of image_array
        known_array = known_array.astype(image_array.dtype)
        # set everything whats 0 inside to 1
        known_array[border_x[0]:known_array.shape[0] - border_x[1], border_y[0]:known_array.shape[1] - border_y[1]] = 1

        # Get target array
        # Make Boolean Mask with all 0 = True and all 1 = False
        mask = known_array < 1
        # fancy indexing with boolean mask, all former cut values (True) are saved in target_array
        target_array = image_array[mask]

        return input_array, known_array, target_array
