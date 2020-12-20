from pydantic import BaseModel
from typing import List,Dict


class Movie(BaseModel):
    title : str
    imageUrl : str
    ratingValue : str
    ratingCount : str
    duration : str
    genre : List[str]
    release_date : str
    summary_text : str
    credits : Dict[str,List[str]]
    class Config:
        orm_mode = True