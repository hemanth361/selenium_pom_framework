from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    """Base page class — all page objects inherit from this."""

    DEFAULT_TIMEOUT = 10

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    # ── Navigation ────────────────────────────────────────────────────────
    def navigate_to(self, url: str) -> None:
        self.driver.get(url)

    def get_title(self) -> str:
        return self.driver.title

    def get_current_url(self) -> str:
        return self.driver.current_url

    # ── Wait helpers ──────────────────────────────────────────────────────
    def wait_for_element(self, locator: tuple, timeout: int = DEFAULT_TIMEOUT) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator: tuple, timeout: int = DEFAULT_TIMEOUT) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def is_element_visible(self, locator: tuple, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    # ── Interactions ──────────────────────────────────────────────────────
    def click(self, locator: tuple) -> None:
        self.wait_for_clickable(locator).click()

    def enter_text(self, locator: tuple, text: str) -> None:
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        return self.wait_for_element(locator).text

    def get_attribute(self, locator: tuple, attribute: str) -> str:
        return self.wait_for_element(locator).get_attribute(attribute)

    # ── Screenshot ────────────────────────────────────────────────────────
    def take_screenshot(self, name: str = "screenshot") -> None:
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
