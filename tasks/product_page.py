from ui.product_ui import ProductUi
from actions.display import Display
from selenium import webdriver

class ProductPage:

    def __init__(self, driver: webdriver):
        self.driver = driver

    def is_loaded(self):
        try:
            return Display().view_element(self.driver, ProductUi().page_title)
        except Exception as inst:
            print("Error: Verifying Product Page", inst)
