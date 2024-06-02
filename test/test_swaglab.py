import pytest
from actions.actor import Actor
from tasks.open_browser import OpenBrowser
from tasks.add_to_cart import AddToCart
from tasks.verify_cart_button import VerifyCartButton
from tasks.verify_item_in_cart import VerifyItemInCart

@pytest.fixture
def actor():
    actor = Actor("Tester")
    yield actor
    actor.quit()
def test_add_to_cart(actor):
    actor.can(OpenBrowser("https://www.saucedemo.com/"))
    actor.browser.find_by_id('user-name').fill('standard_user')
    actor.browser.find_by_id('password').fill('secret_sauce')
    actor.browser.find_by_name('login-button').click()

    actor.can(AddToCart('sauce-labs-backpack'))
    actor.can(VerifyCartButton('sauce-labs-backpack'))
def test_item_in_cart(actor):
    actor.can(OpenBrowser("https://www.saucedemo.com/"))
    actor.browser.find_by_id('user-name').fill('standard_user')
    actor.browser.find_by_id('password').fill('secret_sauce')
    actor.browser.find_by_name('login-button').click()

    actor.can(AddToCart('sauce-labs-backpack'))
    actor.browser.find_by_css('.shopping_cart_link').click()
    actor.can(VerifyItemInCart())
