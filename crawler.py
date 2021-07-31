import time
import random
import os 

from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv

load_dotenv()

instagram_username = os.environ.get('instagram_username')
instagram_password = os.environ.get('instagram_password')

executable_path = '/usr/chromedriver'
options = Options()
options.headless = False
driver = Chrome(executable_path, options=options)

users = []

def check_exists_element(class_name):
    try:
        driver.find_element_by_class_name(class_name)
    except NoSuchElementException:
        return False
    return True

def get_random_user():
  r = random.randint(0, len(users))
  user_name = users[r]
  return user_name

def init(post_url):
  url = 'https://instagram.com/accounts/login'
  driver.get(url)

  time.sleep(3)

  user_input = driver.find_element_by_name('username')
  pass_input = driver.find_element_by_name('password')
  login_button = driver.find_element_by_xpath('//button[@type="submit"]')

  ActionChains(driver)\
    .move_to_element(user_input).click()\
    .send_keys(instagram_username)\
    .move_to_element(pass_input).click()\
    .send_keys(instagram_password)\
    .perform()
  
  login_button.click()
  time.sleep(3)

  driver.get(post_url)

  # while check_exists_element('dCJp8'):
  #   more_button = driver.find_element_by_class_name('dCJp8')
  #   more_button.click()
  #   time.sleep(1)
  
  time.sleep(2)
  comments = driver.find_elements_by_xpath('//h3[@class="_6lAjh "]/div/span/a')
  print('comments length', len(comments))

  for idx in range(len(comments)):
    comment = comments[idx]
    user_comment = comment.get_attribute('innerHTML')
    users.append(str(user_comment))

  random_user = get_random_user()
  
  time.sleep(5)
  driver.quit()
  return random_user





