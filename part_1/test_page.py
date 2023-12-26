import time

from selenium.webdriver.common.alert import Alert

from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

from conftest import browser


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, '''//*[@id="login"]/div[1]/label/input''')
    LOCATOR_PASS_FIELD = (By.XPATH, '''//*[@id="login"]/div[2]/label/input''')
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, '''button''')
    LOCATOR_ERROR_FIELD = (By.XPATH, '''//*[@id="app"]/main/div/div/div[2]/h2''')
    LOCATOR_SUCCESS_FIELD = (By.XPATH, '''//*[@id="app"]/main/nav/ul/li[3]/a''')
    LOCATOR_CONTACT_TAB = (By.XPATH, '''//*[@id="app"]/main/nav/ul/li[2]/a''')
    LOCATOR_YOUR_NAME = (By.XPATH, '''//*[@id="contact"]/div[1]/label/input''')
    LOCATOR_YOUR_EMAIL = (By.XPATH, '''//*[@id="contact"]/div[2]/label/input''')
    LOCATOR_YOUR_CONTENT = (By.XPATH, '''//*[@id="contact"]/div[3]/label/span/textarea''')
    LOCATOR_CONTACT_US_BTN = (By.CSS_SELECTOR, '''button''')


class OperationsHelper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.init_browser = None

    def enter_login(self, word):
        logging.info(f"Senf {word} of element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Senf {word} of element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info('Click login button')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_success_text(self):
        success_field = self.find_element(TestSearchLocators.LOCATOR_SUCCESS_FIELD, time=2)
        text = success_field.text
        logging.info(f'We find text {text} in success field {TestSearchLocators.LOCATOR_PASS_FIELD[1]}')
        return text

    def click_contact_us_button(self):
        logging.info('Click Contact tab')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_TAB).click()

    def enter_your_name(self, word):
        logging.info(f"Send {word} of element {TestSearchLocators.LOCATOR_YOUR_NAME[1]}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_NAME, time=2)
        name_field.clear()
        name_field.send_keys(word)

    def enter_your_email(self, word):
        logging.info(f"Send {word} of element {TestSearchLocators.LOCATOR_YOUR_EMAIL[1]}")
        email_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_EMAIL, time=2)
        email_field.clear()
        email_field.send_keys(word)

    def content(self, word):
        logging.info(f"Send {word} of element {TestSearchLocators.LOCATOR_YOUR_CONTENT[1]}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_CONTENT, time=2)
        content_field.clear()
        content_field.send_keys(word)

    def btn_contact_us(self):
        logging.info('Click button Contact Us')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

    def get_alert_text(self):
        logging.info('Loading alert')
        time.sleep(4)
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        logging.info(f'Send of true text by test "{alert_text}"')
        return alert_text
