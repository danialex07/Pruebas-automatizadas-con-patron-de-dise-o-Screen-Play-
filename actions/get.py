from selenium import webdriver


class Get:
    def get(self, driver: webdriver, locator):
        try:
            return driver.get(locator)
        except Exception as inst:
            print("Error: when get element", inst)
