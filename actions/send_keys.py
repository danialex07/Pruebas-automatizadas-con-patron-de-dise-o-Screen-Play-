from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SendKeys:
    def send_text(self, driver: webdriver, locator, text):
        return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, locator))).send_keys(text)
