from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
import os
PATH=("C:\Program Files (x86)\chromedriver.exe")
driver=webdriver.Chrome(PATH)
cwd_path=os.getcwd()
print(">>>>>>>",cwd_path,"<<<<<<<")

# create action chain object
action = ActionChains(driver)

def ja():
    #Test Case -Nein
    time.sleep(1)
    arrow = driver.find_element_by_xpath('//div[@data-testid="label-container" and @class="SingleAnswer_AnswerLabelContainer__316pD"]')
    arrow.click()

def roof_type(path):
    arrow = driver.find_element_by_xpath(path)
    arrow.click()

def homepage():
    driver.get("https://dynamic-slider-staging.azurewebsites.net/")
    print("site successfully loaded!")
    time.sleep(1)

def family_size(path):
    time.sleep(1)
    arrow = driver.find_element_by_xpath(path)
    arrow.click()

def daytime(path):
    time.sleep(1)
    arrow = driver.find_element_by_xpath(path)
    arrow.click()

def house_owner(path):
    time.sleep(1)
    arrow = driver.find_element_by_xpath(path)
    arrow.click()

def fill_form(path,keys):
    arrow=driver.find_element_by_xpath(path)
    arrow.send_keys(keys)
    
def age_check(path):
    time.sleep(1)
    arrow = driver.find_element_by_xpath(path)
    arrow.click()

def submit_button(path):
    arrow=driver.find_element_by_xpath(path)
    arrow.send_keys(Keys.ENTER)

def click(path):
    arrow=driver.find_element_by_xpath(path)
    arrow.click()
    
def upload_picture(element_path,local_picture_path):
    s = driver.find_element_by_xpath(element_path)
    s.send_keys(local_picture_path)
