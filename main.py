import uvicorn  # To start an ASGI web server
from typing import Union  # For type hinting that FastAPI uses
from fastapi import FastAPI  # For creating APIs
from pydantic import BaseModel  # For automatic data validation and conversion


# Create our application
app = FastAPI()

# Pydantic class for automatic data validation and conversion
class User(BaseModel):
    user_id: Union[int, None]


# This function is triggered automatically when a request is made to the root (index) page.
@app.get("/")
async def root_page():  # user-defined Asynchronous function, the function name can be anything.
    return {"message": "Connection establised, Welcome!!!"}


# Creating an welcome/{paramter} endpoint, where the path parameter 'user_name' can be set by the client
# And the function can take in a parameter of the same name for further operations.
@app.get("/welcome/{user_name}")
async def path_parameter(user_name: str):
    return {"message": f"Hi {user_name} this is an endpoint with your name!!!"}


# Creating an /user/{paramter} endpoint, where the path parameter 'user_name' can be set by the client
# And the function can take in a parameter of the same name for further operations.
# Further, the function can take one more parameter 'age' which is considered as a query parameter.
@app.get("/user/{user_name}")
async def path_parameter_with_qeury(user_name: str, age: int):
    return f"welcome to your page User: {user_name}. The query parameter 'age'= {age}"


# Creating a welcome/post endpoint where you can send "user_id" as part of request body.
@app.post("/welcome/post")
async def welcome_with_post(user: User):
    # Here you can perform any computation you want.
    # ===================================================================
    if user.user_id:
        user_id_square = user.user_id**2
        return_message = f"Hello {user.user_id}, this message uses data passed via the post request!!!"
        return_message += f" user_id_square is {user_id_square}."

    else:
        return_message = "No user id passed."
    # ===================================================================
    return {"message": return_message}


if __name__ == "__main__":
    """
    The web server can be started by

    either executing: uvicorn main:app --reload --port 12345
    or by excecuting: python main.py

    on the terminal or command prompt.
    """
    uvicorn.run("main:app", reload=True, port=12345)
