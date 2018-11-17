# Heart Rate Sentinel Server


## How to Run
* Clone the heart_rate_sentinel_server repository onto your machine
* The server.py file should already be running on http://vcm-7335.vm.duke.edu:5002/
* Initialize the virtual environment by running `pip install -r requirements.txt` in the terminal
* Run the client.py file 
* The script should print information about 6 options to show the functionality of each of the 6 server routes
* Enter the desired route
* It is recommended that you run the client script 6 times in the order 1 to 6 to see all route functionality
* If you would like to change the email to your own, go to line 83 of the client.py file and enter your own email
* If you would like to increase or decrease the number of patients created, change num_patients on line 84

## Route Functionality and Messages
* `POST /api/new_patient`
  * Route adds new patients to the database. It expects the following input:
  ```sh
  {
      "patient_id": "1", # usually this would be the patient MRN
      "attending_email": "suyash.kumar@duke.edu", 
      "user_age": 50, # in years
  }
  ```
  * If these three keys are not entered, the server will return the following error message:
  ```sh
  {"message": 'Required Keys not Present'}
  ```
  * If the patient id alread exists, the server will return the following error message:
  ```sh
  {'message': 'Cannot overwrite current patient information'}
  ```
  * If a patient is added correctly, the server will return the following message:
  ```sh
  {'message': 'Added patient 1 successfully to the patient database'}
  ```
* `POST /api/heart_rate`
 * Route adds patient heart rate data to the database. It expects the following input:
  ```sh
  {
      "patient_id": "1", # usually this would be the patient MRN
      "heart_rate": 100
  }
  ```
  * If these three keys are not entered, the server will return the following error message:
  ```sh
  {"message": 'Required Keys not Present'}
  ```
  * If the patient id alread exists, the server will return the following error message:
  ```sh
  {'message': 'Cannot overwrite current patient information'}
  ```
  * If a patient is added correctly, the server will return the following message:
  ```sh
  {'message': 'Added heart rate data for user 1 successfully to the patient database'}
  ```
  * If the posted heart rate is determined to be tachycardic based on the age of the patient, an email will be sent to the attending email
  * The database entry for the patient will then be the following:
  ```sh
  {
    "_id": 1,
    "attending_email": "clarkbulleit@gmail.com",
    "user_age": 65,
    "heart_rate": [
        104,
    ],
    "time": [
        "2018-11-17 13:06:04.108997",
    ],
    "is_tachycardic": false,
  }
  ```



## Functions
* readcsv.py
* validate_data.py
* peak_detect.py
* time_duration.py
* voltage_extremes.py
* count_beats.py
* calc_mean_hr.py
* create_dict.py
* write_JSON.py
