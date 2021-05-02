
''' 
TestCase No : 2
Written by  : SHANAWAR 
Version     : v1.0
Last modified date : 30.04. 27
Company :     Enpal 
'''
import enpal_defination as enp
import os


#----------------------------------------Test Case *navigation path*-----------------------------
#Flachdach 
#->Dachfenster              |Nein
#->Personen leben           |1-2
#->electricity              |Morgen&abends
#->Eigentümer des Hauses    |Nein
#->ZipCode                  |12345
#ContactForm 
        #NAME :    "abcefghijklmnoooooooooppppppppppp@ @xyzzzzzzzzzzzzzzzzzzzzz"
        #Address:  "alexnder plazt strasse 23 12581 berlin"
        #phone :   "+491797266549"
        #email:    "shan@mail.com"
#-> Personen stehen     | 2-personen
#click on above 70  
#Then click on below 70
#House description with Maximum number of characters | 250 characters
#Enter reminder phone number and get link on phone   | 1797266549
#upload dachflahen photos                            | 5 phots .jpeg,.png and sql script file
#upload house surrouding pictures                    | 2 phots .jpeg ,.png
#upload meter pictures                               | 2 phots .jpeg ,.png
#upload electricity bill pictures                    | 2 phots .jpeg ,.png
#Finish
#------------------------------------------------------------------------------------------------------------

#--------Test Case-1 - Sanity Check - Loading the dynamic0slider-staging.azurewebsites.net----------
enp.homepage() 

#--------------FlachDach---------------------------------------------------
roof_path=arrow ='(//DIV[@data-testid="label-container"])[2]'
enp.roof_type(roof_path)

#---------------Dachfenter -Nein---------------------------------------------
answer_type='(//DIV[@data-testid="label-container"])[2]'
enp.fenster_type(answer_type)

#-------------Personen leben->  1-2------------------------------------------
family_path='//div[@data-testid="label-container" and @class="SingleAnswer_AnswerLabelContainer__316pD"]'
enp.family_size(family_path)

#--------------electricity|Morgen_evening-------------------------------------
enp.time_path='//div[@data-testid="answer" and @class="SingleAnswer_Answer__sWhX8"]'
enp.daytime(enp.time_path)

#--------------Eigentümer des Hauses--->Nein-----------------------------------
house_path='((//DIV[@data-testid="label-container"])[1]/../../..//DIV[@data-testid="label-container"])[2]'
enp.house_owner(house_path)
 
#--------------zip_code--------------------------------------------------------
enp.time.sleep(2)
zip_path='//INPUT[@name="zipCode"]'
zip_number="12345"
enp.fill_form(zip_path,zip_number)

# ---Press Next/Submit/Weiter
zip_path='//BUTTON[@data-testid="submit"][text()="Weiter"]'
enp.submit_button(zip_path)

#--wiriting name----------------
enp.time.sleep(5)
name_path='//input[@name="name"]'
name_x='abcefghijklmnoooooooooppppppppppp@ @xyzzzzzzzzzzzzzzzzzzzzz'
enp.fill_form(name_path,name_x)

#----- writting address---------
address_path='//input[@name="address"]'
address_x="alexnder plazt strasse 23 12581 berlin"
enp.fill_form(address_path,address_x)

#------writing phone number----
phone_path='//input[@name="phone"]'
phone_number="+491797266549"
enp.fill_form(phone_path,phone_number)

#--writing email --------------
email_path='//input[@name="email"]' 
email_address="shan@mail.com"
enp.fill_form(email_path,email_address)

#---------Submit Contact details---
contact_form_button_path='//BUTTON[@data-testid="submit"]'
enp.submit_button(contact_form_button_path)

#-----wait for script to run to submit contact details form----
enp.time.sleep(4)
weiter_path='//BUTTON[@data-testid="submit"][text()="Weiter"]'
enp.submit_button(weiter_path)

#--How many household are registers -initally click on 3 , to check the error message, then it will click on 2?-----------------------
enp.time.sleep(2)
enp.click('(//DIV[@data-testid="label-container"])[3]')


#----Check if the page is raising exception ,when 3 persons are selected------------
arrow=enp.driver.find_element_by_xpath('//DIV[@data-testid="disqualify-alert"]')
are_you_sure=arrow.get_attribute('innerHTML')
print(">>>>>>>>>>>>>>>>>>>>>>>>>",are_you_sure)

# ----click 2- registered household members-------------------------------------------
enp.time.sleep(1)
enp.click('(//DIV[@data-testid="label-container"])[2]')


#---Agecheck : are you 70 or under 70------?
#--above_70()
age_path='(//DIV[@data-testid="label-container"])[2]'
enp.age_check(age_path)

#--below_70()
age_path='(//DIV[@data-testid="label-container"])[1]'
enp.age_check(age_path)

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
enp.time.sleep(2)
house_path='//TEXTAREA[@name="freetext"]'
house_desc=text_house_description
enp.fill_form(house_path,house_desc)
#---submit house description
enp.submit_button('//BUTTON[@data-testid="freetext-submit"]')

#----goto-upload picures
enp.time.sleep(1)
goto_picuters_path='//BUTTON[@data-testid="submit"]'
enp.submit_button(goto_picuters_path)

#-----start uploading pictueing from local dir
element_path="/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div/div[3]/div/form/input[@type='file']"
picture_path_1="D:\\enpal\\a.jpg"
picture_path_2="D:\\enpal\\b.png"
picture_path_3="D:\\enpal\\script.sql"
enp.upload_picture(element_path,picture_path_1)
enp.upload_picture(element_path,picture_path_2)
enp.upload_picture(element_path,picture_path_2)
enp.upload_picture(element_path,picture_path_1)


enp.upload_picture(element_path,picture_path_3)

#---submit phone number for reminder
enp.time.sleep(3)
enp.submit_button('//BUTTON[@type="submit"]')
enp.click('//A[@data-testid="next-step"]')

#---House with surrouding----

element_path="/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div/div[3]/div/form/input[@type='file']"
picture_path_1="D:\\enpal\\a.jpg"
picture_path_2="D:\\enpal\\b.png"
picture_path_3="D:\\enpal\\script.sql"
enp.upload_picture(element_path,picture_path_1)
enp.upload_picture(element_path,picture_path_2)
#---Next button for house surrounding
enp.click('//A[@data-testid="next-step"]')

#------meter picure---------------
element_path="/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div/div[3]/div/form/input"
picture_path_1="D:\\enpal\\a.jpg"
picture_path_2="D:\\enpal\\b.png"
picture_path_3="D:\\enpal\\script.sql"
enp.upload_picture(element_path,picture_path_1)
enp.upload_picture(element_path,picture_path_2)
enp.time.sleep(1)
enp.click('//A[@data-testid="next-step"]')
#------electric city bill pictures-------
element_path="/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div/div[3]/div/form/input"
picture_path_1="D:\\enpal\\a.jpg"
picture_path_2="D:\\enpal\\b.png"
picture_path_3="D:\\enpal\\script.sql"
enp.upload_picture(element_path,picture_path_1)
enp.upload_picture(element_path,picture_path_2)
enp.click('//A[@data-testid="next-step"]')

#-------Finish Button---------------------
enp.time.sleep(5)
element_path="/html/body/div/div[1]/div[1]/div/div/div[2]/div/div[3]/button"
enp.submit_button(element_path)

#--------More information button--------
element_path="/html/body/div/div[1]/div[1]/div/div/div[2]/div/div[3]/button[1]"
enp.submit_button(element_path)
