from selenium.webdriver.common.by import By

from ui.login_ui import LoginUi
from actions.display import Display
from actions.get import Get
from actions.send_keys import SendKeys
from selenium import webdriver
from actions.on_click import Click
import time

class LoginPage:

    def init_page(self, driver: webdriver):
        try:
            Get().get(driver, LoginUi.base_url)
            driver.maximize_window()
            return Display().view_element(driver, LoginUi().button)
        except Exception as inst:
            print("Error: To init the request", inst)

    def enter_credential(self, driver: webdriver, user, password):
        try:
            SendKeys().send_text(driver, LoginUi().input_user, user)
            SendKeys().send_text(driver, LoginUi().input_password, password)
            Click().click(driver, LoginUi.button)
        except Exception as inst:
            print("Error: insert credential", inst)

    def obtain_element_home(self, driver):
        try:
            return Display().view_element(driver, LoginUi().xpath_page_init)
        except Exception as inst:
            print("Error:", inst)
    def obtain_element_login_failed(self, driver):
        try:
            return Display().view_element(driver, LoginUi().xpath_alert_error)
        except Exception as inst:
            print("Error 2", inst)

    def add_product_to_cart(self, driver):
        try:
            add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
            add_to_cart_button.click()
            time.sleep(5)  # Espera 5 segundos después de hacer clic en el botón de agregar al carrito
        except Exception as e:
            print("Error al agregar producto al carrito:", e)

    def navigate_to_cart(self, driver):
        try:
            cart_button = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
            cart_button.click()
            time.sleep(5)  # Espera 5 segundos después de hacer clic en el botón del carrito
        except Exception as e:
            print("Error al navegar al carrito:", e)