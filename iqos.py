from selenium import webdriver
from selenium.webdriver.support.ui import Select
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.set_window_size(1024, 600)
driver.maximize_window()
driver.implicitly_wait(3) # seconds
driver.execute_script("document.body.style.zoom='.6'")

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from win10toast import ToastNotifier
import time

driver.get("https://ba.iqos.com/")

driver.find_element(By.ID, value="onetrust-accept-btn-handler").click()

alSelect = driver.find_elements(By.CLASS_NAME, value='nbw-select-field')
for s in alSelect:
  Select(s).select_by_index(10)

driver.find_element(By.CLASS_NAME, value="nbw-button-primary").click()

driver.get("https://ba.iqos.com/bs/login?loginType=PASSWORD")

driver.find_element(By.CSS_SELECTOR, value='.login-page-content')

driver.find_element(By.CSS_SELECTOR, value="input.nbw-input-field[name='loginMethodInput']").send_keys("063577303")
driver.find_element(By.CSS_SELECTOR, value="input.nbw-input-password[name='loginMethodInput']").send_keys("Toshiba15")
driver.find_element(By.CSS_SELECTOR, value="input.nbw-input-password[name='loginMethodInput']").send_keys(Keys.ENTER)

ignoreTitle = ['Ulaznice za online predstavu "Zlatni lančić od bižuterije"', 'Pristup Arena Coud kanalima 2022', 'ulaznice za koncert Nina Badrić / Ana Rucner']
reload = True

time.sleep(1)

while reload:
  driver.get("https://ba.iqos.com/bs/loyalty/benefits/3?p=1")

  pogodnosti = driver.find_elements(By.CSS_SELECTOR, value='.nbw-benefit')
  driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.CONTROL + Keys.END)
  for p in pogodnosti:
    if p.find_element(By.CSS_SELECTOR, value='.text-title-10').text not in ignoreTitle:
      reload = False
      driver.execute_script("arguments[0].scrollIntoView(true);", p)
      eventName = p.find_element(By.CSS_SELECTOR, value='.text-title-10').text
      print('_______')
      print('PRONADJEN EVENT: ', eventName)
      print('_______')
      time.sleep(.4)
      p.find_element(By.CSS_SELECTOR, value=".comp-card-image-wrapper").click()
      driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.CONTROL + Keys.HOME)
      print('_______')
      print('IS ENABLED: ', driver.find_element(By.XPATH, '//button[contains(text(), "Preuzmi ovdje")]').is_enabled())
      print('_______')

      if(driver.find_element(By.XPATH, '//button[contains(text(), "Preuzmi ovdje")]').is_enabled()):
        driver.find_element(By.XPATH, '//button[contains(text(), "Preuzmi ovdje")]').click()

      toaster = ToastNotifier()
      toaster.show_toast(eventName,"Prikupi IQOS", duration=50, threaded=True)
      toaster.show_toast(eventName,"Prikupi IQOS", duration=50, threaded=True)
      toaster.show_toast(eventName,"NAGRADA", threaded=True)
      while toaster.notification_active(): time.sleep(0.1)
      time.sleep(1)
      driver.save_screenshot("event-"+eventName+".png")
    else:
      time.sleep(2)
    
