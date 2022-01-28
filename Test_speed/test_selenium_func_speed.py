from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep 

driver = webdriver.Chrome('C://webdriver/chromedriver.exe')

class Selenium_test:
    
    def login_test(user, password) :
        # Insert user and password in the login form 
        driver.find_element_by_id('email').send_keys(user)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_name('submit').click()
        
        # Assert h1 field is correct in this page
        h1 = driver.find_element_by_tag_name('h1')
        assert h1.text == "CANDIDATURES"
        # Assert Flash login success 
        flash_login = driver.find_element_by_class_name('alert')
        assert 'Vous êtes connecté en tant que :' in flash_login.text 
        print('------------------test login user Done----------------------')

    def add_candidacy_test(test_name, contact_test):
        # Click the button add candidacy
        # Need id button
        add_xpath = '//button[@class="btn btn-lg btn-primary mt-4 d-block"]/a'
        driver.find_element(By.XPATH, add_xpath).click()
        # Insert the candidacy in the form 
        driver.find_element_by_id('name').send_keys(test_name) 
    
        driver.find_element_by_id('place').send_keys('Lille') 

        driver.find_element_by_id('contact').send_keys(contact_test) 

        # Click on the button add candidacy
        driver.find_element_by_name('submit').click()

        # Assert flash element added success 
        flash_succes_xpath = '//div[@class="alert alert-success alter-dismissable fade show"]'
        flash_succes = driver.find_element_by_class_name('alert').text
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
        logout_xpath = '//body/nav/div[@class="col-3 text-right"]/span[2]'
        # driver.find_element_by_class_name('nav-link').click() [Need unique ID. Else xpath]
        driver.find_element(By.XPATH, logout_xpath).click()
        #Assert flash sucess loging 
        flash_logout = driver.find_element_by_class_name('alert')
        assert 'Vous êtes correctement déconnecté' in flash_logout.text
        print ('----------------Test logout done---------------------------')


    def click_login():
        # Need id 
        click_login_xpath = '//span/a[@class="nav-link"]'
        driver.find_element(By.XPATH, click_login_xpath).click()
        print('---------------Click to login---------------------------')

    def modify_candidacy():
        # Save init status text in status coloumn 
        status_xpath = '//tbody/tr[3]/td[6]'
        status_start = driver.find_element(By.XPATH, status_xpath).text
        
        modify_xpath = '//tbody/tr[3]/td[7]/a[1]'
        driver.find_element(By.XPATH, modify_xpath).click()
      
        driver.find_element_by_id('status').send_keys('Accepté')
        driver.find_element_by_id('button').click()
        
        status_end = driver.find_element(By.XPATH, status_xpath).text
        assert status_start != status_end
        print('----------------Test modify status Candidacy-------------')
        