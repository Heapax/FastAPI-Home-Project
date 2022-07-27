# FastAPI

# Advantages:

1. Data Validation - in FastAPI you define the types of data your API is expecting.
   Traditionally when we wire a web app in python we don't explictly set what type of information our endpoint will be accepting, this means we have to do alot of data validation, to check and ensure that the tpye of data you recive is matching to the expected type.
   In FastAPI this is done automatically so if the API gets the wrong type of it will return an error telling us what type of data was recived and what is expected.
2.

# HTTP methods

- GET - returns information from the endpoint, "gets" information.
- POST - sending information to the endpoint, or creating something new, e.g "posting" a new user login.
- PUT - update/modifiy exsiting information.
- DELETE - deleting exsiting information.

# Running the API

1. "cd" into the directory containing the API script.
2. Execute the following command "uvicorn working:app --reload", the syntax is as follows: "uvicore <name_of_script>:<name_of_app_in_script> --reload".
   note: the "--reload" means that uvicorn will constantly reload the server whenever a change is made to the python file that stores that API.
