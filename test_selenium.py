from test_selenium_func import Selenium_test,  driver 
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep 


url = 'https://candiapp.herokuapp.com/login'

driver.get(url)

# -------------------- Starting test add candidacy with 2 accounts and tchek board with admin account--------------

Selenium_test.login_test(user='florian@gmail.com', password="1234")

# Second assert flash connexion more complete than this one in the function
flash_login_xpath = '//div[@class="alert alert-success alter-dismissable fade show"]'
flash_login = driver.find_element(By.XPATH , flash_login_xpath)
assert 'Vous êtes connecté en tant que : Florian Abgrall' in flash_login.text 
sleep(2)

# Add candidacy with first user
Selenium_test.add_candidacy_test(test_name="Apple", contact_test = "Steve Jobs")
sleep(2)

# logout first user
Selenium_test.logout_test()
sleep(2)

# Connexion with the second user
Selenium_test.click_login()
sleep(1)
Selenium_test.login_test(user='ayoub@gmail.com', password='lol')
sleep(2)

# Second assert flash connexion more complete than this one in the function
flash_login_xpath = '//div[@class="alert alert-success alter-dismissable fade show"]'
flash_login = driver.find_element(By.XPATH , flash_login_xpath)
assert 'Vous êtes connecté en tant que : Ayoub Haddou' in flash_login.text

# Add candidacy with the second user
Selenium_test.add_candidacy_test(test_name="Stars wars", contact_test='Dark Vador')
sleep(2)

# Go to admin account to tchek if both posts previously added are visible
Selenium_test.logout_test()
sleep(2)
Selenium_test.click_login()
Selenium_test.login_test(user='yanis@gmail.com', password="Admin")
sleep(2)

# Cheking 
candidacy_added_xpath = '//table/tbody/tr[2]/td[2]'
candidacy_added_2_xpath = '//table/tbody/tr[3]/td[2]'
candidacy_added = driver.find_element(By.XPATH, candidacy_added_xpath).text
candidacy_added_2 = driver.find_element(By.XPATH, candidacy_added_2_xpath).text
assert candidacy_added == 'Florian'
assert candidacy_added_2 == 'Ayoub'
print('--------Admin test done-------------') 

# Delete the posts previously added by user 1 and user 2 
Selenium_test.logout_test()
Selenium_test.click_login()
Selenium_test.login_test(user='florian@gmail.com', password="1234")
sleep(1)
Selenium_test.delete_candidacy_test()



# td_check_xpath = '//div[@class="tbl-content"]/table/tbody/tr[3]/td[7]/a[2]'
# td_chek = driver.find_element(By.XPATH, td_check_xpath)
# assert "Apple" not in td_chek 


sleep(2)
Selenium_test.logout_test()
sleep(1)
Selenium_test.click_login()
Selenium_test.login_test(user='ayoub@gmail.com', password='lol')
sleep(1)
Selenium_test.modify_candidacy()
sleep(2)
Selenium_test.delete_candidacy_test()
sleep(2)




Selenium_test.logout_test()
print('------------- Test finish with sucess ---------------')
sleep(1)
driver.quit()