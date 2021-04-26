from selenium import webdriver
import re
import unittest
from functools import partial
from typing import NoReturn

from helpers import get_element_with_wait


class HotlineTestCase(unittest.TestCase):
    def setUp(self) -> NoReturn:
        self.driver = webdriver.Firefox()
        self.get_element = partial(get_element_with_wait, driver=self.driver)

    def test_category_selection(self, category: str = "Книги") -> NoReturn:
        self.driver.get("https://hotline.ua/")

        category_link = self.get_element(
            selector=f'[data-menu-main-item="{category}"] > a'
        )
        category_link.click()

        header = self.get_element(selector=".cell-12 > h1")
        assert header.text == category

    def test_filter_by_option(self, option: str = "1920-2000") -> NoReturn:
        self.driver.get("https://hotline.ua/computer/diski-ssd/")

        option_link = self.get_element(
            xpath=f'//a[contains(text(), "{option}")]'
        )
        option_link.click()

        label = option_link.get_attribute("data-eventlabel")
        match = re.match(r"^.*\[(\d+)\]$", label)

        if not match:
            raise Exception(f"Invalid option {option}")
        code = match.group(1)

        selected = self.get_element(
            selector=f'span[data-catalog-selected-filter="{code}"]'
        )
        selected_text = selected.get_attribute("innerText")
        assert selected_text == option

    def tearDown(self) -> NoReturn:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
