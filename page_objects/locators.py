from selenium.webdriver.common.by import By


class IMDbPageLocators:
    SEARCH = (By.ID, "suggestion-search")
    MOVIES = (
        By.XPATH,
        """
        .//a[@name="tt"]/../../table[@class="findList"]//td
        [@class="result_text"]
        """,
    )
    MOVIE = (
        By.XPATH,
        """
        .//a[@name="tt"]/../../table[@class="findList"]//td
        [@class="result_text" and contains(., "{movie}")]/a
        """,
    )
    DIRECTORS = (
        By.XPATH,
        """
        //div[@class="credit_summary_item"]/h4[text()="Creator:"
        or text()="Director:"]/../a[starts-with(@href, "/name/")]
        """,
    )
    RATING = (By.CSS_SELECTOR, 'span[itemprop="ratingValue"]')
