from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

email = "*********"
password = "*******"

ig_username = "s******"
ig_password = "*********"

username_to_enter = "virat.kohli"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.instagram.com/")
sleep(5)

fb_login_btn = driver.find_element(By.CLASS_NAME,
                                   "_ab37")
fb_login_btn.click()

email_btn = driver.find_element(By.NAME, "email")
password_btn = driver.find_element(By.NAME, "pass")

email_btn.send_keys(email)
password_btn.send_keys(password)

password_btn.send_keys(Keys.ENTER)

sleep(10)

notification_btn = driver.find_element(By.XPATH,
                                       '//button[@class="_a9-- _ap36 _a9_1"]')
notification_btn.click()

sleep(2)
search_btn = driver.find_element(By.XPATH,
                                 "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[1]/div")
search_btn.click()

sleep(2)
search = driver.find_element(By.XPATH,
                             "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input")
search.send_keys(username_to_enter)

sleep(2)
acc_select = driver.find_element(By.XPATH,
                                 "(//div[@class='x9f619 x1n2onr6 x1ja2u2z x78zum5 x2lah0s x1qughib x6s0dn4 xozqiw3 x1q0g3np'])[1]")

# (//div[@class="x9f619 x1n2onr6 x1ja2u2z x78zum5 x1iyjqo2 xs83m0k xeuugli x1qughib x6s0dn4 x1a02dak x1q0g3np xdl72j9"])[1]
acc_select.click()

sleep(5)
follower_btn = driver.find_element(By.XPATH,
                                   "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a")
follower_btn.click()
#
# sleep(4)
# modal=driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div/button')
# modal.click()
sleep(4)
for i in range(1, 10):
        try:
            follow = driver.find_element(By.XPATH,
                                              f'(//div[@class="_ap3a _aaco _aacw _aad6 _aade"])[{i+1}]')
            follow.click()
            sleep(2)
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follow)
        except ElementClickInterceptedException:
            cancel_button = driver.find_element(By.XPATH,
                                                     "/html/body/div[2]/div/div/div/div[2]/div/div/div["
                                                     "2]/div/div/div[1]/div/div[ "
                                                     "2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
            cancel_button.click()
            sleep(1)

