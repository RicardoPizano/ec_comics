import time
from hashlib import md5
from typing import Tuple, Union, List, Dict

import requests

import logger
from constans import MARVEL_PUBLIC_KEY, MARVEL_PRIVATE_KEY
from models.responses import Character, Comic

LOGGER_FILE_NAME = "repositories/marvel.py"


class ApiMarvel:
    BASE_URL = "https://gateway.marvel.com/v1/public"
    CHARACTERS_ENDPOINT = "characters"
    COMICS_ENDPOINT = "comics"

    @staticmethod
    def _get_ts_hash() -> Tuple[str, str]:
        ts = time.time()
        raw_hash = f"{ts}{MARVEL_PRIVATE_KEY}{MARVEL_PUBLIC_KEY}"
        hash_param = md5(raw_hash.encode('utf-8'))
        return str(ts), hash_param.hexdigest()

    @staticmethod
    def _get_default_params(limit: int = 20, offset: int = 0):
        ts, hash_param = ApiMarvel._get_ts_hash()
        return {
            "ts": ts,
            "apikey": MARVEL_PUBLIC_KEY,
            "hash": hash_param,
            "limit": limit,
            "offset": offset
        }

    @staticmethod
    def find_comics(query: str = None, limit: int = 20, offset: int = 0) -> List[Comic]:
        url = f"{ApiMarvel.BASE_URL}/{ApiMarvel.COMICS_ENDPOINT}"
        params = ApiMarvel._get_default_params(limit=limit, offset=offset)
        params["orderBy"] = "title"
        if query:
            params["titleStartsWith"] = query
        comics = list()
        try:
            response = requests.get(url=url, params=params)
            if response.status_code == 200:
                json_response = response.json()
                for comic in json_response['data']['results']:
                    comics.append(ApiMarvel._parse_comic(comic=comic))
            return comics
        except KeyError:
            logger.err(LOGGER_FILE_NAME, "find_comics", "error to try get a response element")
            return comics
        except Exception as e:
            logger.err(LOGGER_FILE_NAME, "find_comics", f"error: {str(e)}")
            return comics

    @staticmethod
    def _parse_comic(comic: Dict[str, any]) -> Union[Comic, None]:
        try:
            image = f"{comic.get('thumbnail').get('path')}.{comic.get('thumbnail').get('extension')}"
            on_sale_date = ""
            for date in comic.get("dates", []):
                if date["type"] == "onsaleDate":
                    on_sale_date = date["date"]
                    break
            return Comic(
                id=comic["id"],
                title=comic["title"],
                image=image,
                onsaleDate=on_sale_date,
            )
        except Exception as e:
            logger.err(LOGGER_FILE_NAME, "_parse_comic", f"error: {str(e)}")
            return

    @staticmethod
    def find_characters(query: str = None, limit: int = 20, offset: int = 0) -> List[Character]:
        url = f"{ApiMarvel.BASE_URL}/{ApiMarvel.CHARACTERS_ENDPOINT}"
        params = ApiMarvel._get_default_params(limit=limit, offset=offset)
        params["orderBy"] = "name"
        if query:
            params["nameStartsWith"] = query
        characters = list()
        try:
            response = requests.get(url=url, params=params)
            if response.status_code == 200:
                json_response = response.json()
                for character in json_response['data']['results']:
                    characters.append(ApiMarvel._parse_character(character=character))
            return characters
        except KeyError:
            logger.err(LOGGER_FILE_NAME, "find_comics", "error to try get a response element")
            return characters
        except Exception as e:
            logger.err(LOGGER_FILE_NAME, "find_characters", f"error: {str(e)}")
            return characters

    @staticmethod
    def _parse_character(character: Dict[str, any]) -> Union[Character, None]:
        try:
            image = f"{character.get('thumbnail').get('path')}.{character.get('thumbnail').get('extension')}"
            return Character(
                id=character["id"],
                name=character["name"],
                image=image,
                appearances=character.get("comics").get("available"),
            )
        except Exception as e:
            logger.err(LOGGER_FILE_NAME, "_parse_character", f"error: {str(e)}")
            return
