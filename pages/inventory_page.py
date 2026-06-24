from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page object for the SauceDemo inventory/products page."""

    # ── Locators ──────────────────────────────────────────────────────────
    PAGE_TITLE        = (By.CLASS_NAME, "title")
    PRODUCT_ITEMS     = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES     = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BTN   = (By.CSS_SELECTOR, "[data-test^='add-to-cart']")
    CART_BADGE        = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON         = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN     = (By.CLASS_NAME, "product_sort_container")

    def __init__(self, driver):
        super().__init__(driver)

    # ── Actions ───────────────────────────────────────────────────────────
    def get_page_title(self) -> str:
        return self.get_text(self.PAGE_TITLE)

    def get_product_count(self) -> int:
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))

    def get_product_names(self) -> list:
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [el.text for el in elements]

    def add_first_item_to_cart(self) -> "InventoryPage":
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BTN)
        if buttons:
            buttons[0].click()
        return self

    def add_item_to_cart_by_name(self, product_name: str) -> "InventoryPage":
        locator = (By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
        self.click(locator)
        return self

    def get_cart_count(self) -> int:
        if self.is_element_visible(self.CART_BADGE, timeout=3):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def go_to_cart(self) -> None:
        self.click(self.CART_ICON)

    def sort_products(self, option_value: str) -> "InventoryPage":
        """Sort products. Values: 'az', 'za', 'lohi', 'hilo'"""
        from selenium.webdriver.support.ui import Select
        Select(self.wait_for_element(self.SORT_DROPDOWN)).select_by_value(option_value)
        return self
