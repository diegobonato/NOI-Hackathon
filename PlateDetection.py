import ocrspace
import re


def Plate_Detection(image_path):
    """
    This function takes an image path as input and returns the detected license plate number.
    It uses OCR to extract text from the image and then applies a regular expression to find the license plate number.

    :param image_path: The path of the image to be processed.
    :type image_path: str
    :return: The detected license plate number.
    :rtype: str
    """
    api = ocrspace.API(endpoint='https://api.ocr.space/parse/image', api_key='K86689608588957', language=ocrspace.Language.Croatian)
    text_in_image = api.ocr_file(image_path)

    license_plate = re.findall(r'\b[A-Z0-9]{7}\b', text_in_image)[0]
    return license_plate
