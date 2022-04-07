
from selenium import webdriver
from Screenshot import Screenshot_Clipping
from PIL import Image
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
base_url="https://www.connectbudpro.com/"
driver=webdriver.Chrome(executable_path="/home/arnab/Downloads/chromedriver_linux64 (1)/chromedriver")
driver.get(base_url)
driver.maximize_window()
val = 10
driver.implicitly_wait(val) 
assert "Live 1:1 online Professional courses" in driver.title
# driver.implicitly_wait(val)
element=driver.find_element_by_xpath("/html/body/div/div/nav/div/div/ul/a[2]")
element.click()
print(element)
time.sleep(5)
user=driver.find_element_by_xpath("/html/body/div/div/section[1]/div/div/div/div/div[2]/div/form/div[1]/div/div/input")
user.send_keys('krishanu.das@cbnits.com')
password=driver.find_element_by_xpath("/html/body/div/div/section[1]/div/div/div/div/div[2]/div/form/div[2]/div/div/input")
password.send_keys('@dmiN007')
button=driver.find_element_by_xpath("/html/body/div/div/section[1]/div/div/div/div/div[2]/div/form/div[4]/div/button")
button.click()
# driver.implicitly_wait(val) 
time.sleep(5)
skip=driver.find_element_by_css_selector("body > div:nth-child(7) > div > div.modal.fade.show > div > div > div.custm_Mftr.modal-footer > div > button:nth-child(1)")
skip.click()
driver.get(driver.current_url)
print(driver.current_url)
time.sleep(5)
profileicon=driver.find_element_by_xpath("/html/body/div/div/nav/div/div/div[2]/div[1]")
profileicon.click()
profileview=driver.find_element_by_xpath("/html/body/div/div/nav/div/div/div[2]/div[2]/a[1]/span")
profileview.click()
time.sleep(5)
driver.get(driver.current_url)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
time.sleep(5)
for i in range(400):
    #ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    driver.execute_script("window.scrollBy(0,1)")
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight/5.4);")
time.sleep(3)
profileEdit=driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div/div[2]/div/div[1]/div[3]/h5/a/button")
profileEdit.click()

time.sleep(5)

profileimageselect=driver.find_element_by_xpath("/html/body/div/div/div/div[2]/section/div/div/div/div/div/div[2]/div/div[2]/button")
profileimageselect.click()


time.sleep(5)

profileimagechange=driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div[2]/div/div/input")
# profileimagechange.click()
profileimagechange.send_keys("/home/arnab/Downloads/pro.png")


time.sleep(5)

profileimageuploadbutton=driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div[3]/div/button[2]")
profileimageuploadbutton.click()


# ss = Screenshot_Clipping.Screenshot()
# driver.get(driver.current_url)
# image = ss.full_Screenshot(driver, save_path='/home/arnab/Downloads' , image_name='profile.png')

# screen = Image.open(image)
# screen.show()

# driver.close()
