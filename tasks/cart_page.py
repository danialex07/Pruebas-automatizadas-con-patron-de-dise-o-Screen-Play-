from ui.cart_ui import CartUi
from actions.display import Display
from selenium import webdriver

class CartPage:

    def __init__(self, driver: webdriver):
        self.driver = driver

    def is_loaded(self):
        try:
            return Display().view_element(self.driver, CartUi().page_title)
        except Exception as inst:
            print("Error: Verifying Cart Page", inst)
