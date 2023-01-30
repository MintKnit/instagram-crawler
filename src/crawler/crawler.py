import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

username = "ampersandOr_"
password = input() # 땅콩

# create a new Firefox browser instance
driver = webdriver.Chrome(executable_path='../../lib/chromedriver')

driver.implicitly_wait(5)

# navigate to Instagram's login page
driver.get("https://www.instagram.com/accounts/login/")

# find the username and password input fields and enter your credentials
username_input = driver.find_element(By.NAME, 'username')
password_input = driver.find_element(By.NAME, "password")
username_input.send_keys(username)
password_input.send_keys(password)


# find the login button and click it
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()


driver.get("https://www.instagram.com/explore/tags/맛집/")

import time
time.sleep(10)



# navigate to a user's profile
driver.get("https://www.instagram.com/instagram/")

# find the number of posts on the user's profile
post_count = driver.find_element_by_xpath("//span[@class='g47SY ']")
print(f"{post_count.text} posts")

# find the number of followers on the user's profile
follower_count = driver.find_element_by_xpath("//a[@href='/instagram/followers/']/span")
print(f"{follower_count.text} followers")

# Close the browser
driver.close()

