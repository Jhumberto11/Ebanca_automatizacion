from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config.settings import settings
from core.exceptions import ElementNotFoundError


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, settings.wait_timeout)

    def open(self, url: str):
        self.driver.get(url)

    def find_first_visible(self, candidates):
        last_error = None

        for locator in candidates:
            try:
                return self.wait.until(
                    EC.visibility_of_element_located(locator)
                )
            except TimeoutException as exc:
                last_error = exc

        raise ElementNotFoundError(
            f"No se encontró ningún elemento de los candidatos: {candidates}"
        ) from last_error

    def find_first_clickable(self, candidates):
        last_error = None

        for locator in candidates:
            try:
                return self.wait.until(
                    EC.element_to_be_clickable(locator)
                )
            except TimeoutException as exc:
                last_error = exc

        raise ElementNotFoundError(
            f"No se encontró ningún elemento clickeable: {candidates}"
        ) from last_error

    def type_text(self, element, value: str, clear: bool = True):
        if clear:
            element.clear()
        element.send_keys(value)

    def click(self, element):
        element.click()
