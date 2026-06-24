import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import Config


@allure.feature("Authentication")
@allure.story("Login")
class TestLogin:

    @allure.title("Successful login with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_valid_login(self, login_page):
        login_page.login(Config.STANDARD_USER, Config.PASSWORD)
        inventory = InventoryPage(login_page.driver)
        assert "inventory" in login_page.get_current_url(), \
            "Expected to be redirected to inventory page after login"
        assert inventory.get_page_title() == "Products"

    @allure.title("Login fails with incorrect password")
    @allure.severity(allure.severity_level.HIGH)
    @pytest.mark.regression
    @pytest.mark.login
    def test_invalid_password(self, login_page):
        login_page.login(Config.STANDARD_USER, "wrong_password")
        assert login_page.is_error_displayed(), "Expected error message to be visible"
        assert "Username and password do not match" in login_page.get_error_message()

    @allure.title("Login fails with empty username")
    @pytest.mark.regression
    @pytest.mark.login
    def test_empty_username(self, login_page):
        login_page.login("", Config.PASSWORD)
        assert login_page.is_error_displayed()
        assert "Username is required" in login_page.get_error_message()

    @allure.title("Login fails with empty password")
    @pytest.mark.regression
    @pytest.mark.login
    def test_empty_password(self, login_page):
        login_page.login(Config.STANDARD_USER, "")
        assert login_page.is_error_displayed()
        assert "Password is required" in login_page.get_error_message()

    @allure.title("Locked-out user cannot login")
    @pytest.mark.regression
    @pytest.mark.login
    def test_locked_user(self, login_page):
        login_page.login(Config.LOCKED_USER, Config.PASSWORD)
        assert login_page.is_error_displayed()
        assert "locked out" in login_page.get_error_message().lower()

    @allure.title("Login page title is correct")
    @pytest.mark.smoke
    def test_login_page_title(self, login_page):
        assert "Swag Labs" in login_page.get_title()


@allure.feature("Authentication")
@allure.story("Data-driven login")
class TestLoginParametrized:

    @pytest.mark.parametrize("username, password, expected_error", [
        ("",                    "secret_sauce",  "Username is required"),
        ("standard_user",       "",              "Password is required"),
        ("invalid_user",        "wrong_pass",    "Username and password do not match"),
        ("locked_out_user",     "secret_sauce",  "locked out"),
    ])
    @allure.title("Login validation - {username}")
    @pytest.mark.regression
    def test_invalid_credentials_parametrized(self, login_page, username, password, expected_error):
        login_page.login(username, password)
        assert login_page.is_error_displayed(), f"Expected error for user='{username}'"
        assert expected_error.lower() in login_page.get_error_message().lower()
