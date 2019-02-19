import numpy as np

from robust_svm.settings import *


def get_successors(pixd,xlim,ylim):
    """

    :param pixd:
    :param xlim:
    :param ylim:
    :return:
    """



def grow_region(image):
    """

    :param image:
    :return:
    """
def hole_fill(image):
    """

    :param image:
    :return:
    """
def get_seeds(pixel,xlim,ylim,image):
    """

    :param pixel:
    :param xlim:
    :param ylim:
    :param image:
    :return:
    """
def highlight_invariant_threashold(image):
    """

    :param image:
    :return:
    """

def image_to_feature_vector(image):
    """

    :param image:
    :return:
    """


def read_feature_file(features_folder_path, data_class_id, image_file_name):
    """
    The function reads image file and returns its corresponding HOG feature file in the form of a numpy array
    :param data_class_id:The name of directory holding image_feature_filename. (Example = '00000')
    :param image_file_name:The name of image file.(Example = '00000_00001.ppm')
    :return:hog_data_array
    """
    feature_filename = image_file_name.replace(".ppm",".txt")
    feature_file_path = join(features_folder_path, data_class_id, feature_filename)
    hog_data_array = np.fromfile(feature_file_path)
    return hog_data_array


if __name__ == "__main__":
    # Test the function read_feature_file
    data_class_id = '00000'
    image_file_name = '00000_00000.ppm'
    features_folder_path = join(training_data_folder, hog3_path)
    hog_feature_data = read_feature_file(features_folder_path, data_class_id, image_file_name)
