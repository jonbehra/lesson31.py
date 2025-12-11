from pydantic import BaseModel

class AuthorBAse(BaseModel):
    name: str

class AuthorCreate(AuthorBAse):
    pass

class AuthorResponse(BaseModel):
    id: int
    name : str

class Author(AuthorBAse):
    id : int
    