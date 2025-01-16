from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()
users = {
        123: {"user_id":123,"name": "John", "age": 25, "email": "john@gmail.com"},
        124: {"name": "Doe", "age": 30, "email": "doe@gmail.com"},
    }
#returning a string
@app.get("/")
async def read_root() -> dict:
    return {"message":"Hello World"}

#returning a dictionary
@app.get("/users")
async def read_users() -> dict:
    return users


#path parameter
@app.get("/users/{user_id}")
async def read_user(user_id: int, q: str = None) -> dict: 
   
    if user_id in users: 
        return { "users" : users[user_id], "message": f"Hello {q}"}
    else:
        return {"error": "User not found"} 
#usecase of path parameter
#http://abc.com/users/123

#query parameter
@app.get("/admin")
async def read_admin(type: str="superadmin", q: str = None):
    return {"message": f"Hello {type} Admin {q}"}
#usecase of query parameter
#http://abc.com/admin?type=superuser&q=1234

class User(BaseModel):
    name: str
    age: int
    profession: str
    email: str
#request body
@app.post("/create_user")
async def create_user(user_data: User):
    return {"user_data": user_data}

#  get headers
@app.get("/get_headers")
async def get_headers(
    user_agent: str = Header(None),
    x_token: str = Header(None),
    accept : str = Header(None),
    host : str = Header(None),
    content_type : str = Header(None),
):
    request_headers = {}
    request_headers["user_agent"] = user_agent
    request_headers["x_token"] = x_token
    request_headers["accept"] = accept
    request_headers["host"] = host
    request_headers["Content-Type"] = content_type
    return request_headers

#usecase of headers
#http://abc.com/get_headers
#actual usecase of headers is to pass the token in the header for authentication purpose.