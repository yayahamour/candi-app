from selenium import webdriver 


driver = webdriver.Chrome()

url = 'http://candi-data.herokuapp.com/login'

driver.get(url)

#Récupéré les xpath avec les balises html des champs email adress et password
user_xpath = ""
password_xpath = ""
button_click_xpath = ""

# On utilise la fonction  find_element_by_xpath
driver.find_element_by_xpath(user_xpath).send_keys('username-test')
driver.find_element_by_xpath(password_xpath).send_keys('password-Test')
driver.find_element_by_xpath(button_click_xpath).click()

# Pour etre sur d'être logué je pense mais à confirmer
driver.impcitly_wait(10)

text_inside_board_xpath = ""

text = driver.find_element_by_xpath(text_inside_board_xpath)

# Récupéré du conteneu apres avoir été logué. 
print(text) 


# driver.quit()

