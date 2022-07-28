# FastAPI

## Advantages:

1. **Data Validation** - In FastAPI you define the types of data your API is expecting.
   Traditionally when we wire a web app in python we don't explictly set what type of information our endpoint will be accepting, this means we have to do alot of data validation, to check and ensure that the tpye of data you recive is matching to the expected type.
   In FastAPI this is done automatically so if the API gets the wrong type of it will return an error telling us what type of data was recived and what is expected.
2. **Auto Documentation** - Since we are assigning all of the types expected of the API, fastAPI can generate documentation that also works as a "test script", a webpage is generated so we can access it
   and see all of the API endpoint and what type of input they expect and any description or information.
3. **Auto Completion and Code Suggestions** - If we are working in an IDE like VSCode or Pycharm then we get really good auto-completion because we are defining these types.

## Installation

1.  `pip install fastapi`
2.  `pip install uvicorn`
3.  Make a new python file and import FastAPI from fastapi e.g. `from fastapi improt FastAPI`
4.  To start using the fastAPI we need to create an "app" parameter and assign it the FastAPI method e.g. `app = FastAPI()`

### HTTP methods

- GET - returns information from the endpoint, "gets" information.
- POST - sending information to the endpoint, or creating something new, e.g "posting" a new user login.
- PUT - update/modifiy exsiting information.
- DELETE - deleting exsiting information.

## Running the API

1. "cd" into the directory containing the API script.
2. Execute the following command:
   `uvicorn working:app --reload`
   The syntax is as follows:`uvicore <name_of_script>:<name_of_app_in_script> --reload`.
   _note: the `--reload` means that uvicorn will constantly reload the server whenever a change is made to the python file that stores that API._
