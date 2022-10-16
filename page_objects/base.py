from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from typing import Callable


class BasePage:
    def __init__(self, driver: WebDriver, base_url: str) -> None:
        self.driver = driver
        self.base_url = base_url

    def __get_wait(self, timeout: int = 10) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout)

    def _get_elements(
        self, locator: tuple[str, str], timeout: int = 10
    ) -> list[WebElement]:
        try:
            wait = self.__get_wait(timeout)
            return wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            raise Exception("Could not find elements")

    def _get_element(
        self, locator: tuple[str, str], timeout: int = 10
    ) -> WebElement:
        elements = self._get_elements(locator, timeout)
        return elements[0]

    def _wait_for_redirect(
        self, redirect: Callable, timeout: int = 10
    ) -> None:
        wait = self.__get_wait(timeout)
        url = self.driver.current_url
        redirect()
        wait.until(EC.url_changes(url))

    def open_page(self) -> None:
        self.driver.get(self.base_url)

    def get_page_title(self) -> str:
        return self.driver.title
