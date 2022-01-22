from selenium import webdriver 
import time 

print('bonjour1')
driver = webdriver.Chrome('C://webdriver/chromedriver.exe')
time.sleep(5)
driver.maximize_window()
print('bonjour2')
url = 'https://www.manomano.fr/'

driver.get(url)

#Récupéré les xpath avec les balises html des champs email adress et password
foot_path = '//*[@id="lazyFooter"]/footer/div[3]'
print('bonjour3')

# On utilise la fonction  find_element_by_xpath
text = driver.find_element_by_xpath(foot_path)
print('bonjour4')

# Récupéré du conteneu apres avoir été logué. 
print('mon print : ', text) 

# driver.quit()
