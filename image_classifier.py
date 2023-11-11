import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import numpy as np


def image_classifier(image):
    # Image should be a numpy array
    # Load the pre-trained ResNet model
    resnet = models.resnet50(pretrained=True)
    resnet.eval()


    # Define a transformation for your input image
    # These values are requested in PyTorch documentation: https://pytorch.org/hub/pytorch_vision_resnet/
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize((224, 224)),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])


    # Load and preprocess your image

    #image = Image.open(image_path)
    input_tensor = transform(image)
    input_batch = input_tensor.unsqueeze(0)  # Add a batch dimension

    # Check if a GPU is available and move the model and input tensor to the GPU
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    resnet.to(device)
    input_batch = input_batch.to(device)

    # Perform inference
    with torch.no_grad():
        output = resnet(input_batch)


    # Load the labels used by the pre-trained model
    # You can find the labels here: https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json
    import requests
    LABELS_URL = "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json"
    labels = requests.get(LABELS_URL).json()

    # Get the predicted label
    _, predicted_idx = torch.max(output, 1)
    predicted_label = labels[predicted_idx.item()]

    #print("Predicted Label:", predicted_label)


    return predicted_label



