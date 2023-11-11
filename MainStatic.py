from CarDetection import CarDetection
from FaceRecognition import FaceRecognition
from PersonDetection import PersonDetection
from PlateDetection import PlateDetection
import time
from datetime import datetime
import requests
from Segmenter import Segmenter


trigger = 1 # trigger for the main loop, in real life it will be a proximity sensor

maximum_time_without_person = 60 # seconds
max_overall_time = 40 #minutes
charging = False 
ID_colonnina = 666 # ID of the charging station


# The first time this code is run it can take up to one minute to load.
# For performance evaluation run it two times.

#the trigger actives when there is something in front of the sensor and deactivates when there is nothing
while trigger: 

    # Start timer
    start_timer = time.time()

    # Take a picture and save it in the folder "images"
    image = "car_arrival.jpg"

    # take the picture and detect if there is a car
    Car_detected = CarDetection(image) 

    if Car_detected:

        # Check if car is electric or not by checking the license plate
        # TODO: This is fixed, in real life it will be a continous checking of the license plate
        image = 'plate.jpeg' 

        Plate_number = PlateDetection(image)

        #for testing purposes we set the plate number to a fixed value

        Plate_number = 'TARGA123'


        # Send plate number to API and get back if the car is electric or not

        parking_arrival = {"stationID": ID_colonnina ,"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "plate": Plate_number  }
        ###modifica url
#        requests.post(url='http://127.0.0.1:5000/parking_arrival', json=parking_arrival)

        # Add delay to wait for the API to process the request
        ##time.sleep(.05) 
        #get if car is eletric or not
#        Electric_status = requests.get(f'http://127.0.0.1:5000/valid/{Plate_number}').json()["isEV"]


        Electric_status = True

        if Electric_status:


            # wait for the person to get out of the car 
            # PersonDection function checks if a person appears in the fieldview of the camera.
            # If no person is detected within a certain amount of time, the charging station will output a warning message,
            # inviting the people to free the parking lot.

            # Start to take frame from the camera unitl a person is detected
            # Here we're still scripting, in real life it will be a continous checking of the camera.
            image = "man.jpg"
            Person_detected = False

            # If a car arrives we want to understand weather the person is getting out of the car or not.
            # If the person doesn't get out it probably means that he/she is not going to charge the car.
            
            while Person_detected == False:

                Person_detected, number_persons = PersonDetection(image)
                time_elapsed = time.time() - start_timer

                if time_elapsed > maximum_time_without_person:
                    # Call warning function. This will be handled by the API.
                    print("GET OUT OF THE CAR!!!")
                    break

            # We should have a function that halts everything and print warning message. 
            # If we're here it means that Person_detected == True so this if statement is not necessary.
            # We put it anyway to be sure.
            if Person_detected:

                Person_exited_car = {"ID": ID_colonnina ,"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "plate": Plate_number  }

#                requests.post(url='http://127.0.0.1:5000/driver_out', json=Person_exited_car)
                
                # Start customer profiling:
                # FaceRecognition function detects the followeing characteristics of the person:
                # - Emotion (Angry, Happy, Sad, Neutral, Surprised, Disgusted, Fearful)
                ## - Age
                ## - Etnicity
                ## - Gender

                # profilation is a dictionary containing the above info related to the person.
                profilation = FaceRecognition(image)


                profilation["time_stamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                profilation["number_persons"] = number_persons

                # Send profilation to API / DB
                # Example of profilation: '{"age": 34, "gender": "Man", "ethnicity": "white", "emotion": "neutral", "time_stamp": "2023-11-11 05:08:50"}' 
 #               requests.post(url='http://127.0.0.1:5000/user_profiling', json=profilation)

                print(profilation)

                # Send profilation data to API
                
                # Final implementation should check an average emotion
                # This script looks at emotion only instantaneously.
                # This is more likely to get false positives. (e.g. a person is angry for a second and then gets happy)

                if profilation['emotion'] in ['angry',"fear","sad","disgust"]:

                    # This should be a function that calls the assistance
                    print('call assistance, customer not happy')
                    break

                # If customer seems to have no problems, check when he/she starts to charge the car
                
                else:

                    # Here we should have a function that checks if the car is charging or not.
                    # Take data from charging station and set charging = True when the car starts to charge
                    charging = True

                    # API request to show reccomendation based on the customer profile

                    overall_time = time.time() - start_timer

                    # Customer can stay for 40 minutes max.
                    # (If charging station has data regarding the battery, we can check if the car is fully charged or not)
                    # If  car is fully charged, ask driver to free the parking lot asap.

                    print("Recharging phase begins")
                    print("API should now be giving reccomendations to the customer")

                    # Now we can mine the videos to get as much data as possible
                    # To do so we use Segment Anything from Meta: 
                    # https://segment-anything.com
                    # https://github.com/facebookresearch/segment-anything

                    # Since Segmenter takes quite a few minutes to run, we run it only if charging phase has already begun,
                    # while we are already giving reccomendations to the customer.
                    objects_detected = Segmenter(image)

                    # To send objects_detected to API we need to convert it to a string
                    # Create a dictionary with the list as value
                    objects_detected_dict = {'objects_detected': objects_detected, 'time_stamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

#                    requests.post(url='http://127.0.0.1:5000/user_profiling', json=objects_detected_dict)

                    break


        else:
            # Here if car is not electric
            # Set function
            print('allerta POLIZEI')
            # Send data to API
            
            abusive = {"ID": ID_colonnina ,"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "plate": Plate_number  }

#            requests.post(url='http://127.0.0.1:5000/abusive_parking', json=abusive)
            

            break

    else:
        # Here if something different from a car is occupying the parking lot
        print('levati, libera il passaggio per favore')
        break
    
