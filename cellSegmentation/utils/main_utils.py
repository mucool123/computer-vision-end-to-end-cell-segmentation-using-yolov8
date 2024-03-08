#created this utils file because in out code, there will be some functionalities whih we will be using very often 
#like reading yaml file, reading json file, we cant write code everytime for it, so we willl code once and store it inside our
#utils file

import os.path
import sys
import yaml
import base64

from cellSegmentation.exception import AppException
from cellSegmentation.logger import logging


def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns its contents as a dictionary.

    :param file_path: The path to the YAML file to be read.
    :return: A dictionary representing the YAML file's contents.
    """
    try:
        with open(file_path, "rb") as yaml_file:
            logging.info("Read yaml file successfully")
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise AppException(e, sys) from e
    



def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Writes content to a YAML file at the specified path. Optionally replaces the file if it already exists.

    :param file_path: The path to the YAML file to be written.
    :param content: The content to write to the file.
    :param replace: Whether to replace the file if it already exists. Defaults to False.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            yaml.dump(content, file)
            logging.info("Successfully write_yaml_file")

    except Exception as e:
        raise AppException(e, sys)
    



def decodeImage(imgstring, fileName):
    """
    Decodes a base64-encoded image string and saves it to a file.

    :param imgstring: The base64-encoded image string.
    :param fileName: The name of the file to save the decoded image.
    """
    imgdata = base64.b64decode(imgstring)
    with open("./data/" + fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    """
    Encodes an image file into a base64 string.

    :param croppedImagePath: The path to the image file to be encoded.
    :return: The base64-encoded string of the image.
    """

    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())

    
    