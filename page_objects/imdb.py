from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

from .locators import IMDbPageLocators, pass_locator_params
from .base import BasePage


class IMDbPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver, "https://www.imdb.com")

    def search(self, query: str) -> None:
        search_bar = self._get_element(IMDbPageLocators.SEARCH)
        search_bar.send_keys(query)
        search_bar.send_keys(Keys.ENTER)

    def get_movies(self) -> set[str]:
        movies = self._get_elements(IMDbPageLocators.MOVIES)
        return set(movie.text for movie in movies)

    def open_movie_page(self, title: str) -> None:
        locator = pass_locator_params(IMDbPageLocators.MOVIE, movie=title)
        movie = self._get_element(locator)
        self._wait_for_redirect(lambda: movie.click())

    def get_movie_rating(self) -> float:
        rating = self._get_element(IMDbPageLocators.RATING)
        return float(rating.text)

    def get_movie_directors(self) -> set[str]:
        directors = self._get_elements(IMDbPageLocators.DIRECTORS)
        return set(director.text for director in directors)
