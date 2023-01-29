from pydantic import BaseModel

class CreateUser(BaseModel):
    user:str
    address:str
    start_point:str