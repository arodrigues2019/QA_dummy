import pytest
import allure
import time
from selenium import webdriver

@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="C:/Drivers/chromedriver.exe")
    driver.get("https://my-connect.qa.adaptiv-networks.com/")
    driver.maximize_window()
    yield
    driver.close()

@allure.description("Test successful login credential")
@allure.severity(severity_level="Normal")
def test_login_credential(test_setup):
    enter_username("arodrigues@adaptiv-networks.com")
    driver.find_element_by_xpath("//button[@name='action']").click()
    enter_password("Test@1234")
    driver.find_element_by_xpath("//button[@name='action']").click()
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="Successful Login Credentials", attachment_type=allure.attachment_type.PNG)

@allure.step("The username is {0}")
def enter_username(uname):
    driver.find_element_by_id("username").send_keys(uname)

@allure.step("The password is {0}")
def enter_password(pword):
    driver.find_element_by_id("password").send_keys(pword)

@allure.description("Test Invalid login credential")
def test_login_invalid_credentials(test_setup):
    enter_username("arodrigues@adaptiv-networks.com")
    driver.find_element_by_xpath("//button[@name='action']").click()
    enter_password("test1234")
    driver.find_element_by_xpath("//button[@name='action']").click()
    time.sleep(3)
    result = driver.find_element_by_id("error-element-password")
    allure.attach(driver.get_screenshot_as_png(), name="Invalid Login Credentials", attachment_type=allure.attachment_type.PNG)
    #print(result)
    #try:
    #    assert "error-element-password" in result
    #finally:
    #    if AssertionError:
    #        driver.get_screenshot_as_png()





#    try:
#        assert "my-connect.qa.adaptiv-networks.com" in driver.current_url
#    finally:
#        if AssertionError:
#            allure.attach(driver.get_screenshot_as_png(), name="url",
#                          attachment_type=allure.attachment_type.PNG)




