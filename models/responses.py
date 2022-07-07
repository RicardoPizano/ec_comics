from typing import List

from pydantic import BaseModel


class Character(BaseModel):
    id: int
    name: str
    image: str
    appearances: int


class Comic(BaseModel):
    id: int
    title: str
    image: str
    onsaleDate: str


class SearchComicsResponse(BaseModel):
    characters: List[Character] = list()
    comics: List[Comic] = list()
