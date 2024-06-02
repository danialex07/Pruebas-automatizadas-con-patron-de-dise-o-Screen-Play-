import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from tasks.login_page import LoginPage
from tasks.catalog_page import CatalogPage
from tasks.cart_page import CartPage
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

class Test_Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test1_login_success(self):
        # Paso 1: Entrar a la página de login
        login_page = LoginPage()
        self.assertTrue(login_page.init_page(self.driver))

        # Paso 2: Logearse correctamente
        login_page.enter_credential(self.driver, 'standard_user', 'secret_sauce')

        # Verificar que estamos en la página de catálogos
        catalog_page = CatalogPage(self.driver)
        self.assertTrue(catalog_page.is_loaded(), "Catalog page is not loaded")

    def test2_add_product_to_cart(self):
        # Paso 3: Agregar el producto al carrito
        login_page = LoginPage()
        login_page.add_product_to_cart(self.driver)

        # Esperar un momento para asegurar que el producto se agregue correctamente al carrito
        time.sleep(5)

        # Verificar que estamos en la página del catálogo
        catalog_page = CatalogPage(self.driver)
        self.assertTrue(catalog_page.is_loaded(), "Catalog page is not loaded")

    def test3_goto_cart_page(self):
        # Paso 4: Navegar al carrito
        login_page = LoginPage()
        login_page.navigate_to_cart(self.driver)

        # Verificar que estamos en la página del carrito
        cart_page = CartPage(self.driver)
        self.assertTrue(cart_page.is_loaded(), "Failed to load cart page")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
