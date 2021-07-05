var webdriver =require('selenium-webdriver'),
    by =webdriver.By,
    until =webdriver.until;

var driver = new webdriver.Builder().forBrowser('chrome')
.build();
driver.manage().window().maximize();

function callinghomepage() {
    return new Promise(resolve => {
      setTimeout(() => {
        portal_link='https://www.enpal.de/test/staging-slider'    
        driver.get(portal_link)
        
        resolve('resolved');
      }, 1000);
    });
  }

function fillPassword_and_enter(passwordpath,password_Keys,submit_path,timeout) {
    return new Promise(resolve => {
      setTimeout(() => {   
        driver.findElement(webdriver.By.xpath(passwordpath) ).sendKeys(password_Keys)
        driver.findElement(webdriver.By.xpath(submit_path) ).click()
        resolve('Password written resolved');
      }, timeout);

    });
  }

function click_and_go(path,timeout) {
    return new Promise(resolve => {
      setTimeout(() => {   
        driver.findElement(webdriver.By.xpath(path) ).click()
        resolve('Operation done...');
      }, timeout);

    });
  }

function textbox_input(inboxpath,input,timeout) {
    return new Promise(resolve => {
      setTimeout(() => {   
        driver.findElement(webdriver.By.xpath(inboxpath) ).sendKeys(input)
        resolve('Text is written in the inbox');
      }, timeout);

    });
  }
  

  
  async function asyncCall() {
    
    console.log('--calling Homepage--');
    const homepage = await callinghomepage();
    console.log(homepage);

    console.log('--writing Password and hitting enter--');
    const fpassword = await fillPassword_and_enter("//INPUT[@type='password']",'123',"//INPUT[@type='submit']",2*1000);
    console.log(fpassword);

    console.log('--Click Roof Type--');
    const roof_type = await click_and_go("//div[@data-testid='label-container' and @class='SingleAnswer_AnswerLabelContainer__316pD']",1*1000);
    console.log(roof_type);

    console.log('--Click Fenster type--');
    const fenter_type = await click_and_go('//div[@data-testid="label-container" and @class="SingleAnswer_AnswerLabelContainer__316pD"]',1.5*1000);
    console.log(fenter_type);

    console.log('--Click Personen leben--');
    const personen_leben = await click_and_go('//div[@data-testid="label-container" and @class="SingleAnswer_AnswerLabelContainer__316pD"]',1.6*1000);
    console.log(personen_leben);

    console.log('--Click Electricity usage Morgen/evening --');
    const electricity_time = await click_and_go('//div[@data-testid="answer" and @class="SingleAnswer_Answer__sWhX8"]',1.7*1000);
    console.log(electricity_time);

    console.log('---Click house owner ?--');
    const house_owner = await click_and_go('((//DIV[@data-testid="label-container"])[1]/../../..//DIV[@data-testid="label-container"])[2]',1.8*1000);
    console.log(house_owner);

    console.log('--Writing Post code --');
    const post_box = await textbox_input('//INPUT[@name="zipCode"]',"12345",1.9*1000);
    console.log(post_box);

    const weite = await click_and_go('//BUTTON[@data-testid="submit"][text()="Weiter"]',2*1000);
    console.log(weite);

    console.log('--Writing Name --');
    const name = await textbox_input('//input[@name="name"]',"abc xyz",5*1000);
    console.log(name);

    console.log('--Writing address --');
    const address_ = await textbox_input('//input[@name="address"]',"alexzader",1*1000);
    console.log(address_);

    console.log('--Writing Handy nummber --');
    const handy = await textbox_input('//input[@name="phone"]',"123456789",1*1000);
    console.log(handy);
 
    console.log('--Writing Email address --');
    const email = await textbox_input('//input[@name="email"]',"TestCase_3@mailinator.com",1*1000);
    console.log(email);

    const get_info = await click_and_go('//BUTTON[@data-testid="submit" and @class="components_Button__25vC8"]',1.1*1000);
    console.log(get_info);

    const further = await click_and_go('//BUTTON[@data-testid="submit"][text()="Weiter"]',1.1*1000);
    console.log(further);


    // expected output: "resolved"
  }
  
  asyncCall();
  
