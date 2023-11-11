import numpy as np
import torch
import torchvision.models as models
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import cv2
import matplotlib.image as mpimg
from PIL import Image
import sys
sys.path.append("..")
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor
from image_classifier import image_classifier
from tqdm import tqdm


sam_checkpoint = "sam_vit_h_4b8939.pth"
model_type = "vit_h"

device = "cpu"
ID_colonnina = 666

sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)

mask_generator = SamAutomaticMaskGenerator(sam)

def Segmenter(image_path):
    
    image = mpimg.imread(image_path)
    
    masks = mask_generator.generate(image)

    list_of_labels = []
    #objects = {}
    
    for _, mask in tqdm(enumerate(masks), total=len(masks), desc="Segmenting over masks"):
        box = mask["bbox"]
        x, y, w, h = box
        cropped_image = image[y:y+h, x:x+w]

        # qui metti il segmentedededdd
        label = image_classifier(cropped_image)

        list_of_labels.append(label)

   # objects = {"stationID": ID_colonnina ,"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"object" : list_of_labels}
    return list_of_labels
        