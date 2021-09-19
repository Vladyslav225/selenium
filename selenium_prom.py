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
          number_input_field.send_keys('Input your phone number:')

          button_lod_in = driver.find_element_by_id('phoneEmailConfirmButton')
          button_lod_in.send_keys(Keys.RETURN)
          time.sleep(3)

          input_number_ = driver.find_elements_by_class_name('_1KcTA.O43e6._3iNcs._1zv6i._2qzjN._1aVgW')
          time.sleep(2)

          for n in input_number_:
               n.send_keys(input('Input code from your sms:'))

          time.sleep(3)

# #Подтверждение кода и Вход в аакаунт
          button_confirmation = driver.find_element_by_id('verifyTempPasswordConfirmButton')
          button_confirmation.send_keys(Keys.RETURN)

     except Exception as ex:
          print(ex)


def search():

     try:

          search_term = driver.find_element_by_class_name('_3tZPe')
          search_term.send_keys('Лицензионный ключ активации Windows 10 Pro + Ключ Office 2019 ProPlus')
          search_term.send_keys(Keys.RETURN)
          time.sleep(3)

          products = driver.find_elements_by_class_name('_2KaCs.xuuH_')[2]
          products.send_keys(Keys.ENTER)
          time.sleep(3)

     except Exception as ex:
          print(ex)


def writing_comment():

     try:
     
          comany_name = driver.find_element_by_class_name('_2KaCs.fxzyv._3y8C0.N4J0p')
          comany_name.send_keys(Keys.ENTER)
          time.sleep(3)

          short_company_rating = driver.find_elements_by_class_name('_2KaCs._2RuOC')[1]
          short_company_rating.send_keys(Keys.ENTER)
          time.sleep(3)

          button_create_company_opinion = driver.find_element_by_class_name('VspXp.aEPJa._3dQ3K.Keuxg')
          button_create_company_opinion.send_keys(Keys.ENTER)

          time.sleep(3)

#Здесь я думаю, как поставить 5 звезд

          # button_rating_label = driver.find_elements_by_class_name('_1KcTA.ggTpW._3TpPX._2wbE4.nN6NX._1v-n_')[4]
          # print(button_rating_label)
          # time.sleep(3)
          # button_rating_label.send_keys(Keys.ENTER)

          input_opinion_text = driver.find_element_by_class_name('_3Gj6W._1mkhj')
          input_opinion_text.send_keys('Все очень хорошо')

     except Exception as ex:
          print(ex)



main_page()
search()
writing_comment()

