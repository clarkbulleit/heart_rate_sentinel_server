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
  {'message': 'Added user 1 successfully to the patient database'}
  ```
* Warning: n Rows with non-numeric inputs were not imported
* Info: test_data.csv was read and validated
* Warning: No beats were detected: 
* Warning: The heart rate is below normal range
* Warning: The hear rate exceeds normal range
* Info: Metrics have been written to test_data.json in the output_data folder


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
