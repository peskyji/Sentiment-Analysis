from unittest.mock import Base
from fastapi import FastAPI
from pydantic import BaseModel

# create an object of FastAPI
app = FastAPI()

# create objects to receive input from client
class Input(BaseModel):
    num1 : float
    num2 : float
    num3 : float = 0.1
    text : str = None

# create route for index page
@app.get("/")
def homepage():
    print("Hi this is index page")
    return {'a':'b'}

# create another route for calculation
@app.post("/calculate")
def calculate(data:Input):
    my_dict={}
    if data.num3 != 0.1:
        return {'sum':data.num1+data.num2+data.num3}
    else:
        return {'sum':data.num1+data.num2, "num3":data.num3, "text":data.text}




