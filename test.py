import re
import unittest
from typing import NoReturn

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class HotlineTestCase(unittest.TestCase):
    def setUp(self) -> NoReturn:
        self.driver = webdriver.Firefox()

    def get_with_wait(
        self, xpath: str = None, selector: str = None, timeout: int = 10
    ) -> WebElement:
        if xpath is None and selector is None:
            raise Exception("Find option is not defined")
        try:
            wait = WebDriverWait(self.driver, timeout)
            locator = (
                (By.XPATH, xpath) if xpath is not None
                else (By.CSS_SELECTOR, selector)
            )
            return wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise Exception("Could not find element")

    def test_category_selection(self, category: str = "Книги") -> NoReturn:
        self.driver.get("https://hotline.ua/")

        category_link = self.get_with_wait(
            selector=f'[data-menu-main-item="{category}"] > a'
        )
        category_link.click()

        header = self.get_with_wait(selector=".cell-12 > h1")
        assert header.text == category

    def test_filter_by_option(self, option: str = "1920-2000") -> NoReturn:
        self.driver.get("https://hotline.ua/computer/diski-ssd/")

        option_link = self.get_with_wait(
            xpath=f'//a[contains(text(), "{option}")]'
        )
        option_link.click()

        label = option_link.get_attribute("data-eventlabel")
        match = re.match(r'^.*\[(\d+)\]$', label)

        if not match:
            raise Exception(f"Invalid option {option}")
        code = match.group(1)

        selected = self.get_with_wait(
            selector=f'span[data-catalog-selected-filter="{code}"]'
        )
        selected_text = selected.get_attribute("innerText")
        assert selected_text == option

    def tearDown(self) -> NoReturn:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
