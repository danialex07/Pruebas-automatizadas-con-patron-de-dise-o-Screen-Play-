from ui.catalog_ui import CatalogUi
from actions.display import Display
from actions.on_click import Click
from selenium import webdriver

class CatalogPage:

    def __init__(self, driver: webdriver):
        self.driver = driver

    def is_loaded(self):
        try:
            return Display().view_element(self.driver, CatalogUi().page_title)
        except Exception as inst:
            print("Error: Verifying Catalog Page", inst)

    def click_on_product(self, product_name):
        try:
            product_element = CatalogUi().get_product_by_name(product_name)
            Click().click(self.driver, product_element)
        except Exception as inst:
            print("Error: Clicking on product", inst)

    def add_to_cart(self):
        try:
            cart_button = CatalogUi().get_add_to_cart_button()
            Click().click(self.driver, cart_button)
        except Exception as inst:
            print("Error: Adding to cart", inst)
