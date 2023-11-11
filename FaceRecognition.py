from deepface import DeepFace

def FaceRecognition(image_path):
        
        # Analyze the image using DeepFace library
        objs = DeepFace.analyze(img_path = image_path, 
                actions = ['age', 'gender', 'race', 'emotion']
        )

        # Extract the age, gender, race, and emotion from the analysis results
        
        age = objs[0]["age"]
        gender = objs[0]["dominant_gender"]
        ethnicity  = objs[0]["dominant_race"]
        emotion = objs[0]["dominant_emotion"]
        
        # Create a dictionary with the 4 variables
        result_dict = {'age': age, 'gender': gender, 'ethnicity': ethnicity, 'emotion': emotion}
        
        # Return the dictionary
        return result_dict

