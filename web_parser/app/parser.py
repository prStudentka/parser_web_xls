import requests
from requests import Response
from requests import exceptions
from bs4 import BeautifulSoup, Tag
from typing import Dict, List


__URL: Dict[str, str | dict] = {
    'name': 'https://habr.com',
    'path': '/ru/search/',
    'params': {
        'target_type': 'posts',
        'order': 'relevance',
        'q': '{Туториал}',
    }
}


def __get_soup(url: str, params: dict) -> BeautifulSoup | int:
    '''Scrape information from web page

    :param url:    str - this link to open webpage
    :param params: dict - params for set URL parameter

    This function takes two arguments and send a GET request.
    The query parametrs will be embedded in the URL.
    If all OK and you get code 200.
    Scrape information and return parsing HTML.
    '''

    try:
        response: Response = requests.get(url, params=params)
    except exceptions.HTTPError:
        raise ('HTTP error')
    except exceptions.ConnectionError:
        raise ('Error connecting')
    except exceptions.Timeout:
        raise ('Time out')
    except exceptions.RequestException:
        raise ('Sorry...I can not open url')
    finally:
        if response and response.status_code == requests.codes.ok:
            soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
            return soup
        return 0


def __get_url_page(page: int = 1) -> str:
    '''Get next page URL

    :param page: int - page number

    This function return new URL for scrapping
    '''

    if page == 1:
        return f'{__URL["name"]}{__URL["path"]}?'
    return f'{__URL["name"]}{__URL["path"]}page{page}/?'


def include_parser(query: str) -> tuple | None:
    '''Filtering queries in the context

    :param query: str - filter for context

    This function get html page and filtering contex by user query
    Returning result work
    '''

    soup: BeautifulSoup | int = __get_soup(
        __get_url_page(),
        __URL['params']
    )
    if soup:
        last_tag: Tag = soup.find_all('a', attrs={
            'class': 'tm-pagination__page'})[-1]
        last_page: int = int(last_tag.contents[0])
        page: int = 0
        rows: List[List[str]] = []
        while page < last_page:
            page += 1
            soup_page: BeautifulSoup | int = __get_soup(
                __get_url_page(page),
                __URL['params']
            )
            items: Tag = soup_page.find_all(
                'a', attrs={
                            'class': 'tm-title__link'
                            }
            )
            for item in items:
                text: str = item.find('span').text
                if query in text.lower():
                    link: str = f'{__URL["name"]}{item["href"]}'
                    rows.append([text, link])
        return tuple(rows)
    else:
        raise ('Sorry...I can not find page')
