from typing import Union

from fastapi import FastAPI

import logger
from models.enums import FilterTypeEnum
from models.responses import SearchComicsResponse
from repositories.marvel import ApiMarvel

app = FastAPI()

LOGGER_FILE_NAME = "main.py"


@app.get("/searchComics", response_model=SearchComicsResponse)
async def search_comics(query: Union[str, None] = None, search_by_type: Union[FilterTypeEnum, None] = None,
                        limit: Union[int, None] = 20, page: Union[int, None] = 1):
    logger.inf(LOGGER_FILE_NAME, "search_comics", f"try search comic: query => {query} - "
                                                  f"search_by_type => {search_by_type} - "
                                                  f"limit => {limit} - page => {page}")
    response = SearchComicsResponse(characters=list(), comics=list())
    characters = list()
    comics = list()
    offset = limit * (page - 1)
    if query:
        if search_by_type == FilterTypeEnum.characters:
            characters = ApiMarvel.find_characters(query=query, limit=limit, offset=offset)
        elif search_by_type == FilterTypeEnum.comics:
            comics = ApiMarvel.find_comics(query=query, limit=limit, offset=offset)
        else:
            comics = ApiMarvel.find_comics(query=query, limit=limit, offset=offset)
            characters = ApiMarvel.find_characters(query=query, limit=limit, offset=offset)
    else:
        characters = ApiMarvel.find_characters(limit=limit, offset=offset)
    response.characters = characters
    response.comics = comics
    logger.inf(LOGGER_FILE_NAME, "search_comics", f"get {len(comics)} comics and {len(characters)} characters")
    return response
