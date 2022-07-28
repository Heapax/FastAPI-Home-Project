from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

@app.get("/")
def home():
  return {"Data": "Test"}

@app.get("/about")
def about():
  return {"Data": "About"}

inventory = {
    1: {
      "name": "Milk",
      "price": 3.99,
      "brand": "Regular"
    }
}

# Set a path with a variable of "item_id" in this case "1", and set the input data to be only valid as an intreger, and default path could be any item id but here used "None" as default
# And added a decription for the api method.
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None ,description="The ID of the item you would like to view")):
  return inventory[item_id]

# Accepts one query parameter, and that will be the item that we want to retrive
# The query parameter is "name" which is a string.
@app.get("/get-by-name")
def get_item(name: Optional[str] = None):
  for item_id in inventory:                   # Loops over the items in a given inventory id
    if inventory[item_id]["name"] == name:    # If the item that is looped over in a spacific inventory id has the parameter "name" and assigns its value "Milk" the the fucntion "name" paramenter
      return inventory[item_id]               # Reterns the item id of inventory id "1" becasue ("name" : "Mlik") is assigned 
  return {"Data": "Not found"}                # Else returens "Data" : "Notfound"

# In this example when we go to "http://localhost:8000/get-by-name?name=milk", we will get the output of inventory id "1"
# If no parameter is passed then we will get an error with the message "field required".
# When we set "str = None" this allows us to not get an error when no parameter is passed, insted we get {"Data": "Not found"}