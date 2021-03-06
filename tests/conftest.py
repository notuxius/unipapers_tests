import os
import sys

curr_dir = os.path.abspath(".")
sys.path.insert(0, curr_dir)

import pytest
from msedge.selenium_tools import Edge, EdgeOptions
from pages.home import HomePage


@pytest.fixture
def browser():
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument("-start-maximized")
    options.binary_location = (
        r"C:\Program Files (x86)\Microsoft\Edge Dev\Application\msedge.exe"
    )

    browser_location = os.path.join(curr_dir, "msedgedriver.exe")
    browser = Edge(options=options, executable_path=browser_location)

    yield browser
    browser.quit()


@pytest.fixture
def home_page(browser):
    home_page = HomePage(browser)

    return home_page
