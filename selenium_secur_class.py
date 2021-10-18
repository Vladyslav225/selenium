from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import antigravity


driver = webdriver.Chrome(executable_path='/home/vladyslav/IT_Step/lesson_25-26/chromedriver')


class MainPage_ChoosingProduct:

    def __init__(self, driver):
        self.driver = driver

    def main_page(self):
            
        try:
            self.driver.implicitly_wait(10)
            self.driver.get('https://secur.ua/')

        except:
            print('A site that does not exist or is incorrectly specified')
            exit()

    
    def element_search(self):

        try:
            self.driver.implicitly_wait(10)
            element_search = self.driver.find_element(By.ID, 'search')
            
            element_search.clear()
            element_search.send_keys('Видеокамера AHD купольная Tecsar AHDD-20V5M-in')
            element_search.send_keys(Keys.ENTER)

        except:
            print('Element with the specified "ID" was not found')
            exit()

    def choosing_product(self):

        try:
            self.driver.implicitly_wait(10)
            self.driver.find_element(By.CLASS_NAME, 'product-wrap').click()

        except:
            print('Element with the specified "CLASS_NAME" was not found')
            exit()

class SearchElementReview_WritingReview:
    def __init__(self, driver):
        self.driver = driver

    def search_element_review(self):

        try:
            self.driver.implicitly_wait(10)
            tabs_manu = driver.find_element(By.LINK_TEXT, 'Отзывы')
            tabs_manu.send_keys(Keys.RETURN)

        except:
            print('Element with the specified "link text" was not found')
            exit()

    def writing_review(self):
        try:
            self.driver.implicitly_wait(10)
            name = driver.find_element(By.ID, 'nickname_field')

            name.clear()
            name.send_keys('Vlad')

        except:
            print('Element with the specified "ID" was not found')
            exit()

        try:
            self.driver.implicitly_wait(10)
            email = driver.find_element(By.ID, 'summary_field')

            email.clear()
            email.send_keys('@')

        except:
            print('Element with the specified "ID" was not found')
            exit()
        
        try:
            self.driver.implicitly_wait(10)
            detail = driver.find_element(By.ID, 'review_field')

            detail.clear()
            detail.send_keys('Very good')

        except:
            print('Element with the specified "ID" was not found')
            exit()

        try:
            self.driver.implicitly_wait(10)
            pluses_product = driver.find_element(By.ID, 'pluses_product')

            pluses_product.clear()
            pluses_product.send_keys('Very-very good')

        except:
            print('Element with the specified "ID" was not found')
            exit()

        try:
            self.driver.implicitly_wait(10)
            lows_product = driver.find_element(By.ID, 'lows_product')

            lows_product.clear()
            lows_product.send_keys('Nope')

        except:
            print('Element with the specified "ID" was not found')
            exit()

        try:
            self.driver.implicitly_wait(10)
            driver.find_element(By.CLASS_NAME, 'btn.btn-silver.btn-review-post.button').click()

        except:
            print('Element with the specified "CLASS_NAME" was not found')
            exit()

        finally:
            time.sleep(10)
            driver.close()
            driver.quit()




first_class = MainPage_ChoosingProduct(driver)
first_class.main_page()
first_class.element_search()
first_class.choosing_product()

second_class = SearchElementReview_WritingReview(driver)
second_class.search_element_review()
second_class.writing_review()


