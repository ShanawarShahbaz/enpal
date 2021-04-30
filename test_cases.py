from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

PATH=("C:\Program Files (x86)\chromedriver.exe")
driver=webdriver.Chrome(PATH)

# create action chain object
action = ActionChains(driver)

def ja():
    #Test Case -Nein
    time.sleep(1)
    arrow = driver.find_element_by_xpath('//div[@data-testid="label-container" and @class="SingleAnswer_AnswerLabelContainer__316pD"]')
    arrow.click()

def roof_type(path):
    arrow = driver.find_element_by_xpath('//div[@data-testid="label-container" and @class="SingleAnswer_AnswerLabelContainer__316pD"]')
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


#Test Case-1 - Sanity Check - Loading the dynamic0slider-staging.azurewebsites.net
homepage() 

# Test Case -Navigation -Accessing the roof type SattleDach
roof_path=arrow ='//div[@data-testid="label-container" and @class="SingleAnswer_AnswerLabelContainer__316pD"]'
roof_type(roof_path)
#sattelDach()

#Test Case -JA
ja()

#Test Case 1-2
family_path='//div[@data-testid="label-container" and @class="SingleAnswer_AnswerLabelContainer__316pD"]'
family_size(family_path)
#--------------
time_path='//div[@data-testid="answer" and @class="SingleAnswer_Answer__sWhX8"]'
daytime(time_path)
#----house owner-- ? JA or Nein ->Nein
house_path='((//DIV[@data-testid="label-container"])[1]/../../..//DIV[@data-testid="label-container"])[2]'
house_owner(house_path)
 
#---zip_code()
time.sleep(2)
zip_path='//INPUT[@name="zipCode"]'
zip_number="12345"
fill_form(zip_path,zip_number)

# ---Press Next/Submit/Weiter
zip_path='//BUTTON[@data-testid="submit"][text()="Weiter"]'
submit_button(zip_path)

#--wiriting name----------------
time.sleep(5)
name_path='//input[@name="name"]'
name_x='abc 123'
fill_form(name_path,name_x)

#----- writting address------
address_path='//input[@name="address"]'
address_x="alexnder plazt strasse 23 12581 berlin"
fill_form(address_path,address_x)

#------writing phone number
phone_path='//input[@name="phone"]'
phone_number="+491797266549"
fill_form(phone_path,phone_number)

#--writing email -----
email_path='//input[@name="email"]' 
email_address="shan@mail.com"
fill_form(email_path,email_address)

#---------Submit Contact details---
contact_form_button_path='//BUTTON[@data-testid="submit"]'
submit_button(contact_form_button_path)

#-----wait for script to run to submit contact details form----
time.sleep(4)
weiter_path='//BUTTON[@data-testid="submit"][text()="Weiter"]'
submit_button(weiter_path)

#--How many household are registers -initally click on 3 , to check the error message, then it will click on 2?-----------------------
time.sleep(1)
arrow = driver.find_element_by_xpath('(//DIV[@data-testid="label-container"])[3]')
arrow.click()

#----Check if the page is raising exception ,when 3 persons are selected 
arrow=driver.find_element_by_xpath('//DIV[@data-testid="disqualify-alert"]')
are_you_sure=arrow.get_attribute('innerHTML')
print(">>>>>>>>>>>>>>>>>>>>>>>>>",are_you_sure)

# ----click 2- registered household members
time.sleep(1)
arrow = driver.find_element_by_xpath('(//DIV[@data-testid="label-container"])[2]')
arrow.click()

#------------------------------------------------------------------------------------------------------------------------------------
#check : are you 70 or under 70 ?
#--above_70()
age_path='(//DIV[@data-testid="label-container"])[2]'
age_check(age_path)

#--below_70()
age_path='(//DIV[@data-testid="label-container"])[1]'
age_check(age_path)

#---Description about house 250 lenth characters ---
text_house_description=''' When the days are cold
And the cards all fold
And the saints we see
Are all made of gold
When your dreams all fail
And the ones we hail
Are the worst of all 
And the blood's run stale
This is my kingdom come  This is my kingdom come.This is my king'''

#---write_house_desciption-------
time.sleep(2)
house_path='//TEXTAREA[@name="freetext"]'
house_desc=text_house_description
fill_form(house_path,house_desc)

submit_button('//BUTTON[@data-testid="freetext-submit"]')

#//INPUT[@id='reminder-input']

#----goto-upload picures
time.sleep(1)
goto_picuters_path='//BUTTON[@data-testid="submit"]'
submit_button(goto_picuters_path)

#-----Upload picture button
#//*[@id="container_image-roof"]
#/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div/div[3]/div/form/input
#to identify element
def upload_picture(element_path,local_picture_path):
    s = driver.find_element_by_xpath(element_path)
    s.send_keys(local_picture_path)

element_path="/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div/div[3]/div/form/input[@type='file']"
picture_path_1="D:\\enpal\\a.jpg"
picture_path_2="D:\\enpal\\b.png"
picture_path_3="D:\\enpal\\script.sql"
upload_picture(element_path,picture_path_1)
upload_picture(element_path,picture_path_2)
upload_picture(element_path,picture_path_2)
upload_picture(element_path,picture_path_1)
upload_picture(element_path,picture_path_2)
upload_picture(element_path,picture_path_2)
upload_picture(element_path,picture_path_1)
upload_picture(element_path,picture_path_2)

upload_picture(element_path,picture_path_3)
