from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome(executable_path='/home/vladyslav/IT_Step/lesson_25-26/chromedriver')


def main_page_search():

     try:

          driver.get('https://secur.ua/')

          element_search = driver.find_element_by_id('search')
          time.sleep(3)
          element_search.send_keys('Видеокамера AHD купольная Tecsar AHDD-20V5M-in')
          element_search.send_keys(Keys.ENTER)

          products_grid = driver.find_elements_by_class_name('product-wrap')[0]
          print(products_grid.text)
          time.sleep(3)

          products_grid.click()
          time.sleep(3)

     except Exception as ex:
          print(ex)


def product_page():

     try:

          tabs_manu = driver.find_element_by_link_text('Отзывы')
          tabs_manu.send_keys(Keys.RETURN)
          time.sleep(3)

     except Exception as ex:
          print(ex)


def review_form():

     try:

          name = driver.find_element_by_id('nickname_field')
          name.send_keys('asdd')

          email = driver.find_element_by_id('summary_field')
          email.send_keys('asd')

          detail = driver.find_element_by_id('review_field')
          detail.send_keys('asd')

          pluses_product = driver.find_element_by_id('pluses_product')
          pluses_product.send_keys('asd')

          lows_product = driver.find_element_by_id('lows_product')
          lows_product.send_keys('asd')

          button_send = driver.find_element_by_class_name('btn.btn-silver.btn-review-post.button').click()
          # print(button_send.text)

     except Exception as ex:
          print(ex)

     finally:
          driver.close()
          driver.quit()


main_page_search()
product_page()
review_form()
