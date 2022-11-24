# Generated by Selenium IDE
# El usuario ingresa 3 veces de manera erronea su contraseña y accede

import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSjs():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_sjs(self):
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(1936, 1056)
    self.driver.find_element(By.LINK_TEXT, "Sign In").click()
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("sample@example.com")
    self.driver.find_element(By.NAME, "password").send_keys("error")
    self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("sample@example.com")
    self.driver.find_element(By.NAME, "password").send_keys("error2")
    self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("sample@example.com")
    self.driver.find_element(By.NAME, "password").send_keys("error3")
    self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("sample@example.com")
    self.driver.find_element(By.NAME, "password").send_keys("sample")
    self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    user_name = self.driver.find_element(By.CLASS_NAME,"dropbtn").text
    assert "Sample" in user_name
  
