
## Overview
This Python scripts are part of a system to manage parking spaces equipped with electric vehicle (EV) charging stations. The system utilizes various detection modules to identify and monitor vehicles, individuals, and their activities.

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

## Notes
- Ensure that all necessary dependencies and libraries are installed.
- The script is designed for testing purposes and may require adjustments for a real-time environment.
- The API endpoints are currently commented out and should be modified with the appropriate URLs in a production environment.
- The initial run may take up to a minute to load dependencies.

## Dependencies
- Ensure that the following Python modules are installed:
  - `CarDetection`
  - `FaceRecognition`
  - `PersonDetection`
  - `PlateDetection`
  - `Segmenter`
- External dependencies may include image processing libraries and APIs for license plate recognition and facial recognition.

## Usage
1. Modify the script according to your requirements and configurations.
2. Run the script in a Python environment.
3. Monitor the console output for system alerts, warnings, and customer profiling information.

## License
This Smart Parking System script is released under the MIT License. See the [LICENSE](LICENSE) file for details.
