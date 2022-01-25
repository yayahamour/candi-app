from App import db 
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep 

driver = webdriver.Chrome('C://webdriver/chromedriver.exe')

class Selenium_test:
    
    def login_test(user, password) :
        # Xpath instances required to connect an account 
        user_xpath = "//input[@id='email']"
        password_xpath = "//input[@id='password']"
        button_click_xpath = '//input[@id="button"]'
        # Insert user and password in the login form 
        driver.find_element(By.XPATH, user_xpath).send_keys(user)
        sleep(1)
        driver.find_element(By.XPATH, password_xpath).send_keys(password)
        sleep(1)
        driver.find_element(By.XPATH , button_click_xpath).click()
        # Assert h1 field is correct in this page
        h1_xpath = "/html/body/section/h1"
        h1 = driver.find_element(By.XPATH , h1_xpath)
        assert h1.text == "CANDIDATURES"
        # Assert Flash login success 
        flash_login_xpath = '//div[@class="alert alert-success alter-dismissable fade show"]'
        flash_login = driver.find_element(By.XPATH , flash_login_xpath)
        assert 'Vous êtes connecté en tant que :' in flash_login.text 
        print('------------------test login user Done----------------------')


    def add_candidacy_test(test_name, contact_test):
        # Click the button add candidacy
        add_xpath = '//button[@class="btn btn-lg btn-primary mt-4 d-block"]/a'
        driver.find_element(By.XPATH, add_xpath).click()
        # Xpath instances required
        entreprise_field_xpath = '//*[@id="name"]'
        lieu_field_xpath = '//*[@id="place"]'
        contact_field_xpath = '//*[@id="contact"]'
        # Insert the candidacy in the form 
        driver.find_element(By.XPATH, entreprise_field_xpath).send_keys(test_name) 
        sleep(1)
        driver.find_element(By.XPATH, lieu_field_xpath).send_keys('Lille') 
        sleep(1)
        driver.find_element(By.XPATH, contact_field_xpath).send_keys(contact_test) 
        sleep(1)
        # Click on the button add candidacy
        add_xpath = '//input[@id="button"]'
        driver.find_element(By.XPATH, add_xpath).click()
        sleep(5)
        # Assert flash element added success 
        flash_succes_xpath = '//div[@class="alert alert-success alter-dismissable fade show"]'
        flash_succes = driver.find_element(By.XPATH, flash_succes_xpath).text
        assert 'Nouvelle Candidature ajouté' in flash_succes 
        # Assert element is on dashboard's following place => Front test
        td_entreprise_xpath = '//div[@class="tbl-content"]/table/tbody/tr[3]/td[2]'
        td_entreprise = driver.find_element(By.XPATH, td_entreprise_xpath)
        assert td_entreprise.text == test_name
        print('------------------test add candidacy Done----------------------')


    def delete_candidacy_test() :
        # Click on the third button delete item 
        delete_xpath = '//div[@class="tbl-content"]/table/tbody/tr[3]/td[7]/a[2]'
        driver.find_element(By.XPATH, delete_xpath).click()
        # assert 'word' not in [xpath row[1]] need order dashboard by last added
        # Or need to use Candidacy.query.filter_by(name=[element to check]) methods ?
        print('------------------delete candidacy n°3 done----------------------')
        


    def logout_test():
        # Click on button logout 
        logout_xpath = '//body/nav/div[@class="col-3"]/span[2]'
        driver.find_element(By.XPATH, logout_xpath).click()
        sleep(0.25)
        #Assert flash sucess loging 
        flash_logout_xpath = '//div[@class="alert alert-success alter-dismissable fade show"]'
        flash_logout = driver.find_element(By.XPATH , flash_logout_xpath)
        assert 'Vous êtes correctement déconnecté' in flash_logout.text
        print ('----------------Test logout done---------------------------')


    def click_login():
        click_login_xpath = '//span/a[@class="nav-link"]'
        driver.find_element(By.XPATH, click_login_xpath).click()
        sleep(1)
        print('---------------Click to login---------------------------')

    def modify_candidacy():
        status_start_xpath = '//tbody/tr[3]/td[6]'
        status_start = driver.find_element(By.XPATH, status_start_xpath).text
        modify_xpath = '//tbody/tr[3]/td[7]/a[1]'
        driver.find_element(By.XPATH, modify_xpath).click()
        field_status_xpath = '//input[@id="status"]'
        driver.find_element(By.XPATH, field_status_xpath).send_keys('Accepté')
        validate_button_xpath = '//input[@id="button"]'
        driver.find_element(By.XPATH, validate_button_xpath).click()
        status_end = driver.find_element(By.XPATH, status_start_xpath).text
        assert status_start != status_end
        print('----------------Test modify status Candidacy-------------')
        