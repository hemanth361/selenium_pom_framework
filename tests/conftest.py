import pytest
import allure
from utils.driver_factory import DriverFactory
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import Config


@pytest.fixture(scope="function")
def driver():
    """Provides a fresh WebDriver instance per test."""
    drv = DriverFactory.get_driver()
    yield drv
    drv.quit()


@pytest.fixture(scope="function")
def login_page(driver):
    """Returns an opened LoginPage."""
    return LoginPage(driver).open()


@pytest.fixture(scope="function")
def authenticated_driver(driver):
    """Returns a driver already logged in as standard user."""
    page = LoginPage(driver).open()
    page.login(Config.STANDARD_USER, Config.PASSWORD)
    return driver


@pytest.fixture(scope="function")
def inventory_page(authenticated_driver):
    """Returns an InventoryPage after successful login."""
    return InventoryPage(authenticated_driver)


def pytest_runtest_makereport(item, call):
    """Attach screenshot on test failure."""
    if call.when == "call" and call.excinfo is not None:
        driver = item.funcargs.get("driver") or item.funcargs.get("authenticated_driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
