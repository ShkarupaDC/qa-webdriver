from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def get_element_with_wait(
    driver, xpath: str = None, selector: str = None, timeout: int = 10
) -> WebElement:
    if xpath is None and selector is None:
        raise Exception("Find option is not defined")
    try:
        wait = WebDriverWait(driver, timeout)
        locator = (
            (By.XPATH, xpath) if xpath is not None
            else (By.CSS_SELECTOR, selector)
        )
        return wait.until(EC.presence_of_element_located(locator))
    except TimeoutException:
        raise Exception("Could not find element")
