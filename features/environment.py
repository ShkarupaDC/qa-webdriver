from behave import fixture, use_fixture
from behave.runner import Context
from selenium.webdriver import Firefox
from typing import Generator

from page_objects.imdb import IMDbPage


@fixture
def init_firefox(context: Context) -> Generator[Context, None, None]:
    firefox = Firefox()
    imdb = IMDbPage(firefox)
    context.imdb = imdb

    yield context
    firefox.quit()


def before_all(context: Context) -> None:
    use_fixture(init_firefox, context)
