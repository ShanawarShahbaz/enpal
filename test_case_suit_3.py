
''' 
TestCase No : 3
Written by  : SHANAWAR 
Version     : v1.0
Last modified date : 30.04. 27
Company :     Enpal 
'''
#------------------------------------------------------------

import enpal_defination as enp
import os
#----------------------------------Test Case *navigation path*---------------------------------------
#Pultdach 
#->Dachfenster              | ja
#->Personen leben           |5 & more
#->electricity              |Night times
#->Eigentümer des Hauses    |ja
#ZipCode                    |"12345"
#ContactForm 
        #NAME :   "1223!@ 4_@!56789"
        #Address: "alexnder plazt strasse 23 12581 berlin"
        #phone :   "+491797266549"
        #email: "shan@mail.com"
#2-personen
#first click on above 70 , then click on below 70
#house description                                  | @#@#!@#!@#!@#@##$#@$
#Enter reminder phone number and get link on phone
#upload dachflahen photos                           | 9 photos with size more then10 MB per photo
#upload house surrouding                            | 2 photos
#upload meter pictures 2                            | 2 photos
#upload electricity bill pictures 2                 | 2 photos
#Finish

#-------------------------------------------------------------------------------------------------------------
#--------Test Case-1 - Sanity Check - Loading the dynamic0slider-staging.azurewebsites.net----------
enp.homepage() 

#--------------plutDach-----------------------------------------------------------
roof_path=arrow ='(//DIV[@data-testid="label-container"])[3]'
enp.roof_type(roof_path)

#---------------Dachfenter -weiS nicht---------------------------------------------
answer_type='(//DIV[@data-testid="label-container"])[3]'
enp.fenster_type(answer_type)

#-------------Personen leben->  1-2------------------------------------------------
family_path='(//DIV[@data-testid="label-container"])[3]'
enp.family_size(family_path)

#--------------electricity|night---------------------------------------------------
enp.time_path='(//DIV[@data-testid="label-container"])[2]'
enp.daytime(enp.time_path)

#--------------Eigentümer des Hauses--->ja----------------------------------------
house_path='(//DIV[@data-testid="label-container"])[1]'
enp.house_owner(house_path)
 
#--------------zip_code-----------------------------------------------------------
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
name_x='1223!@ 4_@!56789'
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
email_address="asdfsdafsdfsdffsdfsfsf19998888@co.com"
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

# ----registered household members--unknown------------------------------------------
enp.time.sleep(1)
enp.click('(//DIV[@data-testid="label-container"])[4]')


#---Agecheck : are you 70 or under 70------?
#--above_70()
age_path='(//DIV[@data-testid="label-container"])[2]'
enp.age_check(age_path)

#--below_70()
age_path='(//DIV[@data-testid="label-container"])[1]'
enp.age_check(age_path)

#---Description about house 250 lenth characters ---
text_house_description=''' @#@#!@#!@#!@#@##$#@$'''

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
enp.upload_picture(element_path,picture_path_2)
enp.upload_picture(element_path,picture_path_2)
enp.upload_picture(element_path,picture_path_1)
enp.upload_picture(element_path,picture_path_2)

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
