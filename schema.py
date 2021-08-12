from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    last_name: str = None
    age: int

    class Config:
        orm_mode = True
        # Pydantics orm_mode will tell the Pydantic model to read the data even
        # if it is not a dict, but an ORM model (or any other arbitrary object
        # with attributes).