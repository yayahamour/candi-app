from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep 

driver = webdriver.Chrome('C://webdriver/chromedriver.exe')

url = 'https://candiapp.herokuapp.com/login'

driver.get(url)

print('------------------test login user1----------------------')
#instances of xpaths
user_xpath = "//*[@id='email']"
password_xpath = "//*[@id='password']"
button_click_xpath = '//*[@id="submit"]'

# I use find_element(By.XPATH, 'xpath') to find element
# And I use .send_keys('field') to enter strings in the field
driver.find_element(By.XPATH, user_xpath).send_keys('rudy@gmail.com')
driver.find_element(By.XPATH, password_xpath).send_keys('mdp')
driver.find_element(By.XPATH , button_click_xpath).click()
sleep(3)

# Assert flash connexion is ok 
flash_login_xpath = '/html/body/div'
flash_login = driver.find_element(By.XPATH , flash_login_xpath)
assert flash_login == 'Vous êtes connecté en tant que : Rudy Bourez'

# Assert h1 field is correct 
h1_xpath = "/html/body/section/h1"
h1 = driver.find_element(By.XPATH , h1_xpath)
assert h1.text == "CANDIDATURES"


print('------------------test add candidacy----------------------')
add_xpath = '/html/body/section/div[3]/a/button'
driver.find_element(By.XPATH, add_xpath).click()

entreprise_field_xpath = '//*[@id="name"]'
lieu_field_xpath = '//*[@id="place"]'
contact_field_xpath = '//*[@id="contact"]'
driver.find_element(By.XPATH, entreprise_field_xpath).send_keys('Apple') 
driver.find_element(By.XPATH, lieu_field_xpath).send_keys('Toulouse') 
driver.find_element(By.XPATH, contact_field_xpath).send_keys('Xavier') 
sleep(1)
add_xpath = '//*[@id="submit"]'
driver.find_element(By.XPATH, add_xpath).click()
sleep(1)
# Une fois la candidature soumise, je vérifie s'il apparait dans la board
#x_path susceptible de changé. Voir pour afficher les nouvelles candidature en premiere place ? 
td_entreprise_xpath = '/html/body/section/div[2]/table/tbody/tr[6]/td[1]'
td_entreprise = driver.find_element(By.XPATH, td_entreprise_xpath)
assert td_entreprise.text == "Apple"


print ('----------------Test logout---------------------------')
logout_xpath = '//*[@id="navbar"]/div/span[2]/a'
driver.find_element(By.XPATH, logout_xpath).click()
sleep(1)
flash_logout_xpath = '/html/body/div'
logout_flash = driver.find_element(By.XPATH , flash_logout_xpath)
assert logout_flash == 'Vous êtes correctement déconnecté'

print('----------------Test login with other user------------------')


print('--------------Test admin peut voir l\'ajout de candidature----------------')
# A faire 



driver.quit()

# Vérifié si on peut ajouter une candidature puis la retrouver dans board
# + A retrouver dans 
