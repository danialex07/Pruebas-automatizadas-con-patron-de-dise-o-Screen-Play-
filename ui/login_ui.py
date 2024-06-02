"""
Locators login page.
"""


class LoginUi:
    base_url = "https://www.saucedemo.com/"
    # xpath_image_login = '//*[@id="root"]/div/div[2]/div[1]/div[2]'
    input_user = 'user-name'
    input_password = 'password'
    button = '//*[@id="login-button"]'
    xpath_page_init = '//*[@id="header_container"]/div[2]/span'
    xpath_alert_error = '//*[@id="login_button_container"]/div/form/div[3]/h3'
