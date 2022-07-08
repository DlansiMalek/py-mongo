from pydantic import BaseModel

class Blog(BaseModel):
    _id: str
    title: str
    content: str
    author: str
    upvote: int
    downvote: int
    