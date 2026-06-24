from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import Config


class LoginPage(BasePage):
    """Page object for the SauceDemo login page."""

    # ── Locators ──────────────────────────────────────────────────────────
    USERNAME_INPUT  = (By.ID, "user-name")
    PASSWORD_INPUT  = (By.ID, "password")
    LOGIN_BUTTON    = (By.ID, "login-button")
    ERROR_MESSAGE   = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    # ── Actions ───────────────────────────────────────────────────────────
    def open(self) -> "LoginPage":
        self.navigate_to(Config.BASE_URL)
        return self

    def enter_username(self, username: str) -> "LoginPage":
        self.enter_text(self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password: str) -> "LoginPage":
        self.enter_text(self.PASSWORD_INPUT, password)
        return self

    def click_login(self) -> None:
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> None:
        """Full login flow — chain of actions."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # ── Assertions ────────────────────────────────────────────────────────
    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self) -> bool:
        return self.is_element_visible(self.ERROR_MESSAGE)
