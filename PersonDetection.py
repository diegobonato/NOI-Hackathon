from imageai.Detection import ObjectDetection
import os

def PersonDetection(image_path):
    # Get the current working directory
    execution_path = os.getcwd()

    # Create an instance of the ObjectDetection class
    detector = ObjectDetection()

    # Set the model type to RetinaNet
    detector.setModelTypeAsRetinaNet()

    # Set the path to the RetinaNet model file
    detector.setModelPath(os.path.join(execution_path , "retinanet_resnet50_fpn_coco-eeacb38b.pth"))

    # Load the RetinaNet model
    detector.loadModel()
    
    # Get the name of the input image file
    image_name=image_path[:-4]

    # Detect objects in the input image
    #output image will be save into cache folder:
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , image_path), output_image_path=f"cache/{image_name}2.jpg", minimum_percentage_probability=30)

    # Check if a person is detected in the image
    is_person=False
    n_person = 0
    for eachObject in detections:
        if eachObject["name"] == "person":
            is_person=True
            n_person += 1
            
    return is_person, n_person

     