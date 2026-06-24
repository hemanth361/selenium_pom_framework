import pytest
import allure
from pages.inventory_page import InventoryPage


@allure.feature("Inventory")
class TestInventory:

    @allure.title("Inventory page loads with 6 products")
    @pytest.mark.smoke
    def test_product_count(self, inventory_page):
        assert inventory_page.get_product_count() == 6

    @allure.title("Products page title is 'Products'")
    @pytest.mark.smoke
    def test_page_title(self, inventory_page):
        assert inventory_page.get_page_title() == "Products"

    @allure.title("Add first product to cart increments badge")
    @pytest.mark.smoke
    def test_add_to_cart(self, inventory_page):
        inventory_page.add_first_item_to_cart()
        assert inventory_page.get_cart_count() == 1

    @allure.title("Add specific product by name")
    @pytest.mark.regression
    def test_add_specific_product(self, inventory_page):
        inventory_page.add_item_to_cart_by_name("Sauce Labs Backpack")
        assert inventory_page.get_cart_count() == 1

    @allure.title("Sort products A to Z")
    @pytest.mark.regression
    def test_sort_az(self, inventory_page):
        inventory_page.sort_products("az")
        names = inventory_page.get_product_names()
        assert names == sorted(names), "Products should be sorted A-Z"

    @allure.title("Sort products Z to A")
    @pytest.mark.regression
    def test_sort_za(self, inventory_page):
        inventory_page.sort_products("za")
        names = inventory_page.get_product_names()
        assert names == sorted(names, reverse=True), "Products should be sorted Z-A"
