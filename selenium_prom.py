from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path='/home/vladyslav/IT_Step/lesson_25-26/chromedriver')

driver.get('https://prom.ua/')

def main_page_search():

     try:

          search_term = driver.find_element_by_class_name('_3tZPe')
          search_term.send_keys('Лицензионный ключ активации Windows 10 Pro + Ключ Office 2019 ProPlus')
          search_term.send_keys(Keys.RETURN)
          time.sleep(3)

          products = driver.find_elements_by_class_name('_2KaCs.xuuH_._3y8C0')[1]
          # print(products.text)

          products.send_keys(Keys.ENTER)
          time.sleep(3)

     except Exception as ex:
          print(ex)


def writing_comment():

     try:
     
          comany_name = driver.find_elements_by_class_name('_2KaCs._2RuOC')
          comany_name.send_keys(Keys.ENTER)
          time.sleep(5)

          # short_company_rating = driver.find_elements_by_class_name('_2KaCs._2RuOC')[1]
          # short_company_rating.send_keys(Keys.ENTER)
          # time.sleep(3)

          # button_create_company_opinion = driver.find_element_by_class_name('VspXp.aEPJa._3dQ3K.Keuxg')
          # button_create_company_opinion.send_keys(Keys.ENTER)
          # time.sleep(3)

          # number_input_field = driver.find_element_by_id('phone_field')
          # number_input_field.send_keys(input('Input your phone number (+380):'))

          # button_lod_in = driver.find_element_by_id('phoneConfirmButton')
          # button_lod_in.send_keys(Keys.RETURN)
          # time.sleep(3)

          # input_number_ = driver.find_elements_by_class_name('_1KcTA.O43e6._3iNcs._1zv6i._2qzjN._1aVgW')
          # time.sleep(2)

          # for items in input_number_:
          #      items.send_keys(input('Input code from your sms:'))

          # time.sleep(3)

          # button_confirmation = driver.find_element_by_id('verifyTempPasswordConfirmButton')
          # button_confirmation.send_keys(Keys.RETURN)

# #           button_rating_label = driver.find_elements_by_css_selector('div._1KcTA.ggTpW._3TpPX._2wbE4.nN6NX._1v-n_')[4]
# #           button_rating_label.click()
# #           time.sleep(3)

# #           button_checkbox = driver.find_elements_by_class_name('_3NYl6')[0]
# #           button_checkbox.click()

# #           input_opinion_text = driver.find_element_by_class_name('_3Gj6W._1mkhj')
# #           input_opinion_text.send_keys(input('Input your opinion_text:'))

     except Exception as ex:
          print(ex)

     # finally:
     #      time.sleep(10)
          # driver.close()


main_page_search()
writing_comment()


