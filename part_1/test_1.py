from test_page import OperationsHelper
import logging
import yaml


with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


def test_step_1(init_browser):
    logging.info("Test1 starting")
    test_page = OperationsHelper(init_browser)
    test_page.go_to_site()
    test_page.enter_login("test")
    test_page.enter_pass("test")
    test_page.click_login_button()
    assert test_page.get_error_text() == '401'


def test_step_2(init_browser):
    logging.info("Test2 starting")
    test_page = OperationsHelper(init_browser)
    test_page.go_to_site()
    test_page.enter_login(testdata['login'])
    test_page.enter_pass(testdata['password'])
    test_page.click_login_button()
    assert test_page.get_success_text() == f'Hello, {testdata["login"]}'


def test_step_3(init_browser):
    logging.info("Test3 starting")
    test_page = OperationsHelper(init_browser)
    test_page.go_to_site()
    test_page.enter_login(testdata['login'])
    test_page.enter_pass(testdata['password'])
    test_page.click_login_button()
    test_page.click_contact_us_button()
    test_page.enter_your_name(testdata['name'])
    test_page.enter_your_email(testdata['email'])
    test_page.content(testdata['content'])
    test_page.btn_contact_us()
    assert test_page.get_alert_text() == f'Form successfully submitted'

