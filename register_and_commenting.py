from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path='/home/vladyslav/IT_Step/lesson_25-26/chromedriver')

def main_page():

     try:

          driver.get('https://prom.ua/')

          button_sing_in = driver.find_element_by_css_selector('button.VspXp.aEPJa._3dQ3K')
          button_sing_in.send_keys(Keys.RETURN)
          time.sleep(3)

          number_input_field = driver.find_element_by_id('phone_field')
          number_input_field.send_keys('933832998')

          button_lod_in = driver.find_element_by_id('phoneEmailConfirmButton')
          button_lod_in.send_keys(Keys.RETURN)
          time.sleep(3)

          

          input_number_ = driver.find_element_by_id('verifyTempPassword')
          print(input_number_)
          

          # input_number_0 = driver.find_element_by_class_name('_1KcTA.O43e6._3iNcs._1zv6i._2qzjN._1aVgW')
          # input_number_0.send_keys(input(':'))

          # input_number_0 = driver.find_element_by_class_name('_1KcTA.O43e6._3iNcs._1zv6i._2qzjN._1aVgW')
          # input_number_0.send_keys(input(':'))

          # input_number_0 = driver.find_element_by_class_name('_1KcTA.O43e6._3iNcs._1zv6i._2qzjN._1aVgW')
          # input_number_0.send_keys(input(':'))

          # input_number_0 = driver.find_element_by_class_name('_1KcTA.O43e6._3iNcs._1zv6i._2qzjN._1aVgW')
          # input_number_0.send_keys(input(':'))

          # input_number_0 = driver.find_element_by_class_name('_1KcTA.O43e6._3iNcs._1zv6i._2qzjN._1aVgW')
          # input_number_0.send_keys(input(':'))

     except Exception as ex:
          print(ex)

     # finally:
     #      time.sleep(10)
     #      # driver.close()



main_page()