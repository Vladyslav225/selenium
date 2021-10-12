from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome(executable_path='lesson_25-26/chromedriver')

def func_register():
     try:

          driver.get('https://pypi.org/account/register/')

          input_full_name = driver.find_element_by_id('full_name')
          input_full_name.clear()
          input_full_name.send_keys('Tester')

          input_email = driver.find_element_by_id('email')
          input_email.clear()
          input_email.send_keys('te433450@gmail.com')

          input_username = driver.find_element_by_id('username')
          input_username.clear()
          input_username.send_keys('dolvar')

          input_password = driver.find_element_by_id('new_password')
          input_password.clear()
          input_password.send_keys('')

          input_password_confirm = driver.find_element_by_id('password_confirm')
          input_password_confirm.send_keys('')
          input_password_confirm.send_keys(Keys.ENTER)

     except Exception as ex:
          print(ex)

     finally:
          time.sleep(5)
          driver.close()

# def func_log_in():

#      try:

#           driver.get('https://pypi.org/account/login/')

#           input_username = driver.find_element_by_id('username')
#           input_username.clear()
#           input_username.send_keys('dolvar')

#           input_password = driver.find_element_by_id('password')
#           input_password.clear()
#           input_password.send_keys('')
          
#           input_password.send_keys(Keys.ENTER)

#      except Exception as ex:
#           print(ex)

#      finally:
#           time.sleep(5)
#           driver.close()


# func_log_in()
func_register()