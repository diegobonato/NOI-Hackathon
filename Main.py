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

        # Send plate number to API and get back if the car is electric or not

        Electric_status = False

        if Electric_status:

            # TODO: ADD timer to parking abusivity

            
            # wait for the person to get out of the car 
            # PersonDection function checks if a person appears in the fieldview of the camera.
            # If no person is detected within a certain amount of time, the charging station will output a warning message,
            # inviting the people to free the parking lot.

            # Start to take frame from the camera unitl a person is detected
            # Here we're still scripting, in real life it will be a continous checking of the camera.
            image = 'confused_man.jpg'
            Person_detected = False

            # If a car arrives we want to understand weather the person is getting out of the car or not.
            # If the person doesn't get out it probably means that he/she is not going to charge the car.
            
            while Person_detected == False:

                Person_detected = PersonDetection(image)
                time_elapsed = time.time() - start_timer

                if time_elapsed > maximum_time_without_person:
                    # Call warning function
                    # warning fucntion should get us out of the loop.
                    print("GET OUT OF THE CAR!!!")
                    break

            # We should have a function that halts everything and print warning message. 
            # If we're here it means that Person_detected == True so this if statement is not necessary.
            # We put it anyway to be sure.
            if Person_detected:
                
                # Start customer profiling:
                # FaceRecognition function detects the followeing characteristics of the person:
                # - Emotion (Angry, Happy, Sad, Neutral, Surprised, Disgusted, Fearful)
                ## - Age
                ## - Etnicity
                ## - Gender

                # profilation is a dictionary containing the above info related to the person.
                profilation = FaceRecognition(image)
              

                # Send profilation data to API
                
                # Final implementation should check an average emotion
                # This script looks at emotion only instantaneously.
                # This is more likely to get false positives. (e.g. a person is angry for a second and then gets happy)
                if profilation['emotion'] == 'Angry':

                    # This should be a function that calls the assistance
                    print('call assistance')
                    break

                # If customer seems to have no problems, check when he/she starts to charge the car
                
                else:
                    # Take data from charging station and set charging = True when the car starts to charge
                    charging = True

                    # API request to show reccomendation based on the customer profile

                    overall_time = time.time() - start_timer

                    # Customer can stay for 40 minutes max.
                    # (If charging station has data regarding the battery, we can check if the car is fully charged or not)
                    # If  car is fully charged, ask driver to free the parking lot asap.

                    if overall_time > max_overall_time*60:
                        print('free the parking lot asap')
                        break

        else:
            # Here if car is not electric
            # Set function
            print('allerta pula')

    else:
        # Here if something different from a car is occupying the parking lot
        print('levati, libera il passaggio per favore')
    
