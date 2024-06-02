import pytest
from splinter import Browser

@pytest.fixture
def browser():
    browser = Browser()
    yield browser
    browser.quit()