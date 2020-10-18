from time import sleep

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def sleep_time():
    sleep(0.5)


class HomePage:
    URL = "https://unipapers.org/"

    ASSIGNMENT_DROPDOWN = (By.CSS_SELECTOR, "span.sod_select-assignment")
    ESSAY_OPTION = (By.XPATH, "//span[contains(@title, 'Essay')]")
    EDITING_OPTION = (By.XPATH, "//span[contains(@title, 'Editing')]")

    LEVEL_DROPDOWN = (By.CSS_SELECTOR, "span.sod_select-level")
    COLLEGE_OPTION = (By.XPATH, "//span[contains(@title, 'College')]")
    PROOFREADING_OPTION = (By.XPATH, "//span[contains(@title, 'Proofreading')]")

    DEADLINE_DROPDOWN = (By.CSS_SELECTOR, "span.sod_select-deadline")
    DAYS7_OPTION = (By.XPATH, "//span[contains(@title, '7 days')]")
    DAYS14_OPTION = (By.XPATH, "//span[contains(@title, '14 days')]")

    NUMPAGES_DROPDOWN = (By.CSS_SELECTOR, "span.sod_select-numpages")
    PAGES_1_275_WORDS_OPTION = (
        By.XPATH,
        "//span[contains(@title, '1 pages / 275 words')]",
    )
    PAGES_7_1925_WORDS_OPTION = (
        By.XPATH,
        "//span[contains(@title, '7 pages / 1925 words')]",
    )

    I_AM_A_NEW_CUSTOMER_CHECKBOX = (
        By.CSS_SELECTOR,
        "div.custom-control.custom-checkbox",
    )

    CURRENT_PRICE = (By.CSS_SELECTOR, "span.current-price")

    DISCOUNT_CHECKED = (By.CSS_SELECTOR, "form.checked")

    DISCOUNT_INFO = (By.CSS_SELECTOR, "div.discount-info")
    DISCOUNT_SIZE = (By.CSS_SELECTOR, "div.discount-info > div.discount-size")
    OLD_PRICE = (By.CSS_SELECTOR, "span#old-price")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def wait_for_elem(self, *elem_loc):
        elem = WebDriverWait(self.browser, 15).until(
            ec.visibility_of_element_located(elem_loc)
        )

        return elem

    def wait_for_elem_and_click(self, *elem_loc):

        elem = self.wait_for_elem(*elem_loc)
        elem.click()

        sleep_time()

    def calculate_default_price(self):
        self.wait_for_elem_and_click(*self.ASSIGNMENT_DROPDOWN)
        self.wait_for_elem_and_click(*self.ESSAY_OPTION)

        self.wait_for_elem_and_click(*self.LEVEL_DROPDOWN)
        self.wait_for_elem_and_click(*self.COLLEGE_OPTION)

        self.wait_for_elem_and_click(*self.DEADLINE_DROPDOWN)
        self.wait_for_elem_and_click(*self.DAYS14_OPTION)

        self.wait_for_elem_and_click(*self.NUMPAGES_DROPDOWN)
        self.wait_for_elem_and_click(*self.PAGES_1_275_WORDS_OPTION)

    def calculate_custom_price(self):
        self.wait_for_elem_and_click(*self.ASSIGNMENT_DROPDOWN)
        self.wait_for_elem_and_click(*self.EDITING_OPTION)

        self.wait_for_elem_and_click(*self.LEVEL_DROPDOWN)
        self.wait_for_elem_and_click(*self.PROOFREADING_OPTION)

        self.wait_for_elem_and_click(*self.DEADLINE_DROPDOWN)
        self.wait_for_elem_and_click(*self.DAYS7_OPTION)

        self.wait_for_elem_and_click(*self.NUMPAGES_DROPDOWN)
        self.wait_for_elem_and_click(*self.PAGES_7_1925_WORDS_OPTION)

        self.click_i_am_a_new_customer_checkbox()

    def click_i_am_a_new_customer_checkbox(self):
        self.wait_for_elem_and_click(*self.I_AM_A_NEW_CUSTOMER_CHECKBOX)

    def discount_info_is_displayed(self):
        return self.browser.find_element(*self.DISCOUNT_INFO).is_displayed()

    def discount_is_checked(self):
        with pytest.raises(NoSuchElementException):
            return self.browser.find_element(*self.DISCOUNT_CHECKED)

    def current_price(self):
        current_price = self.browser.find_element(*self.CURRENT_PRICE)

        return current_price.text

    def old_price(self):
        old_price = self.browser.find_element(*self.OLD_PRICE)

        return old_price.text

    def discount_size(self):
        discount_size = self.browser.find_element(*self.DISCOUNT_SIZE)

        return discount_size.text
