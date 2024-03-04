# chargeware - AI for parking abuse detection and customer profiling

chargeware is a project that aims to fullfill VMware needs of creating smart EV charging stations. Using ML and AI data is collected to detect users and authorize them. In case of a a parking abuse, the system is able to detect:

- thermal engine cars

- ev, not plugged in after 5 mins

- ev, finished charging and still occupying the spot

**This is a proof-of-concept developed during the 24h Hackathon at NOI Techpark on 10th of November 2023.**

Here only the AI part is reported. To see the full project, consult the original repository from which this was forked (XRDPlus)

## Overview
This Python scripts are part of a system to manage parking spaces equipped with electric vehicle (EV) charging stations. The system utilizes various detection modules to identify and monitor vehicles, individuals, and their activities. The main goal is to 

1. Identify a parking abuse.
2. Improve customer experience: understand if assistance is needed, recommend points of interests nearby after charging has begun.
3. Customer profiling.

You can find the presentation of this project at this [link](https://hackathon.bz.it/project/chargeware) .
 
**See the file ` MainStatic.py` for the complete implementation**
##  AI Modules

### CarDetection
The `CarDetection` module is responsible for identifying the presence of a car in the parking space. It captures an image and uses car detection algorithms to determine whether a car is present.

### PlateDetection
The `PlateDetection` module is used to read the license plate of the detected car. The script captures an image and processes it to extract the license plate information.

### PersonDetection
The `PersonDetection` module monitors the area to detect if a person is present. It checks for the presence of individuals and the time elapsed since the last detection.

### FaceRecognition
The `FaceRecognition` module is utilized for customer profiling. It captures an image of the person, recognizes facial features, and extracts information such as age, gender, ethnicity, and emotion.

### Segmenter
The `Segmenter` module employs Meta's Segment Anything to identify and segment objects within an image. This is used to gather additional information about the environment.

## Configuration for a MVP 

- **trigger:** The trigger variable determines the main loop's activation. In a real scenario, this would be connected to a proximity sensor.

- **maximum_time_without_person:** The maximum time allowed without detecting a person near the car.

- **max_overall_time:** The maximum overall time a customer is allowed to stay in the parking space (minutes).

- **charging:** A boolean variable indicating whether the car is currently charging.

- **ID_colonnina:** The unique ID of the charging station.

## Workflow

1. **Car Detection:**
   - Captures an image to check for the presence of a car.
   - If a car is detected, it proceeds to the next steps; otherwise, it prints a message indicating the absence of a car.

2. **License Plate Detection:**
   - Captures a new image to read the license plate.
   - Sends the plate number to an API to determine if the car is electric.

3. **Person Detection:**
   - Monitors the area continuously until a person is detected.
   - If no person is detected within a specified time, a warning message is printed, urging the person to exit the car or leave the parking spot.

4. **Customer Profiling:**
   - Captures an image of the person.
   - Uses facial recognition to determine age, gender, ethnicity, and emotion.
   - Sends profiling information to an API or database.

5. **Charging Phase:**
   - If the car is electric, waits for the person to exit the car.
   - Checks the emotion of the person; if negative, calls for assistance beacuse probably he needs help.
   - If positive we assume he initiates the charging phase and provides recommendations to the customer.
   - Runs the `Segmenter` to gather additional environmental information.

6. **API Requests:**
   - Sends relevant data, including parking arrival, driver exit, user profiling, and environmental information, to a specified API.


